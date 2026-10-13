---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient
title: Cloud Storage v2 API - Class StorageControlClient (1.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:24.373329+00:00
---

# Cloud Storage v2 API - Class StorageControlClient (1.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Storage v2 API - Class StorageControlClient (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1 
    
    
    public abstract class StorageControlClient

Reference documentation and code samples for the Cloud Storage v2 API class StorageControlClient.

StorageControl client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StorageControlClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[StorageControlClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClientImpl)

## Namespace

[Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2)

## Assembly

Google.Cloud.Storage.Control.V2.dll

## Remarks

StorageControl service includes selected control plane operations.

## Properties 

### CreateAnywhereCacheOperationsClient
    
    
    public virtual OperationsClient CreateAnywhereCacheOperationsClient { get; }

The long-running operations client for `CreateAnywhereCache`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateRapidCacheOperationsClient
    
    
    public virtual OperationsClient CreateRapidCacheOperationsClient { get; }

The long-running operations client for `CreateRapidCache`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the StorageControl service, which is a host of "storage.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default StorageControl scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default StorageControl scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/cloud-platform.read-only>
  * <https://www.googleapis.com/auth/devstorage.full_control>
  * <https://www.googleapis.com/auth/devstorage.read_only>
  * <https://www.googleapis.com/auth/devstorage.read_write>



### DeleteFolderRecursiveOperationsClient
    
    
    public virtual OperationsClient DeleteFolderRecursiveOperationsClient { get; }

The long-running operations client for `DeleteFolderRecursive`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DisableRapidCacheOperationsClient
    
    
    public virtual OperationsClient DisableRapidCacheOperationsClient { get; }

The long-running operations client for `DisableRapidCache`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual StorageControl.StorageControlClient GrpcClient { get; }

The underlying gRPC StorageControl client

**Property Value**  
---  
**Type** | **Description**  
`[StorageControl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControl)[StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControl.StorageControlClient)` |   
  
### RenameFolderOperationsClient
    
    
    public virtual OperationsClient RenameFolderOperationsClient { get; }

The long-running operations client for `RenameFolder`.

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
  
### UpdateAnywhereCacheOperationsClient
    
    
    public virtual OperationsClient UpdateAnywhereCacheOperationsClient { get; }

The long-running operations client for `UpdateAnywhereCache`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateRapidCacheOperationsClient
    
    
    public virtual OperationsClient UpdateRapidCacheOperationsClient { get; }

The long-running operations client for `UpdateRapidCache`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static StorageControlClient Create()

Synchronously creates a [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [StorageControlClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient)` | The created [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient).  
  
### CreateAnywhereCache(BucketName, AnywhereCache, CallSettings)
    
    
    public virtual Operation<AnywhereCache, CreateAnywhereCacheMetadata> CreateAnywhereCache(BucketName parent, AnywhereCache anywhereCache, CallSettings callSettings = null)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. Properties of the Anywhere Cache instance being created. The parent bucket name is specified in the `parent` field. Server uses the default value of `ttl` or `admission_policy` if not specified in request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = storageControlClient.CreateAnywhereCache(parent, anywhereCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = storageControlClient.PollOnceCreateAnywhereCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAnywhereCache(CreateAnywhereCacheRequest, CallSettings)
    
    
    public virtual Operation<AnywhereCache, CreateAnywhereCacheMetadata> CreateAnywhereCache(CreateAnywhereCacheRequest request, CallSettings callSettings = null)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::CreateAnywhereCacheRequest request = new gcscv::CreateAnywhereCacheRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        AnywhereCache = new gcscv::AnywhereCache(),
    };
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = storageControlClient.CreateAnywhereCache(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = storageControlClient.PollOnceCreateAnywhereCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAnywhereCache(string, AnywhereCache, CallSettings)
    
    
    public virtual Operation<AnywhereCache, CreateAnywhereCacheMetadata> CreateAnywhereCache(string parent, AnywhereCache anywhereCache, CallSettings callSettings = null)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. Properties of the Anywhere Cache instance being created. The parent bucket name is specified in the `parent` field. Server uses the default value of `ttl` or `admission_policy` if not specified in request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = storageControlClient.CreateAnywhereCache(parent, anywhereCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = storageControlClient.PollOnceCreateAnywhereCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAnywhereCacheAsync(BucketName, AnywhereCache, CallSettings)
    
    
    public virtual Task<Operation<AnywhereCache, CreateAnywhereCacheMetadata>> CreateAnywhereCacheAsync(BucketName parent, AnywhereCache anywhereCache, CallSettings callSettings = null)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. Properties of the Anywhere Cache instance being created. The parent bucket name is specified in the `parent` field. Server uses the default value of `ttl` or `admission_policy` if not specified in request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = await storageControlClient.CreateAnywhereCacheAsync(parent, anywhereCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAnywhereCacheAsync(BucketName, AnywhereCache, CancellationToken)
    
    
    public virtual Task<Operation<AnywhereCache, CreateAnywhereCacheMetadata>> CreateAnywhereCacheAsync(BucketName parent, AnywhereCache anywhereCache, CancellationToken cancellationToken)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. Properties of the Anywhere Cache instance being created. The parent bucket name is specified in the `parent` field. Server uses the default value of `ttl` or `admission_policy` if not specified in request.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = await storageControlClient.CreateAnywhereCacheAsync(parent, anywhereCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAnywhereCacheAsync(CreateAnywhereCacheRequest, CallSettings)
    
    
    public virtual Task<Operation<AnywhereCache, CreateAnywhereCacheMetadata>> CreateAnywhereCacheAsync(CreateAnywhereCacheRequest request, CallSettings callSettings = null)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::CreateAnywhereCacheRequest request = new gcscv::CreateAnywhereCacheRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        AnywhereCache = new gcscv::AnywhereCache(),
    };
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = await storageControlClient.CreateAnywhereCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAnywhereCacheAsync(CreateAnywhereCacheRequest, CancellationToken)
    
    
    public virtual Task<Operation<AnywhereCache, CreateAnywhereCacheMetadata>> CreateAnywhereCacheAsync(CreateAnywhereCacheRequest request, CancellationToken cancellationToken)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::CreateAnywhereCacheRequest request = new gcscv::CreateAnywhereCacheRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        AnywhereCache = new gcscv::AnywhereCache(),
    };
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = await storageControlClient.CreateAnywhereCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAnywhereCacheAsync(string, AnywhereCache, CallSettings)
    
    
    public virtual Task<Operation<AnywhereCache, CreateAnywhereCacheMetadata>> CreateAnywhereCacheAsync(string parent, AnywhereCache anywhereCache, CallSettings callSettings = null)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. Properties of the Anywhere Cache instance being created. The parent bucket name is specified in the `parent` field. Server uses the default value of `ttl` or `admission_policy` if not specified in request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = await storageControlClient.CreateAnywhereCacheAsync(parent, anywhereCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAnywhereCacheAsync(string, AnywhereCache, CancellationToken)
    
    
    public virtual Task<Operation<AnywhereCache, CreateAnywhereCacheMetadata>> CreateAnywhereCacheAsync(string parent, AnywhereCache anywhereCache, CancellationToken cancellationToken)

Creates an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. Properties of the Anywhere Cache instance being created. The parent bucket name is specified in the `parent` field. Server uses the default value of `ttl` or `admission_policy` if not specified in request.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> response = await storageControlClient.CreateAnywhereCacheAsync(parent, anywhereCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::CreateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateAsync(CancellationToken)
    
    
    public static Task<StorageControlClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [StorageControlClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient)` | The task representing the created [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient).  
  
### CreateFolder(BucketName, Folder, string, CallSettings)
    
    
    public virtual Folder CreateFolder(BucketName parent, Folder folder, string folderId, CallSettings callSettings = null)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket in which the folder will reside. The bucket must be a hierarchical namespace enabled bucket.  
`folder` | `[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)`  
Required. Properties of the new folder being created. The bucket and name of the folder are specified in the parent and folder_id fields, respectively. Populating those fields in `folder` will result in an error.  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a folder, including all its parent folders. Folders use single '/' characters as a delimiter. The folder_id must end with a slash. For example, the folder_id of "books/biographies/" would create a new "biographies/" folder under the "books/" folder.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::Folder folder = new gcscv::Folder();
    string folderId = "";
    // Make the request
    gcscv::Folder response = storageControlClient.CreateFolder(parent, folder, folderId);
    

### CreateFolder(CreateFolderRequest, CallSettings)
    
    
    public virtual Folder CreateFolder(CreateFolderRequest request, CallSettings callSettings = null)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::CreateFolderRequest request = new gcscv::CreateFolderRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Folder = new gcscv::Folder(),
        FolderId = "",
        Recursive = false,
    };
    // Make the request
    gcscv::Folder response = storageControlClient.CreateFolder(request);
    

### CreateFolder(string, Folder, string, CallSettings)
    
    
    public virtual Folder CreateFolder(string parent, Folder folder, string folderId, CallSettings callSettings = null)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket in which the folder will reside. The bucket must be a hierarchical namespace enabled bucket.  
`folder` | `[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)`  
Required. Properties of the new folder being created. The bucket and name of the folder are specified in the parent and folder_id fields, respectively. Populating those fields in `folder` will result in an error.  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a folder, including all its parent folders. Folders use single '/' characters as a delimiter. The folder_id must end with a slash. For example, the folder_id of "books/biographies/" would create a new "biographies/" folder under the "books/" folder.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::Folder folder = new gcscv::Folder();
    string folderId = "";
    // Make the request
    gcscv::Folder response = storageControlClient.CreateFolder(parent, folder, folderId);
    

### CreateFolderAsync(BucketName, Folder, string, CallSettings)
    
    
    public virtual Task<Folder> CreateFolderAsync(BucketName parent, Folder folder, string folderId, CallSettings callSettings = null)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket in which the folder will reside. The bucket must be a hierarchical namespace enabled bucket.  
`folder` | `[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)`  
Required. Properties of the new folder being created. The bucket and name of the folder are specified in the parent and folder_id fields, respectively. Populating those fields in `folder` will result in an error.  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a folder, including all its parent folders. Folders use single '/' characters as a delimiter. The folder_id must end with a slash. For example, the folder_id of "books/biographies/" would create a new "biographies/" folder under the "books/" folder.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::Folder folder = new gcscv::Folder();
    string folderId = "";
    // Make the request
    gcscv::Folder response = await storageControlClient.CreateFolderAsync(parent, folder, folderId);
    

### CreateFolderAsync(BucketName, Folder, string, CancellationToken)
    
    
    public virtual Task<Folder> CreateFolderAsync(BucketName parent, Folder folder, string folderId, CancellationToken cancellationToken)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket in which the folder will reside. The bucket must be a hierarchical namespace enabled bucket.  
`folder` | `[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)`  
Required. Properties of the new folder being created. The bucket and name of the folder are specified in the parent and folder_id fields, respectively. Populating those fields in `folder` will result in an error.  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a folder, including all its parent folders. Folders use single '/' characters as a delimiter. The folder_id must end with a slash. For example, the folder_id of "books/biographies/" would create a new "biographies/" folder under the "books/" folder.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::Folder folder = new gcscv::Folder();
    string folderId = "";
    // Make the request
    gcscv::Folder response = await storageControlClient.CreateFolderAsync(parent, folder, folderId);
    

### CreateFolderAsync(CreateFolderRequest, CallSettings)
    
    
    public virtual Task<Folder> CreateFolderAsync(CreateFolderRequest request, CallSettings callSettings = null)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::CreateFolderRequest request = new gcscv::CreateFolderRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Folder = new gcscv::Folder(),
        FolderId = "",
        Recursive = false,
    };
    // Make the request
    gcscv::Folder response = await storageControlClient.CreateFolderAsync(request);
    

### CreateFolderAsync(CreateFolderRequest, CancellationToken)
    
    
    public virtual Task<Folder> CreateFolderAsync(CreateFolderRequest request, CancellationToken cancellationToken)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateFolderRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::CreateFolderRequest request = new gcscv::CreateFolderRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Folder = new gcscv::Folder(),
        FolderId = "",
        Recursive = false,
    };
    // Make the request
    gcscv::Folder response = await storageControlClient.CreateFolderAsync(request);
    

### CreateFolderAsync(string, Folder, string, CallSettings)
    
    
    public virtual Task<Folder> CreateFolderAsync(string parent, Folder folder, string folderId, CallSettings callSettings = null)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket in which the folder will reside. The bucket must be a hierarchical namespace enabled bucket.  
`folder` | `[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)`  
Required. Properties of the new folder being created. The bucket and name of the folder are specified in the parent and folder_id fields, respectively. Populating those fields in `folder` will result in an error.  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a folder, including all its parent folders. Folders use single '/' characters as a delimiter. The folder_id must end with a slash. For example, the folder_id of "books/biographies/" would create a new "biographies/" folder under the "books/" folder.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::Folder folder = new gcscv::Folder();
    string folderId = "";
    // Make the request
    gcscv::Folder response = await storageControlClient.CreateFolderAsync(parent, folder, folderId);
    

### CreateFolderAsync(string, Folder, string, CancellationToken)
    
    
    public virtual Task<Folder> CreateFolderAsync(string parent, Folder folder, string folderId, CancellationToken cancellationToken)

Creates a new folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket in which the folder will reside. The bucket must be a hierarchical namespace enabled bucket.  
`folder` | `[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)`  
Required. Properties of the new folder being created. The bucket and name of the folder are specified in the parent and folder_id fields, respectively. Populating those fields in `folder` will result in an error.  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The full name of a folder, including all its parent folders. Folders use single '/' characters as a delimiter. The folder_id must end with a slash. For example, the folder_id of "books/biographies/" would create a new "biographies/" folder under the "books/" folder.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::Folder folder = new gcscv::Folder();
    string folderId = "";
    // Make the request
    gcscv::Folder response = await storageControlClient.CreateFolderAsync(parent, folder, folderId);
    

### CreateManagedFolder(BucketName, ManagedFolder, string, CallSettings)
    
    
    public virtual ManagedFolder CreateManagedFolder(BucketName parent, ManagedFolder managedFolder, string managedFolderId, CallSettings callSettings = null)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket this managed folder belongs to.  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being created. The bucket and managed folder names are specified in the `parent` and `managed_folder_id` fields. Populating these fields in `managed_folder` will result in an error.  
`managedFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the managed folder. It uses a single `/` as delimiter and leading and trailing `/` are allowed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    string managedFolderId = "";
    // Make the request
    gcscv::ManagedFolder response = storageControlClient.CreateManagedFolder(parent, managedFolder, managedFolderId);
    

### CreateManagedFolder(CreateManagedFolderRequest, CallSettings)
    
    
    public virtual ManagedFolder CreateManagedFolder(CreateManagedFolderRequest request, CallSettings callSettings = null)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::CreateManagedFolderRequest request = new gcscv::CreateManagedFolderRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        ManagedFolder = new gcscv::ManagedFolder(),
        ManagedFolderId = "",
    };
    // Make the request
    gcscv::ManagedFolder response = storageControlClient.CreateManagedFolder(request);
    

### CreateManagedFolder(string, ManagedFolder, string, CallSettings)
    
    
    public virtual ManagedFolder CreateManagedFolder(string parent, ManagedFolder managedFolder, string managedFolderId, CallSettings callSettings = null)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket this managed folder belongs to.  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being created. The bucket and managed folder names are specified in the `parent` and `managed_folder_id` fields. Populating these fields in `managed_folder` will result in an error.  
`managedFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the managed folder. It uses a single `/` as delimiter and leading and trailing `/` are allowed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    string managedFolderId = "";
    // Make the request
    gcscv::ManagedFolder response = storageControlClient.CreateManagedFolder(parent, managedFolder, managedFolderId);
    

### CreateManagedFolderAsync(BucketName, ManagedFolder, string, CallSettings)
    
    
    public virtual Task<ManagedFolder> CreateManagedFolderAsync(BucketName parent, ManagedFolder managedFolder, string managedFolderId, CallSettings callSettings = null)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket this managed folder belongs to.  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being created. The bucket and managed folder names are specified in the `parent` and `managed_folder_id` fields. Populating these fields in `managed_folder` will result in an error.  
`managedFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the managed folder. It uses a single `/` as delimiter and leading and trailing `/` are allowed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    string managedFolderId = "";
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.CreateManagedFolderAsync(parent, managedFolder, managedFolderId);
    

### CreateManagedFolderAsync(BucketName, ManagedFolder, string, CancellationToken)
    
    
    public virtual Task<ManagedFolder> CreateManagedFolderAsync(BucketName parent, ManagedFolder managedFolder, string managedFolderId, CancellationToken cancellationToken)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket this managed folder belongs to.  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being created. The bucket and managed folder names are specified in the `parent` and `managed_folder_id` fields. Populating these fields in `managed_folder` will result in an error.  
`managedFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the managed folder. It uses a single `/` as delimiter and leading and trailing `/` are allowed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    string managedFolderId = "";
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.CreateManagedFolderAsync(parent, managedFolder, managedFolderId);
    

### CreateManagedFolderAsync(CreateManagedFolderRequest, CallSettings)
    
    
    public virtual Task<ManagedFolder> CreateManagedFolderAsync(CreateManagedFolderRequest request, CallSettings callSettings = null)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::CreateManagedFolderRequest request = new gcscv::CreateManagedFolderRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        ManagedFolder = new gcscv::ManagedFolder(),
        ManagedFolderId = "",
    };
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.CreateManagedFolderAsync(request);
    

### CreateManagedFolderAsync(CreateManagedFolderRequest, CancellationToken)
    
    
    public virtual Task<ManagedFolder> CreateManagedFolderAsync(CreateManagedFolderRequest request, CancellationToken cancellationToken)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::CreateManagedFolderRequest request = new gcscv::CreateManagedFolderRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        ManagedFolder = new gcscv::ManagedFolder(),
        ManagedFolderId = "",
    };
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.CreateManagedFolderAsync(request);
    

### CreateManagedFolderAsync(string, ManagedFolder, string, CallSettings)
    
    
    public virtual Task<ManagedFolder> CreateManagedFolderAsync(string parent, ManagedFolder managedFolder, string managedFolderId, CallSettings callSettings = null)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket this managed folder belongs to.  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being created. The bucket and managed folder names are specified in the `parent` and `managed_folder_id` fields. Populating these fields in `managed_folder` will result in an error.  
`managedFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the managed folder. It uses a single `/` as delimiter and leading and trailing `/` are allowed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    string managedFolderId = "";
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.CreateManagedFolderAsync(parent, managedFolder, managedFolderId);
    

### CreateManagedFolderAsync(string, ManagedFolder, string, CancellationToken)
    
    
    public virtual Task<ManagedFolder> CreateManagedFolderAsync(string parent, ManagedFolder managedFolder, string managedFolderId, CancellationToken cancellationToken)

Creates a new managed folder.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket this managed folder belongs to.  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being created. The bucket and managed folder names are specified in the `parent` and `managed_folder_id` fields. Populating these fields in `managed_folder` will result in an error.  
`managedFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the managed folder. It uses a single `/` as delimiter and leading and trailing `/` are allowed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    string managedFolderId = "";
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.CreateManagedFolderAsync(parent, managedFolder, managedFolderId);
    

### CreateRapidCache(BucketName, RapidCache, CallSettings)
    
    
    public virtual Operation<RapidCache, CreateRapidCacheMetadata> CreateRapidCache(BucketName parent, RapidCache rapidCache, CallSettings callSettings = null)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to create. Default values for ingest_on_write, ttl and admission_policy will be applied if not specified in the request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = storageControlClient.CreateRapidCache(parent, rapidCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = storageControlClient.PollOnceCreateRapidCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateRapidCache(CreateRapidCacheRequest, CallSettings)
    
    
    public virtual Operation<RapidCache, CreateRapidCacheMetadata> CreateRapidCache(CreateRapidCacheRequest request, CallSettings callSettings = null)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::CreateRapidCacheRequest request = new gcscv::CreateRapidCacheRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        RapidCache = new gcscv::RapidCache(),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = storageControlClient.CreateRapidCache(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = storageControlClient.PollOnceCreateRapidCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateRapidCache(string, RapidCache, CallSettings)
    
    
    public virtual Operation<RapidCache, CreateRapidCacheMetadata> CreateRapidCache(string parent, RapidCache rapidCache, CallSettings callSettings = null)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to create. Default values for ingest_on_write, ttl and admission_policy will be applied if not specified in the request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = storageControlClient.CreateRapidCache(parent, rapidCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = storageControlClient.PollOnceCreateRapidCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateRapidCacheAsync(BucketName, RapidCache, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, CreateRapidCacheMetadata>> CreateRapidCacheAsync(BucketName parent, RapidCache rapidCache, CallSettings callSettings = null)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to create. Default values for ingest_on_write, ttl and admission_policy will be applied if not specified in the request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = await storageControlClient.CreateRapidCacheAsync(parent, rapidCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateRapidCacheAsync(BucketName, RapidCache, CancellationToken)
    
    
    public virtual Task<Operation<RapidCache, CreateRapidCacheMetadata>> CreateRapidCacheAsync(BucketName parent, RapidCache rapidCache, CancellationToken cancellationToken)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to create. Default values for ingest_on_write, ttl and admission_policy will be applied if not specified in the request.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = await storageControlClient.CreateRapidCacheAsync(parent, rapidCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateRapidCacheAsync(CreateRapidCacheRequest, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, CreateRapidCacheMetadata>> CreateRapidCacheAsync(CreateRapidCacheRequest request, CallSettings callSettings = null)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::CreateRapidCacheRequest request = new gcscv::CreateRapidCacheRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        RapidCache = new gcscv::RapidCache(),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = await storageControlClient.CreateRapidCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateRapidCacheAsync(CreateRapidCacheRequest, CancellationToken)
    
    
    public virtual Task<Operation<RapidCache, CreateRapidCacheMetadata>> CreateRapidCacheAsync(CreateRapidCacheRequest request, CancellationToken cancellationToken)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::CreateRapidCacheRequest request = new gcscv::CreateRapidCacheRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        RapidCache = new gcscv::RapidCache(),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = await storageControlClient.CreateRapidCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateRapidCacheAsync(string, RapidCache, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, CreateRapidCacheMetadata>> CreateRapidCacheAsync(string parent, RapidCache rapidCache, CallSettings callSettings = null)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to create. Default values for ingest_on_write, ttl and admission_policy will be applied if not specified in the request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = await storageControlClient.CreateRapidCacheAsync(parent, rapidCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### CreateRapidCacheAsync(string, RapidCache, CancellationToken)
    
    
    public virtual Task<Operation<RapidCache, CreateRapidCacheMetadata>> CreateRapidCacheAsync(string parent, RapidCache rapidCache, CancellationToken cancellationToken)

Creates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs. Format: `projects/{project}/buckets/{bucket}`  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to create. Default values for ingest_on_write, ttl and admission_policy will be applied if not specified in the request.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> response = await storageControlClient.CreateRapidCacheAsync(parent, rapidCache);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::CreateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceCreateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolder(DeleteFolderRequest, CallSettings)
    
    
    public virtual void DeleteFolder(DeleteFolderRequest request, CallSettings callSettings = null)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::DeleteFolderRequest request = new gcscv::DeleteFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
    };
    // Make the request
    storageControlClient.DeleteFolder(request);
    

### DeleteFolder(FolderName, CallSettings)
    
    
    public virtual void DeleteFolder(FolderName name, CallSettings callSettings = null)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    storageControlClient.DeleteFolder(name);
    

### DeleteFolder(string, CallSettings)
    
    
    public virtual void DeleteFolder(string name, CallSettings callSettings = null)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    storageControlClient.DeleteFolder(name);
    

### DeleteFolderAsync(DeleteFolderRequest, CallSettings)
    
    
    public virtual Task DeleteFolderAsync(DeleteFolderRequest request, CallSettings callSettings = null)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DeleteFolderRequest request = new gcscv::DeleteFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
    };
    // Make the request
    await storageControlClient.DeleteFolderAsync(request);
    

### DeleteFolderAsync(DeleteFolderRequest, CancellationToken)
    
    
    public virtual Task DeleteFolderAsync(DeleteFolderRequest request, CancellationToken cancellationToken)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DeleteFolderRequest request = new gcscv::DeleteFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
    };
    // Make the request
    await storageControlClient.DeleteFolderAsync(request);
    

### DeleteFolderAsync(FolderName, CallSettings)
    
    
    public virtual Task DeleteFolderAsync(FolderName name, CallSettings callSettings = null)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    await storageControlClient.DeleteFolderAsync(name);
    

### DeleteFolderAsync(FolderName, CancellationToken)
    
    
    public virtual Task DeleteFolderAsync(FolderName name, CancellationToken cancellationToken)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    await storageControlClient.DeleteFolderAsync(name);
    

### DeleteFolderAsync(string, CallSettings)
    
    
    public virtual Task DeleteFolderAsync(string name, CallSettings callSettings = null)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    await storageControlClient.DeleteFolderAsync(name);
    

### DeleteFolderAsync(string, CancellationToken)
    
    
    public virtual Task DeleteFolderAsync(string name, CancellationToken cancellationToken)

Permanently deletes an empty folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    await storageControlClient.DeleteFolderAsync(name);
    

### DeleteFolderRecursive(DeleteFolderRecursiveRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteFolderRecursiveMetadata> DeleteFolderRecursive(DeleteFolderRecursiveRequest request, CallSettings callSettings = null)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::DeleteFolderRecursiveRequest request = new gcscv::DeleteFolderRecursiveRequest
    {
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
    };
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = storageControlClient.DeleteFolderRecursive(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = storageControlClient.PollOnceDeleteFolderRecursive(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolderRecursive(FolderName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteFolderRecursiveMetadata> DeleteFolderRecursive(FolderName name, CallSettings callSettings = null)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder being deleted, however all of its contents will be deleted too. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = storageControlClient.DeleteFolderRecursive(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = storageControlClient.PollOnceDeleteFolderRecursive(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolderRecursive(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteFolderRecursiveMetadata> DeleteFolderRecursive(string name, CallSettings callSettings = null)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder being deleted, however all of its contents will be deleted too. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = storageControlClient.DeleteFolderRecursive(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = storageControlClient.PollOnceDeleteFolderRecursive(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolderRecursiveAsync(DeleteFolderRecursiveRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteFolderRecursiveMetadata>> DeleteFolderRecursiveAsync(DeleteFolderRecursiveRequest request, CallSettings callSettings = null)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DeleteFolderRecursiveRequest request = new gcscv::DeleteFolderRecursiveRequest
    {
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
    };
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = await storageControlClient.DeleteFolderRecursiveAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = await storageControlClient.PollOnceDeleteFolderRecursiveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolderRecursiveAsync(DeleteFolderRecursiveRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteFolderRecursiveMetadata>> DeleteFolderRecursiveAsync(DeleteFolderRecursiveRequest request, CancellationToken cancellationToken)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DeleteFolderRecursiveRequest request = new gcscv::DeleteFolderRecursiveRequest
    {
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
    };
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = await storageControlClient.DeleteFolderRecursiveAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = await storageControlClient.PollOnceDeleteFolderRecursiveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolderRecursiveAsync(FolderName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteFolderRecursiveMetadata>> DeleteFolderRecursiveAsync(FolderName name, CallSettings callSettings = null)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder being deleted, however all of its contents will be deleted too. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = await storageControlClient.DeleteFolderRecursiveAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = await storageControlClient.PollOnceDeleteFolderRecursiveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolderRecursiveAsync(FolderName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteFolderRecursiveMetadata>> DeleteFolderRecursiveAsync(FolderName name, CancellationToken cancellationToken)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder being deleted, however all of its contents will be deleted too. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = await storageControlClient.DeleteFolderRecursiveAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = await storageControlClient.PollOnceDeleteFolderRecursiveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolderRecursiveAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteFolderRecursiveMetadata>> DeleteFolderRecursiveAsync(string name, CallSettings callSettings = null)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder being deleted, however all of its contents will be deleted too. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = await storageControlClient.DeleteFolderRecursiveAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = await storageControlClient.PollOnceDeleteFolderRecursiveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFolderRecursiveAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteFolderRecursiveMetadata>> DeleteFolderRecursiveAsync(string name, CancellationToken cancellationToken)

Deletes a folder recursively. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder being deleted, however all of its contents will be deleted too. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> response = await storageControlClient.DeleteFolderRecursiveAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcscv::DeleteFolderRecursiveMetadata> retrievedResponse = await storageControlClient.PollOnceDeleteFolderRecursiveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteManagedFolder(DeleteManagedFolderRequest, CallSettings)
    
    
    public virtual void DeleteManagedFolder(DeleteManagedFolderRequest request, CallSettings callSettings = null)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::DeleteManagedFolderRequest request = new gcscv::DeleteManagedFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        AllowNonEmpty = false,
        ManagedFolderName = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]"),
    };
    // Make the request
    storageControlClient.DeleteManagedFolder(request);
    

### DeleteManagedFolder(ManagedFolderName, CallSettings)
    
    
    public virtual void DeleteManagedFolder(ManagedFolderName name, CallSettings callSettings = null)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ManagedFolderName name = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]");
    // Make the request
    storageControlClient.DeleteManagedFolder(name);
    

### DeleteManagedFolder(string, CallSettings)
    
    
    public virtual void DeleteManagedFolder(string name, CallSettings callSettings = null)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/managedFolders/[MANAGED_FOLDER]";
    // Make the request
    storageControlClient.DeleteManagedFolder(name);
    

### DeleteManagedFolderAsync(DeleteManagedFolderRequest, CallSettings)
    
    
    public virtual Task DeleteManagedFolderAsync(DeleteManagedFolderRequest request, CallSettings callSettings = null)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DeleteManagedFolderRequest request = new gcscv::DeleteManagedFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        AllowNonEmpty = false,
        ManagedFolderName = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]"),
    };
    // Make the request
    await storageControlClient.DeleteManagedFolderAsync(request);
    

### DeleteManagedFolderAsync(DeleteManagedFolderRequest, CancellationToken)
    
    
    public virtual Task DeleteManagedFolderAsync(DeleteManagedFolderRequest request, CancellationToken cancellationToken)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DeleteManagedFolderRequest request = new gcscv::DeleteManagedFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        AllowNonEmpty = false,
        ManagedFolderName = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]"),
    };
    // Make the request
    await storageControlClient.DeleteManagedFolderAsync(request);
    

### DeleteManagedFolderAsync(ManagedFolderName, CallSettings)
    
    
    public virtual Task DeleteManagedFolderAsync(ManagedFolderName name, CallSettings callSettings = null)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ManagedFolderName name = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]");
    // Make the request
    await storageControlClient.DeleteManagedFolderAsync(name);
    

### DeleteManagedFolderAsync(ManagedFolderName, CancellationToken)
    
    
    public virtual Task DeleteManagedFolderAsync(ManagedFolderName name, CancellationToken cancellationToken)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ManagedFolderName name = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]");
    // Make the request
    await storageControlClient.DeleteManagedFolderAsync(name);
    

### DeleteManagedFolderAsync(string, CallSettings)
    
    
    public virtual Task DeleteManagedFolderAsync(string name, CallSettings callSettings = null)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/managedFolders/[MANAGED_FOLDER]";
    // Make the request
    await storageControlClient.DeleteManagedFolderAsync(name);
    

### DeleteManagedFolderAsync(string, CancellationToken)
    
    
    public virtual Task DeleteManagedFolderAsync(string name, CancellationToken cancellationToken)

Permanently deletes an empty managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/managedFolders/[MANAGED_FOLDER]";
    // Make the request
    await storageControlClient.DeleteManagedFolderAsync(name);
    

### DisableAnywhereCache(AnywhereCacheName, CallSettings)
    
    
    public virtual AnywhereCache DisableAnywhereCache(AnywhereCacheName name, CallSettings callSettings = null)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.DisableAnywhereCache(name);
    

### DisableAnywhereCache(DisableAnywhereCacheRequest, CallSettings)
    
    
    public virtual AnywhereCache DisableAnywhereCache(DisableAnywhereCacheRequest request, CallSettings callSettings = null)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::DisableAnywhereCacheRequest request = new gcscv::DisableAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.DisableAnywhereCache(request);
    

### DisableAnywhereCache(string, CallSettings)
    
    
    public virtual AnywhereCache DisableAnywhereCache(string name, CallSettings callSettings = null)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.DisableAnywhereCache(name);
    

### DisableAnywhereCacheAsync(AnywhereCacheName, CallSettings)
    
    
    public virtual Task<AnywhereCache> DisableAnywhereCacheAsync(AnywhereCacheName name, CallSettings callSettings = null)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.DisableAnywhereCacheAsync(name);
    

### DisableAnywhereCacheAsync(AnywhereCacheName, CancellationToken)
    
    
    public virtual Task<AnywhereCache> DisableAnywhereCacheAsync(AnywhereCacheName name, CancellationToken cancellationToken)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.DisableAnywhereCacheAsync(name);
    

### DisableAnywhereCacheAsync(DisableAnywhereCacheRequest, CallSettings)
    
    
    public virtual Task<AnywhereCache> DisableAnywhereCacheAsync(DisableAnywhereCacheRequest request, CallSettings callSettings = null)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DisableAnywhereCacheRequest request = new gcscv::DisableAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.DisableAnywhereCacheAsync(request);
    

### DisableAnywhereCacheAsync(DisableAnywhereCacheRequest, CancellationToken)
    
    
    public virtual Task<AnywhereCache> DisableAnywhereCacheAsync(DisableAnywhereCacheRequest request, CancellationToken cancellationToken)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DisableAnywhereCacheRequest request = new gcscv::DisableAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.DisableAnywhereCacheAsync(request);
    

### DisableAnywhereCacheAsync(string, CallSettings)
    
    
    public virtual Task<AnywhereCache> DisableAnywhereCacheAsync(string name, CallSettings callSettings = null)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.DisableAnywhereCacheAsync(name);
    

### DisableAnywhereCacheAsync(string, CancellationToken)
    
    
    public virtual Task<AnywhereCache> DisableAnywhereCacheAsync(string name, CancellationToken cancellationToken)

Disables an Anywhere Cache instance. A disabled instance is read-only. The disablement could be revoked by calling ResumeAnywhereCache. The cache instance will be deleted automatically if it remains in the disabled state for at least one hour.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.DisableAnywhereCacheAsync(name);
    

### DisableRapidCache(DisableRapidCacheRequest, CallSettings)
    
    
    public virtual Operation<RapidCache, DisableRapidCacheMetadata> DisableRapidCache(DisableRapidCacheRequest request, CallSettings callSettings = null)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::DisableRapidCacheRequest request = new gcscv::DisableRapidCacheRequest
    {
        RapidCacheName = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]"),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = storageControlClient.DisableRapidCache(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = storageControlClient.PollOnceDisableRapidCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DisableRapidCache(RapidCacheName, CallSettings)
    
    
    public virtual Operation<RapidCache, DisableRapidCacheMetadata> DisableRapidCache(RapidCacheName name, CallSettings callSettings = null)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RapidCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::RapidCacheName name = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]");
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = storageControlClient.DisableRapidCache(name);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = storageControlClient.PollOnceDisableRapidCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DisableRapidCache(string, CallSettings)
    
    
    public virtual Operation<RapidCache, DisableRapidCacheMetadata> DisableRapidCache(string name, CallSettings callSettings = null)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/rapidCaches/[RAPID_CACHE]";
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = storageControlClient.DisableRapidCache(name);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = storageControlClient.PollOnceDisableRapidCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DisableRapidCacheAsync(DisableRapidCacheRequest, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, DisableRapidCacheMetadata>> DisableRapidCacheAsync(DisableRapidCacheRequest request, CallSettings callSettings = null)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DisableRapidCacheRequest request = new gcscv::DisableRapidCacheRequest
    {
        RapidCacheName = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]"),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = await storageControlClient.DisableRapidCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceDisableRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DisableRapidCacheAsync(DisableRapidCacheRequest, CancellationToken)
    
    
    public virtual Task<Operation<RapidCache, DisableRapidCacheMetadata>> DisableRapidCacheAsync(DisableRapidCacheRequest request, CancellationToken cancellationToken)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::DisableRapidCacheRequest request = new gcscv::DisableRapidCacheRequest
    {
        RapidCacheName = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]"),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = await storageControlClient.DisableRapidCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceDisableRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DisableRapidCacheAsync(RapidCacheName, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, DisableRapidCacheMetadata>> DisableRapidCacheAsync(RapidCacheName name, CallSettings callSettings = null)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RapidCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::RapidCacheName name = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]");
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = await storageControlClient.DisableRapidCacheAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceDisableRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DisableRapidCacheAsync(RapidCacheName, CancellationToken)
    
    
    public virtual Task<Operation<RapidCache, DisableRapidCacheMetadata>> DisableRapidCacheAsync(RapidCacheName name, CancellationToken cancellationToken)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RapidCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::RapidCacheName name = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]");
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = await storageControlClient.DisableRapidCacheAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceDisableRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DisableRapidCacheAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, DisableRapidCacheMetadata>> DisableRapidCacheAsync(string name, CallSettings callSettings = null)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/rapidCaches/[RAPID_CACHE]";
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = await storageControlClient.DisableRapidCacheAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceDisableRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### DisableRapidCacheAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<RapidCache, DisableRapidCacheMetadata>> DisableRapidCacheAsync(string name, CancellationToken cancellationToken)

Disables a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/rapidCaches/[RAPID_CACHE]";
    // Make the request
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> response = await storageControlClient.DisableRapidCacheAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::DisableRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceDisableRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### GetAnywhereCache(AnywhereCacheName, CallSettings)
    
    
    public virtual AnywhereCache GetAnywhereCache(AnywhereCacheName name, CallSettings callSettings = null)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.GetAnywhereCache(name);
    

### GetAnywhereCache(GetAnywhereCacheRequest, CallSettings)
    
    
    public virtual AnywhereCache GetAnywhereCache(GetAnywhereCacheRequest request, CallSettings callSettings = null)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetAnywhereCacheRequest request = new gcscv::GetAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.GetAnywhereCache(request);
    

### GetAnywhereCache(string, CallSettings)
    
    
    public virtual AnywhereCache GetAnywhereCache(string name, CallSettings callSettings = null)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.GetAnywhereCache(name);
    

### GetAnywhereCacheAsync(AnywhereCacheName, CallSettings)
    
    
    public virtual Task<AnywhereCache> GetAnywhereCacheAsync(AnywhereCacheName name, CallSettings callSettings = null)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.GetAnywhereCacheAsync(name);
    

### GetAnywhereCacheAsync(AnywhereCacheName, CancellationToken)
    
    
    public virtual Task<AnywhereCache> GetAnywhereCacheAsync(AnywhereCacheName name, CancellationToken cancellationToken)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.GetAnywhereCacheAsync(name);
    

### GetAnywhereCacheAsync(GetAnywhereCacheRequest, CallSettings)
    
    
    public virtual Task<AnywhereCache> GetAnywhereCacheAsync(GetAnywhereCacheRequest request, CallSettings callSettings = null)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetAnywhereCacheRequest request = new gcscv::GetAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.GetAnywhereCacheAsync(request);
    

### GetAnywhereCacheAsync(GetAnywhereCacheRequest, CancellationToken)
    
    
    public virtual Task<AnywhereCache> GetAnywhereCacheAsync(GetAnywhereCacheRequest request, CancellationToken cancellationToken)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetAnywhereCacheRequest request = new gcscv::GetAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.GetAnywhereCacheAsync(request);
    

### GetAnywhereCacheAsync(string, CallSettings)
    
    
    public virtual Task<AnywhereCache> GetAnywhereCacheAsync(string name, CallSettings callSettings = null)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.GetAnywhereCacheAsync(name);
    

### GetAnywhereCacheAsync(string, CancellationToken)
    
    
    public virtual Task<AnywhereCache> GetAnywhereCacheAsync(string name, CancellationToken cancellationToken)

Gets an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.GetAnywhereCacheAsync(name);
    

### GetFolder(FolderName, CallSettings)
    
    
    public virtual Folder GetFolder(FolderName name, CallSettings callSettings = null)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    gcscv::Folder response = storageControlClient.GetFolder(name);
    

### GetFolder(GetFolderRequest, CallSettings)
    
    
    public virtual Folder GetFolder(GetFolderRequest request, CallSettings callSettings = null)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetFolderRequest request = new gcscv::GetFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
    };
    // Make the request
    gcscv::Folder response = storageControlClient.GetFolder(request);
    

### GetFolder(string, CallSettings)
    
    
    public virtual Folder GetFolder(string name, CallSettings callSettings = null)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    gcscv::Folder response = storageControlClient.GetFolder(name);
    

### GetFolderAsync(FolderName, CallSettings)
    
    
    public virtual Task<Folder> GetFolderAsync(FolderName name, CallSettings callSettings = null)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    gcscv::Folder response = await storageControlClient.GetFolderAsync(name);
    

### GetFolderAsync(FolderName, CancellationToken)
    
    
    public virtual Task<Folder> GetFolderAsync(FolderName name, CancellationToken cancellationToken)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    // Make the request
    gcscv::Folder response = await storageControlClient.GetFolderAsync(name);
    

### GetFolderAsync(GetFolderRequest, CallSettings)
    
    
    public virtual Task<Folder> GetFolderAsync(GetFolderRequest request, CallSettings callSettings = null)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetFolderRequest request = new gcscv::GetFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
    };
    // Make the request
    gcscv::Folder response = await storageControlClient.GetFolderAsync(request);
    

### GetFolderAsync(GetFolderRequest, CancellationToken)
    
    
    public virtual Task<Folder> GetFolderAsync(GetFolderRequest request, CancellationToken cancellationToken)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetFolderRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetFolderRequest request = new gcscv::GetFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
    };
    // Make the request
    gcscv::Folder response = await storageControlClient.GetFolderAsync(request);
    

### GetFolderAsync(string, CallSettings)
    
    
    public virtual Task<Folder> GetFolderAsync(string name, CallSettings callSettings = null)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    gcscv::Folder response = await storageControlClient.GetFolderAsync(name);
    

### GetFolderAsync(string, CancellationToken)
    
    
    public virtual Task<Folder> GetFolderAsync(string name, CancellationToken cancellationToken)

Returns metadata for the specified folder. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    // Make the request
    gcscv::Folder response = await storageControlClient.GetFolderAsync(name);
    

### GetFolderIntelligenceConfig(GetFolderIntelligenceConfigRequest, CallSettings)
    
    
    public virtual IntelligenceConfig GetFolderIntelligenceConfig(GetFolderIntelligenceConfigRequest request, CallSettings callSettings = null)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetFolderIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetFolderIntelligenceConfigRequest request = new gcscv::GetFolderIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetFolderIntelligenceConfig(request);
    

### GetFolderIntelligenceConfig(IntelligenceConfigName, CallSettings)
    
    
    public virtual IntelligenceConfig GetFolderIntelligenceConfig(IntelligenceConfigName name, CallSettings callSettings = null)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your folder. Format: `folders/{id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetFolderIntelligenceConfig(name);
    

### GetFolderIntelligenceConfig(string, CallSettings)
    
    
    public virtual IntelligenceConfig GetFolderIntelligenceConfig(string name, CallSettings callSettings = null)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your folder. Format: `folders/{id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetFolderIntelligenceConfig(name);
    

### GetFolderIntelligenceConfigAsync(GetFolderIntelligenceConfigRequest, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetFolderIntelligenceConfigAsync(GetFolderIntelligenceConfigRequest request, CallSettings callSettings = null)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetFolderIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetFolderIntelligenceConfigRequest request = new gcscv::GetFolderIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetFolderIntelligenceConfigAsync(request);
    

### GetFolderIntelligenceConfigAsync(GetFolderIntelligenceConfigRequest, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetFolderIntelligenceConfigAsync(GetFolderIntelligenceConfigRequest request, CancellationToken cancellationToken)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetFolderIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetFolderIntelligenceConfigRequest request = new gcscv::GetFolderIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetFolderIntelligenceConfigAsync(request);
    

### GetFolderIntelligenceConfigAsync(IntelligenceConfigName, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetFolderIntelligenceConfigAsync(IntelligenceConfigName name, CallSettings callSettings = null)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your folder. Format: `folders/{id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetFolderIntelligenceConfigAsync(name);
    

### GetFolderIntelligenceConfigAsync(IntelligenceConfigName, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetFolderIntelligenceConfigAsync(IntelligenceConfigName name, CancellationToken cancellationToken)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your folder. Format: `folders/{id}/locations/global/intelligenceConfig`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetFolderIntelligenceConfigAsync(name);
    

### GetFolderIntelligenceConfigAsync(string, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetFolderIntelligenceConfigAsync(string name, CallSettings callSettings = null)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your folder. Format: `folders/{id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetFolderIntelligenceConfigAsync(name);
    

### GetFolderIntelligenceConfigAsync(string, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetFolderIntelligenceConfigAsync(string name, CancellationToken cancellationToken)

Returns the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your folder. Format: `folders/{id}/locations/global/intelligenceConfig`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetFolderIntelligenceConfigAsync(name);
    

### GetIamPolicy(IResourceName, CallSettings)
    
    
    public virtual Policy GetIamPolicy(IResourceName resource, CallSettings callSettings = null)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = storageControlClient.GetIamPolicy(resource);
    

### GetIamPolicy(GetIamPolicyRequest, CallSettings)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = storageControlClient.GetIamPolicy(request);
    

### GetIamPolicy(string, CallSettings)
    
    
    public virtual Policy GetIamPolicy(string resource, CallSettings callSettings = null)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = storageControlClient.GetIamPolicy(resource);
    

### GetIamPolicyAsync(IResourceName, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(IResourceName resource, CallSettings callSettings = null)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = await storageControlClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(IResourceName, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(IResourceName resource, CancellationToken cancellationToken)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = await storageControlClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(GetIamPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = await storageControlClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(GetIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CancellationToken cancellationToken)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = await storageControlClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(string resource, CallSettings callSettings = null)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = await storageControlClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(string, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(string resource, CancellationToken cancellationToken)

Gets the IAM policy for a specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = await storageControlClient.GetIamPolicyAsync(resource);
    

### GetIntelligenceFinding(GetIntelligenceFindingRequest, CallSettings)
    
    
    public virtual IntelligenceFinding GetIntelligenceFinding(GetIntelligenceFindingRequest request, CallSettings callSettings = null)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIntelligenceFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetIntelligenceFindingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetIntelligenceFindingRequest request = new gcscv::GetIntelligenceFindingRequest
    {
        IntelligenceFindingName = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]"),
    };
    // Make the request
    gcscv::IntelligenceFinding response = storageControlClient.GetIntelligenceFinding(request);
    

### GetIntelligenceFinding(IntelligenceFindingName, CallSettings)
    
    
    public virtual IntelligenceFinding GetIntelligenceFinding(IntelligenceFindingName name, CallSettings callSettings = null)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceFindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingName)`  
Required. The name of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceFindingName name = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]");
    // Make the request
    gcscv::IntelligenceFinding response = storageControlClient.GetIntelligenceFinding(name);
    

### GetIntelligenceFinding(string, CallSettings)
    
    
    public virtual IntelligenceFinding GetIntelligenceFinding(string name, CallSettings callSettings = null)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/intelligenceFindings/[INTELLIGENCE_FINDING]";
    // Make the request
    gcscv::IntelligenceFinding response = storageControlClient.GetIntelligenceFinding(name);
    

### GetIntelligenceFindingAsync(GetIntelligenceFindingRequest, CallSettings)
    
    
    public virtual Task<IntelligenceFinding> GetIntelligenceFindingAsync(GetIntelligenceFindingRequest request, CallSettings callSettings = null)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIntelligenceFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetIntelligenceFindingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetIntelligenceFindingRequest request = new gcscv::GetIntelligenceFindingRequest
    {
        IntelligenceFindingName = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]"),
    };
    // Make the request
    gcscv::IntelligenceFinding response = await storageControlClient.GetIntelligenceFindingAsync(request);
    

### GetIntelligenceFindingAsync(GetIntelligenceFindingRequest, CancellationToken)
    
    
    public virtual Task<IntelligenceFinding> GetIntelligenceFindingAsync(GetIntelligenceFindingRequest request, CancellationToken cancellationToken)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIntelligenceFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetIntelligenceFindingRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetIntelligenceFindingRequest request = new gcscv::GetIntelligenceFindingRequest
    {
        IntelligenceFindingName = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]"),
    };
    // Make the request
    gcscv::IntelligenceFinding response = await storageControlClient.GetIntelligenceFindingAsync(request);
    

### GetIntelligenceFindingAsync(IntelligenceFindingName, CallSettings)
    
    
    public virtual Task<IntelligenceFinding> GetIntelligenceFindingAsync(IntelligenceFindingName name, CallSettings callSettings = null)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceFindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingName)`  
Required. The name of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceFindingName name = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]");
    // Make the request
    gcscv::IntelligenceFinding response = await storageControlClient.GetIntelligenceFindingAsync(name);
    

### GetIntelligenceFindingAsync(IntelligenceFindingName, CancellationToken)
    
    
    public virtual Task<IntelligenceFinding> GetIntelligenceFindingAsync(IntelligenceFindingName name, CancellationToken cancellationToken)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceFindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingName)`  
Required. The name of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceFindingName name = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]");
    // Make the request
    gcscv::IntelligenceFinding response = await storageControlClient.GetIntelligenceFindingAsync(name);
    

### GetIntelligenceFindingAsync(string, CallSettings)
    
    
    public virtual Task<IntelligenceFinding> GetIntelligenceFindingAsync(string name, CallSettings callSettings = null)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/intelligenceFindings/[INTELLIGENCE_FINDING]";
    // Make the request
    gcscv::IntelligenceFinding response = await storageControlClient.GetIntelligenceFindingAsync(name);
    

### GetIntelligenceFindingAsync(string, CancellationToken)
    
    
    public virtual Task<IntelligenceFinding> GetIntelligenceFindingAsync(string name, CancellationToken cancellationToken)

Gets the `IntelligenceFinding` for a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/intelligenceFindings/[INTELLIGENCE_FINDING]";
    // Make the request
    gcscv::IntelligenceFinding response = await storageControlClient.GetIntelligenceFindingAsync(name);
    

### GetIntelligenceFindingRevision(GetIntelligenceFindingRevisionRequest, CallSettings)
    
    
    public virtual IntelligenceFindingRevision GetIntelligenceFindingRevision(GetIntelligenceFindingRevisionRequest request, CallSettings callSettings = null)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIntelligenceFindingRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetIntelligenceFindingRevisionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetIntelligenceFindingRevisionRequest request = new gcscv::GetIntelligenceFindingRevisionRequest
    {
        IntelligenceFindingRevisionName = gcscv::IntelligenceFindingRevisionName.FromProjectLocationIntelligenceFindingRevision("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]", "[REVISION]"),
    };
    // Make the request
    gcscv::IntelligenceFindingRevision response = storageControlClient.GetIntelligenceFindingRevision(request);
    

### GetIntelligenceFindingRevision(IntelligenceFindingRevisionName, CallSettings)
    
    
    public virtual IntelligenceFindingRevision GetIntelligenceFindingRevision(IntelligenceFindingRevisionName name, CallSettings callSettings = null)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceFindingRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevisionName)`  
Required. The name of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceFindingRevisionName name = gcscv::IntelligenceFindingRevisionName.FromProjectLocationIntelligenceFindingRevision("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]", "[REVISION]");
    // Make the request
    gcscv::IntelligenceFindingRevision response = storageControlClient.GetIntelligenceFindingRevision(name);
    

### GetIntelligenceFindingRevision(string, CallSettings)
    
    
    public virtual IntelligenceFindingRevision GetIntelligenceFindingRevision(string name, CallSettings callSettings = null)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/intelligenceFindings/[INTELLIGENCE_FINDING]/revisions/[REVISION]";
    // Make the request
    gcscv::IntelligenceFindingRevision response = storageControlClient.GetIntelligenceFindingRevision(name);
    

### GetIntelligenceFindingRevisionAsync(GetIntelligenceFindingRevisionRequest, CallSettings)
    
    
    public virtual Task<IntelligenceFindingRevision> GetIntelligenceFindingRevisionAsync(GetIntelligenceFindingRevisionRequest request, CallSettings callSettings = null)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIntelligenceFindingRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetIntelligenceFindingRevisionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetIntelligenceFindingRevisionRequest request = new gcscv::GetIntelligenceFindingRevisionRequest
    {
        IntelligenceFindingRevisionName = gcscv::IntelligenceFindingRevisionName.FromProjectLocationIntelligenceFindingRevision("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]", "[REVISION]"),
    };
    // Make the request
    gcscv::IntelligenceFindingRevision response = await storageControlClient.GetIntelligenceFindingRevisionAsync(request);
    

### GetIntelligenceFindingRevisionAsync(GetIntelligenceFindingRevisionRequest, CancellationToken)
    
    
    public virtual Task<IntelligenceFindingRevision> GetIntelligenceFindingRevisionAsync(GetIntelligenceFindingRevisionRequest request, CancellationToken cancellationToken)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIntelligenceFindingRevisionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetIntelligenceFindingRevisionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetIntelligenceFindingRevisionRequest request = new gcscv::GetIntelligenceFindingRevisionRequest
    {
        IntelligenceFindingRevisionName = gcscv::IntelligenceFindingRevisionName.FromProjectLocationIntelligenceFindingRevision("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]", "[REVISION]"),
    };
    // Make the request
    gcscv::IntelligenceFindingRevision response = await storageControlClient.GetIntelligenceFindingRevisionAsync(request);
    

### GetIntelligenceFindingRevisionAsync(IntelligenceFindingRevisionName, CallSettings)
    
    
    public virtual Task<IntelligenceFindingRevision> GetIntelligenceFindingRevisionAsync(IntelligenceFindingRevisionName name, CallSettings callSettings = null)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceFindingRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevisionName)`  
Required. The name of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceFindingRevisionName name = gcscv::IntelligenceFindingRevisionName.FromProjectLocationIntelligenceFindingRevision("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]", "[REVISION]");
    // Make the request
    gcscv::IntelligenceFindingRevision response = await storageControlClient.GetIntelligenceFindingRevisionAsync(name);
    

### GetIntelligenceFindingRevisionAsync(IntelligenceFindingRevisionName, CancellationToken)
    
    
    public virtual Task<IntelligenceFindingRevision> GetIntelligenceFindingRevisionAsync(IntelligenceFindingRevisionName name, CancellationToken cancellationToken)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceFindingRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevisionName)`  
Required. The name of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceFindingRevisionName name = gcscv::IntelligenceFindingRevisionName.FromProjectLocationIntelligenceFindingRevision("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]", "[REVISION]");
    // Make the request
    gcscv::IntelligenceFindingRevision response = await storageControlClient.GetIntelligenceFindingRevisionAsync(name);
    

### GetIntelligenceFindingRevisionAsync(string, CallSettings)
    
    
    public virtual Task<IntelligenceFindingRevision> GetIntelligenceFindingRevisionAsync(string name, CallSettings callSettings = null)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/intelligenceFindings/[INTELLIGENCE_FINDING]/revisions/[REVISION]";
    // Make the request
    gcscv::IntelligenceFindingRevision response = await storageControlClient.GetIntelligenceFindingRevisionAsync(name);
    

### GetIntelligenceFindingRevisionAsync(string, CancellationToken)
    
    
    public virtual Task<IntelligenceFindingRevision> GetIntelligenceFindingRevisionAsync(string name, CancellationToken cancellationToken)

Gets the `IntelligenceFindingRevision` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/intelligenceFindings/[INTELLIGENCE_FINDING]/revisions/[REVISION]";
    // Make the request
    gcscv::IntelligenceFindingRevision response = await storageControlClient.GetIntelligenceFindingRevisionAsync(name);
    

### GetManagedFolder(GetManagedFolderRequest, CallSettings)
    
    
    public virtual ManagedFolder GetManagedFolder(GetManagedFolderRequest request, CallSettings callSettings = null)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetManagedFolderRequest request = new gcscv::GetManagedFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        ManagedFolderName = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]"),
    };
    // Make the request
    gcscv::ManagedFolder response = storageControlClient.GetManagedFolder(request);
    

### GetManagedFolder(ManagedFolderName, CallSettings)
    
    
    public virtual ManagedFolder GetManagedFolder(ManagedFolderName name, CallSettings callSettings = null)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ManagedFolderName name = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]");
    // Make the request
    gcscv::ManagedFolder response = storageControlClient.GetManagedFolder(name);
    

### GetManagedFolder(string, CallSettings)
    
    
    public virtual ManagedFolder GetManagedFolder(string name, CallSettings callSettings = null)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/managedFolders/[MANAGED_FOLDER]";
    // Make the request
    gcscv::ManagedFolder response = storageControlClient.GetManagedFolder(name);
    

### GetManagedFolderAsync(GetManagedFolderRequest, CallSettings)
    
    
    public virtual Task<ManagedFolder> GetManagedFolderAsync(GetManagedFolderRequest request, CallSettings callSettings = null)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetManagedFolderRequest request = new gcscv::GetManagedFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        ManagedFolderName = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]"),
    };
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.GetManagedFolderAsync(request);
    

### GetManagedFolderAsync(GetManagedFolderRequest, CancellationToken)
    
    
    public virtual Task<ManagedFolder> GetManagedFolderAsync(GetManagedFolderRequest request, CancellationToken cancellationToken)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetManagedFolderRequest request = new gcscv::GetManagedFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        ManagedFolderName = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]"),
    };
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.GetManagedFolderAsync(request);
    

### GetManagedFolderAsync(ManagedFolderName, CallSettings)
    
    
    public virtual Task<ManagedFolder> GetManagedFolderAsync(ManagedFolderName name, CallSettings callSettings = null)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ManagedFolderName name = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]");
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.GetManagedFolderAsync(name);
    

### GetManagedFolderAsync(ManagedFolderName, CancellationToken)
    
    
    public virtual Task<ManagedFolder> GetManagedFolderAsync(ManagedFolderName name, CancellationToken cancellationToken)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ManagedFolderName name = gcscv::ManagedFolderName.FromProjectBucketManagedFolder("[PROJECT]", "[BUCKET]", "[MANAGED_FOLDER]");
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.GetManagedFolderAsync(name);
    

### GetManagedFolderAsync(string, CallSettings)
    
    
    public virtual Task<ManagedFolder> GetManagedFolderAsync(string name, CallSettings callSettings = null)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/managedFolders/[MANAGED_FOLDER]";
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.GetManagedFolderAsync(name);
    

### GetManagedFolderAsync(string, CancellationToken)
    
    
    public virtual Task<ManagedFolder> GetManagedFolderAsync(string name, CancellationToken cancellationToken)

Returns metadata for the specified managed folder.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the managed folder. Format: `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/managedFolders/[MANAGED_FOLDER]";
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.GetManagedFolderAsync(name);
    

### GetOrganizationIntelligenceConfig(GetOrganizationIntelligenceConfigRequest, CallSettings)
    
    
    public virtual IntelligenceConfig GetOrganizationIntelligenceConfig(GetOrganizationIntelligenceConfigRequest request, CallSettings callSettings = null)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetOrganizationIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetOrganizationIntelligenceConfigRequest request = new gcscv::GetOrganizationIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetOrganizationIntelligenceConfig(request);
    

### GetOrganizationIntelligenceConfig(IntelligenceConfigName, CallSettings)
    
    
    public virtual IntelligenceConfig GetOrganizationIntelligenceConfig(IntelligenceConfigName name, CallSettings callSettings = null)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your organization. Format: `organizations/{org_id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetOrganizationIntelligenceConfig(name);
    

### GetOrganizationIntelligenceConfig(string, CallSettings)
    
    
    public virtual IntelligenceConfig GetOrganizationIntelligenceConfig(string name, CallSettings callSettings = null)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your organization. Format: `organizations/{org_id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetOrganizationIntelligenceConfig(name);
    

### GetOrganizationIntelligenceConfigAsync(GetOrganizationIntelligenceConfigRequest, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetOrganizationIntelligenceConfigAsync(GetOrganizationIntelligenceConfigRequest request, CallSettings callSettings = null)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetOrganizationIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetOrganizationIntelligenceConfigRequest request = new gcscv::GetOrganizationIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetOrganizationIntelligenceConfigAsync(request);
    

### GetOrganizationIntelligenceConfigAsync(GetOrganizationIntelligenceConfigRequest, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetOrganizationIntelligenceConfigAsync(GetOrganizationIntelligenceConfigRequest request, CancellationToken cancellationToken)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetOrganizationIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetOrganizationIntelligenceConfigRequest request = new gcscv::GetOrganizationIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetOrganizationIntelligenceConfigAsync(request);
    

### GetOrganizationIntelligenceConfigAsync(IntelligenceConfigName, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetOrganizationIntelligenceConfigAsync(IntelligenceConfigName name, CallSettings callSettings = null)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your organization. Format: `organizations/{org_id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetOrganizationIntelligenceConfigAsync(name);
    

### GetOrganizationIntelligenceConfigAsync(IntelligenceConfigName, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetOrganizationIntelligenceConfigAsync(IntelligenceConfigName name, CancellationToken cancellationToken)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your organization. Format: `organizations/{org_id}/locations/global/intelligenceConfig`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetOrganizationIntelligenceConfigAsync(name);
    

### GetOrganizationIntelligenceConfigAsync(string, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetOrganizationIntelligenceConfigAsync(string name, CallSettings callSettings = null)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your organization. Format: `organizations/{org_id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetOrganizationIntelligenceConfigAsync(name);
    

### GetOrganizationIntelligenceConfigAsync(string, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetOrganizationIntelligenceConfigAsync(string name, CancellationToken cancellationToken)

Returns the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your organization. Format: `organizations/{org_id}/locations/global/intelligenceConfig`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetOrganizationIntelligenceConfigAsync(name);
    

### GetProjectIntelligenceConfig(GetProjectIntelligenceConfigRequest, CallSettings)
    
    
    public virtual IntelligenceConfig GetProjectIntelligenceConfig(GetProjectIntelligenceConfigRequest request, CallSettings callSettings = null)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProjectIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetProjectIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetProjectIntelligenceConfigRequest request = new gcscv::GetProjectIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetProjectIntelligenceConfig(request);
    

### GetProjectIntelligenceConfig(IntelligenceConfigName, CallSettings)
    
    
    public virtual IntelligenceConfig GetProjectIntelligenceConfig(IntelligenceConfigName name, CallSettings callSettings = null)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your project. Format: `projects/{id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetProjectIntelligenceConfig(name);
    

### GetProjectIntelligenceConfig(string, CallSettings)
    
    
    public virtual IntelligenceConfig GetProjectIntelligenceConfig(string name, CallSettings callSettings = null)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your project. Format: `projects/{id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.GetProjectIntelligenceConfig(name);
    

### GetProjectIntelligenceConfigAsync(GetProjectIntelligenceConfigRequest, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetProjectIntelligenceConfigAsync(GetProjectIntelligenceConfigRequest request, CallSettings callSettings = null)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProjectIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetProjectIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetProjectIntelligenceConfigRequest request = new gcscv::GetProjectIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetProjectIntelligenceConfigAsync(request);
    

### GetProjectIntelligenceConfigAsync(GetProjectIntelligenceConfigRequest, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetProjectIntelligenceConfigAsync(GetProjectIntelligenceConfigRequest request, CancellationToken cancellationToken)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProjectIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetProjectIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetProjectIntelligenceConfigRequest request = new gcscv::GetProjectIntelligenceConfigRequest
    {
        IntelligenceConfigName = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]"),
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetProjectIntelligenceConfigAsync(request);
    

### GetProjectIntelligenceConfigAsync(IntelligenceConfigName, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetProjectIntelligenceConfigAsync(IntelligenceConfigName name, CallSettings callSettings = null)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your project. Format: `projects/{id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetProjectIntelligenceConfigAsync(name);
    

### GetProjectIntelligenceConfigAsync(IntelligenceConfigName, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetProjectIntelligenceConfigAsync(IntelligenceConfigName name, CancellationToken cancellationToken)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IntelligenceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfigName)`  
Required. The name of the `IntelligenceConfig` resource associated with your project. Format: `projects/{id}/locations/global/intelligenceConfig`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfigName name = gcscv::IntelligenceConfigName.FromFolderLocation("[FOLDER]", "[LOCATION]");
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetProjectIntelligenceConfigAsync(name);
    

### GetProjectIntelligenceConfigAsync(string, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> GetProjectIntelligenceConfigAsync(string name, CallSettings callSettings = null)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your project. Format: `projects/{id}/locations/global/intelligenceConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetProjectIntelligenceConfigAsync(name);
    

### GetProjectIntelligenceConfigAsync(string, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> GetProjectIntelligenceConfigAsync(string name, CancellationToken cancellationToken)

Returns the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `IntelligenceConfig` resource associated with your project. Format: `projects/{id}/locations/global/intelligenceConfig`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "folders/[FOLDER]/locations/[LOCATION]/intelligenceConfig";
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.GetProjectIntelligenceConfigAsync(name);
    

### GetRapidCache(GetRapidCacheRequest, CallSettings)
    
    
    public virtual RapidCache GetRapidCache(GetRapidCacheRequest request, CallSettings callSettings = null)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetRapidCacheRequest request = new gcscv::GetRapidCacheRequest
    {
        RapidCacheName = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]"),
        RequestId = "",
    };
    // Make the request
    gcscv::RapidCache response = storageControlClient.GetRapidCache(request);
    

### GetRapidCache(RapidCacheName, CallSettings)
    
    
    public virtual RapidCache GetRapidCache(RapidCacheName name, CallSettings callSettings = null)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RapidCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::RapidCacheName name = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]");
    // Make the request
    gcscv::RapidCache response = storageControlClient.GetRapidCache(name);
    

### GetRapidCache(string, CallSettings)
    
    
    public virtual RapidCache GetRapidCache(string name, CallSettings callSettings = null)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/rapidCaches/[RAPID_CACHE]";
    // Make the request
    gcscv::RapidCache response = storageControlClient.GetRapidCache(name);
    

### GetRapidCacheAsync(GetRapidCacheRequest, CallSettings)
    
    
    public virtual Task<RapidCache> GetRapidCacheAsync(GetRapidCacheRequest request, CallSettings callSettings = null)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetRapidCacheRequest request = new gcscv::GetRapidCacheRequest
    {
        RapidCacheName = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]"),
        RequestId = "",
    };
    // Make the request
    gcscv::RapidCache response = await storageControlClient.GetRapidCacheAsync(request);
    

### GetRapidCacheAsync(GetRapidCacheRequest, CancellationToken)
    
    
    public virtual Task<RapidCache> GetRapidCacheAsync(GetRapidCacheRequest request, CancellationToken cancellationToken)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetRapidCacheRequest request = new gcscv::GetRapidCacheRequest
    {
        RapidCacheName = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]"),
        RequestId = "",
    };
    // Make the request
    gcscv::RapidCache response = await storageControlClient.GetRapidCacheAsync(request);
    

### GetRapidCacheAsync(RapidCacheName, CallSettings)
    
    
    public virtual Task<RapidCache> GetRapidCacheAsync(RapidCacheName name, CallSettings callSettings = null)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RapidCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::RapidCacheName name = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]");
    // Make the request
    gcscv::RapidCache response = await storageControlClient.GetRapidCacheAsync(name);
    

### GetRapidCacheAsync(RapidCacheName, CancellationToken)
    
    
    public virtual Task<RapidCache> GetRapidCacheAsync(RapidCacheName name, CancellationToken cancellationToken)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RapidCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::RapidCacheName name = gcscv::RapidCacheName.FromProjectBucketRapidCache("[PROJECT]", "[BUCKET]", "[RAPID_CACHE]");
    // Make the request
    gcscv::RapidCache response = await storageControlClient.GetRapidCacheAsync(name);
    

### GetRapidCacheAsync(string, CallSettings)
    
    
    public virtual Task<RapidCache> GetRapidCacheAsync(string name, CallSettings callSettings = null)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/rapidCaches/[RAPID_CACHE]";
    // Make the request
    gcscv::RapidCache response = await storageControlClient.GetRapidCacheAsync(name);
    

### GetRapidCacheAsync(string, CancellationToken)
    
    
    public virtual Task<RapidCache> GetRapidCacheAsync(string name, CancellationToken cancellationToken)

Gets a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/rapidCaches/[RAPID_CACHE]";
    // Make the request
    gcscv::RapidCache response = await storageControlClient.GetRapidCacheAsync(name);
    

### GetStorageLayout(GetStorageLayoutRequest, CallSettings)
    
    
    public virtual StorageLayout GetStorageLayout(GetStorageLayoutRequest request, CallSettings callSettings = null)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStorageLayoutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetStorageLayoutRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::GetStorageLayoutRequest request = new gcscv::GetStorageLayoutRequest
    {
        StorageLayoutName = gcscv::StorageLayoutName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Prefix = "",
    };
    // Make the request
    gcscv::StorageLayout response = storageControlClient.GetStorageLayout(request);
    

### GetStorageLayout(StorageLayoutName, CallSettings)
    
    
    public virtual StorageLayout GetStorageLayout(StorageLayoutName name, CallSettings callSettings = null)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StorageLayoutName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayoutName)`  
Required. The name of the StorageLayout resource. Format: `projects/{project}/buckets/{bucket}/storageLayout`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::StorageLayoutName name = gcscv::StorageLayoutName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    gcscv::StorageLayout response = storageControlClient.GetStorageLayout(name);
    

### GetStorageLayout(string, CallSettings)
    
    
    public virtual StorageLayout GetStorageLayout(string name, CallSettings callSettings = null)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the StorageLayout resource. Format: `projects/{project}/buckets/{bucket}/storageLayout`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/storageLayout";
    // Make the request
    gcscv::StorageLayout response = storageControlClient.GetStorageLayout(name);
    

### GetStorageLayoutAsync(GetStorageLayoutRequest, CallSettings)
    
    
    public virtual Task<StorageLayout> GetStorageLayoutAsync(GetStorageLayoutRequest request, CallSettings callSettings = null)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStorageLayoutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetStorageLayoutRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetStorageLayoutRequest request = new gcscv::GetStorageLayoutRequest
    {
        StorageLayoutName = gcscv::StorageLayoutName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Prefix = "",
    };
    // Make the request
    gcscv::StorageLayout response = await storageControlClient.GetStorageLayoutAsync(request);
    

### GetStorageLayoutAsync(GetStorageLayoutRequest, CancellationToken)
    
    
    public virtual Task<StorageLayout> GetStorageLayoutAsync(GetStorageLayoutRequest request, CancellationToken cancellationToken)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStorageLayoutRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.GetStorageLayoutRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::GetStorageLayoutRequest request = new gcscv::GetStorageLayoutRequest
    {
        StorageLayoutName = gcscv::StorageLayoutName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Prefix = "",
    };
    // Make the request
    gcscv::StorageLayout response = await storageControlClient.GetStorageLayoutAsync(request);
    

### GetStorageLayoutAsync(StorageLayoutName, CallSettings)
    
    
    public virtual Task<StorageLayout> GetStorageLayoutAsync(StorageLayoutName name, CallSettings callSettings = null)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StorageLayoutName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayoutName)`  
Required. The name of the StorageLayout resource. Format: `projects/{project}/buckets/{bucket}/storageLayout`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::StorageLayoutName name = gcscv::StorageLayoutName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    gcscv::StorageLayout response = await storageControlClient.GetStorageLayoutAsync(name);
    

### GetStorageLayoutAsync(StorageLayoutName, CancellationToken)
    
    
    public virtual Task<StorageLayout> GetStorageLayoutAsync(StorageLayoutName name, CancellationToken cancellationToken)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StorageLayoutName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayoutName)`  
Required. The name of the StorageLayout resource. Format: `projects/{project}/buckets/{bucket}/storageLayout`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::StorageLayoutName name = gcscv::StorageLayoutName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    gcscv::StorageLayout response = await storageControlClient.GetStorageLayoutAsync(name);
    

### GetStorageLayoutAsync(string, CallSettings)
    
    
    public virtual Task<StorageLayout> GetStorageLayoutAsync(string name, CallSettings callSettings = null)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the StorageLayout resource. Format: `projects/{project}/buckets/{bucket}/storageLayout`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/storageLayout";
    // Make the request
    gcscv::StorageLayout response = await storageControlClient.GetStorageLayoutAsync(name);
    

### GetStorageLayoutAsync(string, CancellationToken)
    
    
    public virtual Task<StorageLayout> GetStorageLayoutAsync(string name, CancellationToken cancellationToken)

Returns the storage layout configuration for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the StorageLayout resource. Format: `projects/{project}/buckets/{bucket}/storageLayout`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/storageLayout";
    // Make the request
    gcscv::StorageLayout response = await storageControlClient.GetStorageLayoutAsync(name);
    

### ListAnywhereCaches(BucketName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnywhereCachesResponse, AnywhereCache> ListAnywhereCaches(BucketName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Anywhere Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnywhereCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListAnywhereCachesResponse)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A pageable sequence of [AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    PagedEnumerable<gcscv::ListAnywhereCachesResponse, gcscv::AnywhereCache> response = storageControlClient.ListAnywhereCaches(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::AnywhereCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListAnywhereCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::AnywhereCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::AnywhereCache> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::AnywhereCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnywhereCaches(ListAnywhereCachesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnywhereCachesResponse, AnywhereCache> ListAnywhereCaches(ListAnywhereCachesRequest request, CallSettings callSettings = null)

Lists Anywhere Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnywhereCachesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListAnywhereCachesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnywhereCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListAnywhereCachesResponse)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A pageable sequence of [AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ListAnywhereCachesRequest request = new gcscv::ListAnywhereCachesRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
    };
    // Make the request
    PagedEnumerable<gcscv::ListAnywhereCachesResponse, gcscv::AnywhereCache> response = storageControlClient.ListAnywhereCaches(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::AnywhereCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListAnywhereCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::AnywhereCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::AnywhereCache> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::AnywhereCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnywhereCaches(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnywhereCachesResponse, AnywhereCache> ListAnywhereCaches(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Anywhere Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnywhereCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListAnywhereCachesResponse)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A pageable sequence of [AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    // Make the request
    PagedEnumerable<gcscv::ListAnywhereCachesResponse, gcscv::AnywhereCache> response = storageControlClient.ListAnywhereCaches(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::AnywhereCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListAnywhereCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::AnywhereCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::AnywhereCache> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::AnywhereCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnywhereCachesAsync(BucketName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnywhereCachesResponse, AnywhereCache> ListAnywhereCachesAsync(BucketName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Anywhere Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnywhereCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListAnywhereCachesResponse)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A pageable asynchronous sequence of [AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    PagedAsyncEnumerable<gcscv::ListAnywhereCachesResponse, gcscv::AnywhereCache> response = storageControlClient.ListAnywhereCachesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::AnywhereCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListAnywhereCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::AnywhereCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::AnywhereCache> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::AnywhereCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnywhereCachesAsync(ListAnywhereCachesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnywhereCachesResponse, AnywhereCache> ListAnywhereCachesAsync(ListAnywhereCachesRequest request, CallSettings callSettings = null)

Lists Anywhere Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnywhereCachesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListAnywhereCachesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnywhereCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListAnywhereCachesResponse)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A pageable asynchronous sequence of [AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ListAnywhereCachesRequest request = new gcscv::ListAnywhereCachesRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcscv::ListAnywhereCachesResponse, gcscv::AnywhereCache> response = storageControlClient.ListAnywhereCachesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::AnywhereCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListAnywhereCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::AnywhereCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::AnywhereCache> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::AnywhereCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnywhereCachesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnywhereCachesResponse, AnywhereCache> ListAnywhereCachesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Anywhere Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnywhereCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListAnywhereCachesResponse)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A pageable asynchronous sequence of [AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    // Make the request
    PagedAsyncEnumerable<gcscv::ListAnywhereCachesResponse, gcscv::AnywhereCache> response = storageControlClient.ListAnywhereCachesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::AnywhereCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListAnywhereCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::AnywhereCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::AnywhereCache> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::AnywhereCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFolders(BucketName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFoldersResponse, Folder> ListFolders(BucketName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of folders. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket in which to look for folders. The bucket must be a hierarchical namespace enabled bucket.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListFoldersResponse)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A pageable sequence of [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    PagedEnumerable<gcscv::ListFoldersResponse, gcscv::Folder> response = storageControlClient.ListFolders(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::Folder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::Folder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::Folder> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::Folder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFolders(ListFoldersRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFoldersResponse, Folder> ListFolders(ListFoldersRequest request, CallSettings callSettings = null)

Retrieves a list of folders. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFoldersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListFoldersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListFoldersResponse)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A pageable sequence of [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ListFoldersRequest request = new gcscv::ListFoldersRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Prefix = "",
        LexicographicStart = "",
        LexicographicEnd = "",
        Delimiter = "",
        RequestId = "",
    };
    // Make the request
    PagedEnumerable<gcscv::ListFoldersResponse, gcscv::Folder> response = storageControlClient.ListFolders(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::Folder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::Folder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::Folder> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::Folder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFolders(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFoldersResponse, Folder> ListFolders(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of folders. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket in which to look for folders. The bucket must be a hierarchical namespace enabled bucket.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListFoldersResponse)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A pageable sequence of [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    // Make the request
    PagedEnumerable<gcscv::ListFoldersResponse, gcscv::Folder> response = storageControlClient.ListFolders(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::Folder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::Folder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::Folder> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::Folder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFoldersAsync(BucketName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFoldersResponse, Folder> ListFoldersAsync(BucketName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of folders. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket in which to look for folders. The bucket must be a hierarchical namespace enabled bucket.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListFoldersResponse)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A pageable asynchronous sequence of [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    PagedAsyncEnumerable<gcscv::ListFoldersResponse, gcscv::Folder> response = storageControlClient.ListFoldersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::Folder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::Folder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::Folder> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::Folder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFoldersAsync(ListFoldersRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFoldersResponse, Folder> ListFoldersAsync(ListFoldersRequest request, CallSettings callSettings = null)

Retrieves a list of folders. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFoldersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListFoldersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListFoldersResponse)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A pageable asynchronous sequence of [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ListFoldersRequest request = new gcscv::ListFoldersRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Prefix = "",
        LexicographicStart = "",
        LexicographicEnd = "",
        Delimiter = "",
        RequestId = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcscv::ListFoldersResponse, gcscv::Folder> response = storageControlClient.ListFoldersAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::Folder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::Folder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::Folder> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::Folder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFoldersAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFoldersResponse, Folder> ListFoldersAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of folders. This operation is only applicable to a hierarchical namespace enabled bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket in which to look for folders. The bucket must be a hierarchical namespace enabled bucket.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListFoldersResponse)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)` | A pageable asynchronous sequence of [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    // Make the request
    PagedAsyncEnumerable<gcscv::ListFoldersResponse, gcscv::Folder> response = storageControlClient.ListFoldersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::Folder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::Folder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::Folder> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::Folder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingRevisions(IntelligenceFindingName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIntelligenceFindingRevisionsResponse, IntelligenceFindingRevision> ListIntelligenceFindingRevisions(IntelligenceFindingName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all the revisions of an `IntelligenceFinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[IntelligenceFindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingName)`  
Required. The parent of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIntelligenceFindingRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingRevisionsResponse)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A pageable sequence of [IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceFindingName parent = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]");
    // Make the request
    PagedEnumerable<gcscv::ListIntelligenceFindingRevisionsResponse, gcscv::IntelligenceFindingRevision> response = storageControlClient.ListIntelligenceFindingRevisions(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::IntelligenceFindingRevision item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListIntelligenceFindingRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFindingRevision item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFindingRevision> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFindingRevision item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingRevisions(ListIntelligenceFindingRevisionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListIntelligenceFindingRevisionsResponse, IntelligenceFindingRevision> ListIntelligenceFindingRevisions(ListIntelligenceFindingRevisionsRequest request, CallSettings callSettings = null)

Lists all the revisions of an `IntelligenceFinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIntelligenceFindingRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIntelligenceFindingRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingRevisionsResponse)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A pageable sequence of [IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ListIntelligenceFindingRevisionsRequest request = new gcscv::ListIntelligenceFindingRevisionsRequest
    {
        ParentAsIntelligenceFindingName = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]"),
    };
    // Make the request
    PagedEnumerable<gcscv::ListIntelligenceFindingRevisionsResponse, gcscv::IntelligenceFindingRevision> response = storageControlClient.ListIntelligenceFindingRevisions(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::IntelligenceFindingRevision item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListIntelligenceFindingRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFindingRevision item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFindingRevision> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFindingRevision item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingRevisions(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIntelligenceFindingRevisionsResponse, IntelligenceFindingRevision> ListIntelligenceFindingRevisions(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all the revisions of an `IntelligenceFinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIntelligenceFindingRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingRevisionsResponse)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A pageable sequence of [IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/intelligenceFindings/[INTELLIGENCE_FINDING]";
    // Make the request
    PagedEnumerable<gcscv::ListIntelligenceFindingRevisionsResponse, gcscv::IntelligenceFindingRevision> response = storageControlClient.ListIntelligenceFindingRevisions(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::IntelligenceFindingRevision item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListIntelligenceFindingRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFindingRevision item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFindingRevision> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFindingRevision item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingRevisionsAsync(IntelligenceFindingName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIntelligenceFindingRevisionsResponse, IntelligenceFindingRevision> ListIntelligenceFindingRevisionsAsync(IntelligenceFindingName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all the revisions of an `IntelligenceFinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[IntelligenceFindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingName)`  
Required. The parent of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIntelligenceFindingRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingRevisionsResponse)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A pageable asynchronous sequence of [IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceFindingName parent = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]");
    // Make the request
    PagedAsyncEnumerable<gcscv::ListIntelligenceFindingRevisionsResponse, gcscv::IntelligenceFindingRevision> response = storageControlClient.ListIntelligenceFindingRevisionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::IntelligenceFindingRevision item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListIntelligenceFindingRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFindingRevision item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFindingRevision> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFindingRevision item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingRevisionsAsync(ListIntelligenceFindingRevisionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIntelligenceFindingRevisionsResponse, IntelligenceFindingRevision> ListIntelligenceFindingRevisionsAsync(ListIntelligenceFindingRevisionsRequest request, CallSettings callSettings = null)

Lists all the revisions of an `IntelligenceFinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIntelligenceFindingRevisionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIntelligenceFindingRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingRevisionsResponse)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A pageable asynchronous sequence of [IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ListIntelligenceFindingRevisionsRequest request = new gcscv::ListIntelligenceFindingRevisionsRequest
    {
        ParentAsIntelligenceFindingName = gcscv::IntelligenceFindingName.FromProjectLocationIntelligenceFinding("[PROJECT]", "[LOCATION]", "[INTELLIGENCE_FINDING]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcscv::ListIntelligenceFindingRevisionsResponse, gcscv::IntelligenceFindingRevision> response = storageControlClient.ListIntelligenceFindingRevisionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::IntelligenceFindingRevision item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListIntelligenceFindingRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFindingRevision item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFindingRevision> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFindingRevision item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingRevisionsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIntelligenceFindingRevisionsResponse, IntelligenceFindingRevision> ListIntelligenceFindingRevisionsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all the revisions of an `IntelligenceFinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the `IntelligenceFindingRevision` resource.

## Format:

`projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIntelligenceFindingRevisionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingRevisionsResponse)[IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision)` | A pageable asynchronous sequence of [IntelligenceFindingRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFindingRevision) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/intelligenceFindings/[INTELLIGENCE_FINDING]";
    // Make the request
    PagedAsyncEnumerable<gcscv::ListIntelligenceFindingRevisionsResponse, gcscv::IntelligenceFindingRevision> response = storageControlClient.ListIntelligenceFindingRevisionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::IntelligenceFindingRevision item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListIntelligenceFindingRevisionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFindingRevision item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFindingRevision> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFindingRevision item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindings(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIntelligenceFindingsResponse, IntelligenceFinding> ListIntelligenceFindings(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `IntelligenceFinding` resources for the specified the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingsResponse)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A pageable sequence of [IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<gcscv::ListIntelligenceFindingsResponse, gcscv::IntelligenceFinding> response = storageControlClient.ListIntelligenceFindings(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::IntelligenceFinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFinding> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindings(ListIntelligenceFindingsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListIntelligenceFindingsResponse, IntelligenceFinding> ListIntelligenceFindings(ListIntelligenceFindingsRequest request, CallSettings callSettings = null)

Lists the `IntelligenceFinding` resources for the specified the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIntelligenceFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingsResponse)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A pageable sequence of [IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ListIntelligenceFindingsRequest request = new gcscv::ListIntelligenceFindingsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcscv::ListIntelligenceFindingsResponse, gcscv::IntelligenceFinding> response = storageControlClient.ListIntelligenceFindings(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::IntelligenceFinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFinding> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindings(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIntelligenceFindingsResponse, IntelligenceFinding> ListIntelligenceFindings(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `IntelligenceFinding` resources for the specified the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingsResponse)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A pageable sequence of [IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<gcscv::ListIntelligenceFindingsResponse, gcscv::IntelligenceFinding> response = storageControlClient.ListIntelligenceFindings(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::IntelligenceFinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFinding> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIntelligenceFindingsResponse, IntelligenceFinding> ListIntelligenceFindingsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `IntelligenceFinding` resources for the specified the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingsResponse)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A pageable asynchronous sequence of [IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<gcscv::ListIntelligenceFindingsResponse, gcscv::IntelligenceFinding> response = storageControlClient.ListIntelligenceFindingsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::IntelligenceFinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFinding> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingsAsync(ListIntelligenceFindingsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIntelligenceFindingsResponse, IntelligenceFinding> ListIntelligenceFindingsAsync(ListIntelligenceFindingsRequest request, CallSettings callSettings = null)

Lists the `IntelligenceFinding` resources for the specified the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIntelligenceFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingsResponse)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A pageable asynchronous sequence of [IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ListIntelligenceFindingsRequest request = new gcscv::ListIntelligenceFindingsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcscv::ListIntelligenceFindingsResponse, gcscv::IntelligenceFinding> response = storageControlClient.ListIntelligenceFindingsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::IntelligenceFinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFinding> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIntelligenceFindingsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIntelligenceFindingsResponse, IntelligenceFinding> ListIntelligenceFindingsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `IntelligenceFinding` resources for the specified the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the `IntelligenceFinding` resource. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListIntelligenceFindingsResponse)[IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding)` | A pageable asynchronous sequence of [IntelligenceFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceFinding) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<gcscv::ListIntelligenceFindingsResponse, gcscv::IntelligenceFinding> response = storageControlClient.ListIntelligenceFindingsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::IntelligenceFinding item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::IntelligenceFinding item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::IntelligenceFinding> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::IntelligenceFinding item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListManagedFolders(BucketName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListManagedFoldersResponse, ManagedFolder> ListManagedFolders(BucketName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of managed folders for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket this managed folder belongs to.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListManagedFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListManagedFoldersResponse)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A pageable sequence of [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    PagedEnumerable<gcscv::ListManagedFoldersResponse, gcscv::ManagedFolder> response = storageControlClient.ListManagedFolders(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::ManagedFolder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListManagedFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::ManagedFolder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::ManagedFolder> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::ManagedFolder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListManagedFolders(ListManagedFoldersRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListManagedFoldersResponse, ManagedFolder> ListManagedFolders(ListManagedFoldersRequest request, CallSettings callSettings = null)

Retrieves a list of managed folders for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListManagedFoldersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListManagedFoldersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListManagedFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListManagedFoldersResponse)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A pageable sequence of [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ListManagedFoldersRequest request = new gcscv::ListManagedFoldersRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Prefix = "",
    };
    // Make the request
    PagedEnumerable<gcscv::ListManagedFoldersResponse, gcscv::ManagedFolder> response = storageControlClient.ListManagedFolders(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::ManagedFolder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListManagedFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::ManagedFolder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::ManagedFolder> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::ManagedFolder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListManagedFolders(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListManagedFoldersResponse, ManagedFolder> ListManagedFolders(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of managed folders for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket this managed folder belongs to.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListManagedFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListManagedFoldersResponse)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A pageable sequence of [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    // Make the request
    PagedEnumerable<gcscv::ListManagedFoldersResponse, gcscv::ManagedFolder> response = storageControlClient.ListManagedFolders(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::ManagedFolder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListManagedFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::ManagedFolder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::ManagedFolder> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::ManagedFolder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListManagedFoldersAsync(BucketName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListManagedFoldersResponse, ManagedFolder> ListManagedFoldersAsync(BucketName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of managed folders for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. Name of the bucket this managed folder belongs to.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListManagedFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListManagedFoldersResponse)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A pageable asynchronous sequence of [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    PagedAsyncEnumerable<gcscv::ListManagedFoldersResponse, gcscv::ManagedFolder> response = storageControlClient.ListManagedFoldersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::ManagedFolder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListManagedFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::ManagedFolder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::ManagedFolder> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::ManagedFolder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListManagedFoldersAsync(ListManagedFoldersRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListManagedFoldersResponse, ManagedFolder> ListManagedFoldersAsync(ListManagedFoldersRequest request, CallSettings callSettings = null)

Retrieves a list of managed folders for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListManagedFoldersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListManagedFoldersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListManagedFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListManagedFoldersResponse)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A pageable asynchronous sequence of [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ListManagedFoldersRequest request = new gcscv::ListManagedFoldersRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        Prefix = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcscv::ListManagedFoldersResponse, gcscv::ManagedFolder> response = storageControlClient.ListManagedFoldersAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::ManagedFolder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListManagedFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::ManagedFolder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::ManagedFolder> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::ManagedFolder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListManagedFoldersAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListManagedFoldersResponse, ManagedFolder> ListManagedFoldersAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of managed folders for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the bucket this managed folder belongs to.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListManagedFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListManagedFoldersResponse)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A pageable asynchronous sequence of [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    // Make the request
    PagedAsyncEnumerable<gcscv::ListManagedFoldersResponse, gcscv::ManagedFolder> response = storageControlClient.ListManagedFoldersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::ManagedFolder item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListManagedFoldersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::ManagedFolder item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::ManagedFolder> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::ManagedFolder item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRapidCaches(BucketName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRapidCachesResponse, RapidCache> ListRapidCaches(BucketName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Rapid Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRapidCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListRapidCachesResponse)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A pageable sequence of [RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    PagedEnumerable<gcscv::ListRapidCachesResponse, gcscv::RapidCache> response = storageControlClient.ListRapidCaches(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::RapidCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListRapidCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::RapidCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::RapidCache> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::RapidCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRapidCaches(ListRapidCachesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListRapidCachesResponse, RapidCache> ListRapidCaches(ListRapidCachesRequest request, CallSettings callSettings = null)

Lists Rapid Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRapidCachesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListRapidCachesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRapidCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListRapidCachesResponse)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A pageable sequence of [RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ListRapidCachesRequest request = new gcscv::ListRapidCachesRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        RequestId = "",
    };
    // Make the request
    PagedEnumerable<gcscv::ListRapidCachesResponse, gcscv::RapidCache> response = storageControlClient.ListRapidCaches(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::RapidCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListRapidCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::RapidCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::RapidCache> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::RapidCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRapidCaches(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRapidCachesResponse, RapidCache> ListRapidCaches(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Rapid Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRapidCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListRapidCachesResponse)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A pageable sequence of [RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    // Make the request
    PagedEnumerable<gcscv::ListRapidCachesResponse, gcscv::RapidCache> response = storageControlClient.ListRapidCaches(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::RapidCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::ListRapidCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::RapidCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::RapidCache> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::RapidCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRapidCachesAsync(BucketName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRapidCachesResponse, RapidCache> ListRapidCachesAsync(BucketName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Rapid Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName)`  
Required. The bucket to which this cache belongs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRapidCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListRapidCachesResponse)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A pageable asynchronous sequence of [RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::BucketName parent = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]");
    // Make the request
    PagedAsyncEnumerable<gcscv::ListRapidCachesResponse, gcscv::RapidCache> response = storageControlClient.ListRapidCachesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::RapidCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListRapidCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::RapidCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::RapidCache> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::RapidCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRapidCachesAsync(ListRapidCachesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRapidCachesResponse, RapidCache> ListRapidCachesAsync(ListRapidCachesRequest request, CallSettings callSettings = null)

Lists Rapid Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRapidCachesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListRapidCachesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRapidCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListRapidCachesResponse)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A pageable asynchronous sequence of [RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ListRapidCachesRequest request = new gcscv::ListRapidCachesRequest
    {
        ParentAsBucketName = gcscv::BucketName.FromProjectBucket("[PROJECT]", "[BUCKET]"),
        RequestId = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcscv::ListRapidCachesResponse, gcscv::RapidCache> response = storageControlClient.ListRapidCachesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::RapidCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListRapidCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::RapidCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::RapidCache> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::RapidCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRapidCachesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRapidCachesResponse, RapidCache> ListRapidCachesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Rapid Cache instances for a given bucket.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The bucket to which this cache belongs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRapidCachesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ListRapidCachesResponse)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)` | A pageable asynchronous sequence of [RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/buckets/[BUCKET]";
    // Make the request
    PagedAsyncEnumerable<gcscv::ListRapidCachesResponse, gcscv::RapidCache> response = storageControlClient.ListRapidCachesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::RapidCache item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::ListRapidCachesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::RapidCache item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::RapidCache> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::RapidCache item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PauseAnywhereCache(AnywhereCacheName, CallSettings)
    
    
    public virtual AnywhereCache PauseAnywhereCache(AnywhereCacheName name, CallSettings callSettings = null)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.PauseAnywhereCache(name);
    

### PauseAnywhereCache(PauseAnywhereCacheRequest, CallSettings)
    
    
    public virtual AnywhereCache PauseAnywhereCache(PauseAnywhereCacheRequest request, CallSettings callSettings = null)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.PauseAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::PauseAnywhereCacheRequest request = new gcscv::PauseAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.PauseAnywhereCache(request);
    

### PauseAnywhereCache(string, CallSettings)
    
    
    public virtual AnywhereCache PauseAnywhereCache(string name, CallSettings callSettings = null)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.PauseAnywhereCache(name);
    

### PauseAnywhereCacheAsync(AnywhereCacheName, CallSettings)
    
    
    public virtual Task<AnywhereCache> PauseAnywhereCacheAsync(AnywhereCacheName name, CallSettings callSettings = null)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.PauseAnywhereCacheAsync(name);
    

### PauseAnywhereCacheAsync(AnywhereCacheName, CancellationToken)
    
    
    public virtual Task<AnywhereCache> PauseAnywhereCacheAsync(AnywhereCacheName name, CancellationToken cancellationToken)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.PauseAnywhereCacheAsync(name);
    

### PauseAnywhereCacheAsync(PauseAnywhereCacheRequest, CallSettings)
    
    
    public virtual Task<AnywhereCache> PauseAnywhereCacheAsync(PauseAnywhereCacheRequest request, CallSettings callSettings = null)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.PauseAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::PauseAnywhereCacheRequest request = new gcscv::PauseAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.PauseAnywhereCacheAsync(request);
    

### PauseAnywhereCacheAsync(PauseAnywhereCacheRequest, CancellationToken)
    
    
    public virtual Task<AnywhereCache> PauseAnywhereCacheAsync(PauseAnywhereCacheRequest request, CancellationToken cancellationToken)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.PauseAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::PauseAnywhereCacheRequest request = new gcscv::PauseAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.PauseAnywhereCacheAsync(request);
    

### PauseAnywhereCacheAsync(string, CallSettings)
    
    
    public virtual Task<AnywhereCache> PauseAnywhereCacheAsync(string name, CallSettings callSettings = null)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.PauseAnywhereCacheAsync(name);
    

### PauseAnywhereCacheAsync(string, CancellationToken)
    
    
    public virtual Task<AnywhereCache> PauseAnywhereCacheAsync(string name, CancellationToken cancellationToken)

Pauses an Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.PauseAnywhereCacheAsync(name);
    

### PollOnceCreateAnywhereCache(string, CallSettings)
    
    
    public virtual Operation<AnywhereCache, CreateAnywhereCacheMetadata> PollOnceCreateAnywhereCache(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateAnywhereCache` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | The result of polling the operation.  
  
### PollOnceCreateAnywhereCacheAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AnywhereCache, CreateAnywhereCacheMetadata>> PollOnceCreateAnywhereCacheAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateAnywhereCache`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateAnywhereCacheMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateRapidCache(string, CallSettings)
    
    
    public virtual Operation<RapidCache, CreateRapidCacheMetadata> PollOnceCreateRapidCache(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateRapidCache`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | The result of polling the operation.  
  
### PollOnceCreateRapidCacheAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, CreateRapidCacheMetadata>> PollOnceCreateRapidCacheAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateRapidCache`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[CreateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateRapidCacheMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFolderRecursive(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteFolderRecursiveMetadata> PollOnceDeleteFolderRecursive(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFolderRecursive` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFolderRecursiveAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteFolderRecursiveMetadata>> PollOnceDeleteFolderRecursiveAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFolderRecursive`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DeleteFolderRecursiveMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDisableRapidCache(string, CallSettings)
    
    
    public virtual Operation<RapidCache, DisableRapidCacheMetadata> PollOnceDisableRapidCache(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DisableRapidCache` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | The result of polling the operation.  
  
### PollOnceDisableRapidCacheAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, DisableRapidCacheMetadata>> PollOnceDisableRapidCacheAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DisableRapidCache`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[DisableRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.DisableRapidCacheMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRenameFolder(string, CallSettings)
    
    
    public virtual Operation<Folder, RenameFolderMetadata> PollOnceRenameFolder(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RenameFolder`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | The result of polling the operation.  
  
### PollOnceRenameFolderAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Folder, RenameFolderMetadata>> PollOnceRenameFolderAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RenameFolder`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateAnywhereCache(string, CallSettings)
    
    
    public virtual Operation<AnywhereCache, UpdateAnywhereCacheMetadata> PollOnceUpdateAnywhereCache(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateAnywhereCache` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateAnywhereCacheAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AnywhereCache, UpdateAnywhereCacheMetadata>> PollOnceUpdateAnywhereCacheAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateAnywhereCache`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateRapidCache(string, CallSettings)
    
    
    public virtual Operation<RapidCache, UpdateRapidCacheMetadata> PollOnceUpdateRapidCache(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateRapidCache`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[UpdateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateRapidCacheAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, UpdateRapidCacheMetadata>> PollOnceUpdateRapidCacheAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateRapidCache`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[UpdateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheMetadata)` | A task representing the result of polling the operation.  
  
### RenameFolder(FolderName, string, CallSettings)
    
    
    public virtual Operation<Folder, RenameFolderMetadata> RenameFolder(FolderName name, string destinationFolderId, CallSettings callSettings = null)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the source folder being renamed. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`destinationFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The destination folder ID, e.g. `foo/bar/`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    string destinationFolderId = "";
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = storageControlClient.RenameFolder(name, destinationFolderId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = storageControlClient.PollOnceRenameFolder(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### RenameFolder(RenameFolderRequest, CallSettings)
    
    
    public virtual Operation<Folder, RenameFolderMetadata> RenameFolder(RenameFolderRequest request, CallSettings callSettings = null)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RenameFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::RenameFolderRequest request = new gcscv::RenameFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
        DestinationFolderId = "",
    };
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = storageControlClient.RenameFolder(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = storageControlClient.PollOnceRenameFolder(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### RenameFolder(string, string, CallSettings)
    
    
    public virtual Operation<Folder, RenameFolderMetadata> RenameFolder(string name, string destinationFolderId, CallSettings callSettings = null)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the source folder being renamed. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`destinationFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The destination folder ID, e.g. `foo/bar/`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    string destinationFolderId = "";
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = storageControlClient.RenameFolder(name, destinationFolderId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = storageControlClient.PollOnceRenameFolder(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### RenameFolderAsync(FolderName, string, CallSettings)
    
    
    public virtual Task<Operation<Folder, RenameFolderMetadata>> RenameFolderAsync(FolderName name, string destinationFolderId, CallSettings callSettings = null)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the source folder being renamed. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`destinationFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The destination folder ID, e.g. `foo/bar/`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    string destinationFolderId = "";
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = await storageControlClient.RenameFolderAsync(name, destinationFolderId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = await storageControlClient.PollOnceRenameFolderAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### RenameFolderAsync(FolderName, string, CancellationToken)
    
    
    public virtual Task<Operation<Folder, RenameFolderMetadata>> RenameFolderAsync(FolderName name, string destinationFolderId, CancellationToken cancellationToken)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName)`  
Required. Name of the source folder being renamed. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`destinationFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The destination folder ID, e.g. `foo/bar/`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::FolderName name = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]");
    string destinationFolderId = "";
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = await storageControlClient.RenameFolderAsync(name, destinationFolderId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = await storageControlClient.PollOnceRenameFolderAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### RenameFolderAsync(RenameFolderRequest, CallSettings)
    
    
    public virtual Task<Operation<Folder, RenameFolderMetadata>> RenameFolderAsync(RenameFolderRequest request, CallSettings callSettings = null)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RenameFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::RenameFolderRequest request = new gcscv::RenameFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
        DestinationFolderId = "",
    };
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = await storageControlClient.RenameFolderAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = await storageControlClient.PollOnceRenameFolderAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### RenameFolderAsync(RenameFolderRequest, CancellationToken)
    
    
    public virtual Task<Operation<Folder, RenameFolderMetadata>> RenameFolderAsync(RenameFolderRequest request, CancellationToken cancellationToken)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RenameFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::RenameFolderRequest request = new gcscv::RenameFolderRequest
    {
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        FolderName = gcscv::FolderName.FromProjectBucketFolder("[PROJECT]", "[BUCKET]", "[FOLDER]"),
        DestinationFolderId = "",
    };
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = await storageControlClient.RenameFolderAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = await storageControlClient.PollOnceRenameFolderAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### RenameFolderAsync(string, string, CallSettings)
    
    
    public virtual Task<Operation<Folder, RenameFolderMetadata>> RenameFolderAsync(string name, string destinationFolderId, CallSettings callSettings = null)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the source folder being renamed. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`destinationFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The destination folder ID, e.g. `foo/bar/`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    string destinationFolderId = "";
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = await storageControlClient.RenameFolderAsync(name, destinationFolderId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = await storageControlClient.PollOnceRenameFolderAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### RenameFolderAsync(string, string, CancellationToken)
    
    
    public virtual Task<Operation<Folder, RenameFolderMetadata>> RenameFolderAsync(string name, string destinationFolderId, CancellationToken cancellationToken)

Renames a source folder to a destination folder. This operation is only applicable to a hierarchical namespace enabled bucket. During a rename, the source and destination folders are locked until the long running operation completes.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the source folder being renamed. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`  
`destinationFolderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The destination folder ID, e.g. `foo/bar/`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder)[RenameFolderMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RenameFolderMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/folders/[FOLDER]";
    string destinationFolderId = "";
    // Make the request
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> response = await storageControlClient.RenameFolderAsync(name, destinationFolderId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::Folder result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::Folder, gcscv::RenameFolderMetadata> retrievedResponse = await storageControlClient.PollOnceRenameFolderAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::Folder retrievedResult = retrievedResponse.Result;
    }
    

### ResumeAnywhereCache(AnywhereCacheName, CallSettings)
    
    
    public virtual AnywhereCache ResumeAnywhereCache(AnywhereCacheName name, CallSettings callSettings = null)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.ResumeAnywhereCache(name);
    

### ResumeAnywhereCache(ResumeAnywhereCacheRequest, CallSettings)
    
    
    public virtual AnywhereCache ResumeAnywhereCache(ResumeAnywhereCacheRequest request, CallSettings callSettings = null)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ResumeAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ResumeAnywhereCacheRequest request = new gcscv::ResumeAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.ResumeAnywhereCache(request);
    

### ResumeAnywhereCache(string, CallSettings)
    
    
    public virtual AnywhereCache ResumeAnywhereCache(string name, CallSettings callSettings = null)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = storageControlClient.ResumeAnywhereCache(name);
    

### ResumeAnywhereCacheAsync(AnywhereCacheName, CallSettings)
    
    
    public virtual Task<AnywhereCache> ResumeAnywhereCacheAsync(AnywhereCacheName name, CallSettings callSettings = null)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.ResumeAnywhereCacheAsync(name);
    

### ResumeAnywhereCacheAsync(AnywhereCacheName, CancellationToken)
    
    
    public virtual Task<AnywhereCache> ResumeAnywhereCacheAsync(AnywhereCacheName name, CancellationToken cancellationToken)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnywhereCacheName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCacheName)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCacheName name = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]");
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.ResumeAnywhereCacheAsync(name);
    

### ResumeAnywhereCacheAsync(ResumeAnywhereCacheRequest, CallSettings)
    
    
    public virtual Task<AnywhereCache> ResumeAnywhereCacheAsync(ResumeAnywhereCacheRequest request, CallSettings callSettings = null)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ResumeAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ResumeAnywhereCacheRequest request = new gcscv::ResumeAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.ResumeAnywhereCacheAsync(request);
    

### ResumeAnywhereCacheAsync(ResumeAnywhereCacheRequest, CancellationToken)
    
    
    public virtual Task<AnywhereCache> ResumeAnywhereCacheAsync(ResumeAnywhereCacheRequest request, CancellationToken cancellationToken)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ResumeAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ResumeAnywhereCacheRequest request = new gcscv::ResumeAnywhereCacheRequest
    {
        AnywhereCacheName = gcscv::AnywhereCacheName.FromProjectBucketAnywhereCache("[PROJECT]", "[BUCKET]", "[ANYWHERE_CACHE]"),
    };
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.ResumeAnywhereCacheAsync(request);
    

### ResumeAnywhereCacheAsync(string, CallSettings)
    
    
    public virtual Task<AnywhereCache> ResumeAnywhereCacheAsync(string name, CallSettings callSettings = null)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.ResumeAnywhereCacheAsync(name);
    

### ResumeAnywhereCacheAsync(string, CancellationToken)
    
    
    public virtual Task<AnywhereCache> ResumeAnywhereCacheAsync(string name, CancellationToken cancellationToken)

Resumes a disabled or paused Anywhere Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name field in the request should be: `projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/anywhereCaches/[ANYWHERE_CACHE]";
    // Make the request
    gcscv::AnywhereCache response = await storageControlClient.ResumeAnywhereCacheAsync(name);
    

### SetIamPolicy(IResourceName, Policy, CallSettings)
    
    
    public virtual Policy SetIamPolicy(IResourceName resource, Policy policy, CallSettings callSettings = null)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = storageControlClient.SetIamPolicy(resource, policy);
    

### SetIamPolicy(SetIamPolicyRequest, CallSettings)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRequest request, CallSettings callSettings = null)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = storageControlClient.SetIamPolicy(request);
    

### SetIamPolicy(string, Policy, CallSettings)
    
    
    public virtual Policy SetIamPolicy(string resource, Policy policy, CallSettings callSettings = null)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = storageControlClient.SetIamPolicy(resource, policy);
    

### SetIamPolicyAsync(IResourceName, Policy, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(IResourceName resource, Policy policy, CallSettings callSettings = null)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = await storageControlClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(IResourceName, Policy, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(IResourceName resource, Policy policy, CancellationToken cancellationToken)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = await storageControlClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(SetIamPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CallSettings callSettings = null)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = await storageControlClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(SetIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CancellationToken cancellationToken)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = await storageControlClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(string, Policy, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(string resource, Policy policy, CallSettings callSettings = null)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = await storageControlClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(string, Policy, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(string resource, Policy policy, CancellationToken cancellationToken)

Updates an IAM policy for the specified bucket. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = await storageControlClient.SetIamPolicyAsync(resource, policy);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient#Google_Cloud_Storage_Control_V2_StorageControlClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient#Google_Cloud_Storage_Control_V2_StorageControlClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient#Google_Cloud_Storage_Control_V2_StorageControlClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient#Google_Cloud_Storage_Control_V2_StorageControlClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### SummarizeIntelligenceFindings(SummarizeIntelligenceFindingsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SummarizeIntelligenceFindingsResponse, FindingSummary> SummarizeIntelligenceFindings(SummarizeIntelligenceFindingsRequest request, CallSettings callSettings = null)

Summarizes the intelligence findings for the specified scope (organization, folder or project).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SummarizeIntelligenceFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.SummarizeIntelligenceFindingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SummarizeIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.SummarizeIntelligenceFindingsResponse)[FindingSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FindingSummary)` | A pageable sequence of [FindingSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FindingSummary) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::SummarizeIntelligenceFindingsRequest request = new gcscv::SummarizeIntelligenceFindingsRequest
    {
        Parent = "",
        ResourceScope = gcscv::SummarizeIntelligenceFindingsRequest.Types.ResourceScope.Unspecified,
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcscv::SummarizeIntelligenceFindingsResponse, gcscv::FindingSummary> response = storageControlClient.SummarizeIntelligenceFindings(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::FindingSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::SummarizeIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::FindingSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::FindingSummary> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::FindingSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SummarizeIntelligenceFindings(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SummarizeIntelligenceFindingsResponse, FindingSummary> SummarizeIntelligenceFindings(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Summarizes the intelligence findings for the specified scope (organization, folder or project).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The scope to summarize the findings for. Format:

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SummarizeIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.SummarizeIntelligenceFindingsResponse)[FindingSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FindingSummary)` | A pageable sequence of [FindingSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FindingSummary) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<gcscv::SummarizeIntelligenceFindingsResponse, gcscv::FindingSummary> response = storageControlClient.SummarizeIntelligenceFindings(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcscv::FindingSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcscv::SummarizeIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::FindingSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::FindingSummary> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::FindingSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SummarizeIntelligenceFindingsAsync(SummarizeIntelligenceFindingsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SummarizeIntelligenceFindingsResponse, FindingSummary> SummarizeIntelligenceFindingsAsync(SummarizeIntelligenceFindingsRequest request, CallSettings callSettings = null)

Summarizes the intelligence findings for the specified scope (organization, folder or project).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SummarizeIntelligenceFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.SummarizeIntelligenceFindingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SummarizeIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.SummarizeIntelligenceFindingsResponse)[FindingSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FindingSummary)` | A pageable asynchronous sequence of [FindingSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FindingSummary) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::SummarizeIntelligenceFindingsRequest request = new gcscv::SummarizeIntelligenceFindingsRequest
    {
        Parent = "",
        ResourceScope = gcscv::SummarizeIntelligenceFindingsRequest.Types.ResourceScope.Unspecified,
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcscv::SummarizeIntelligenceFindingsResponse, gcscv::FindingSummary> response = storageControlClient.SummarizeIntelligenceFindingsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::FindingSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::SummarizeIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::FindingSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::FindingSummary> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::FindingSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SummarizeIntelligenceFindingsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SummarizeIntelligenceFindingsResponse, FindingSummary> SummarizeIntelligenceFindingsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Summarizes the intelligence findings for the specified scope (organization, folder or project).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The scope to summarize the findings for. Format:

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SummarizeIntelligenceFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.SummarizeIntelligenceFindingsResponse)[FindingSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FindingSummary)` | A pageable asynchronous sequence of [FindingSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FindingSummary) resources.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<gcscv::SummarizeIntelligenceFindingsResponse, gcscv::FindingSummary> response = storageControlClient.SummarizeIntelligenceFindingsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcscv::FindingSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcscv::SummarizeIntelligenceFindingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcscv::FindingSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcscv::FindingSummary> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcscv::FindingSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### TestIamPermissions(IResourceName, IEnumerable<string>, CallSettings)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(IResourceName resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = storageControlClient.TestIamPermissions(resource, permissions);
    

### TestIamPermissions(TestIamPermissionsRequest, CallSettings)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(TestIamPermissionsRequest request, CallSettings callSettings = null)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = storageControlClient.TestIamPermissions(request);
    

### TestIamPermissions(string, IEnumerable<string>, CallSettings)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(string resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = storageControlClient.TestIamPermissions(resource, permissions);
    

### TestIamPermissionsAsync(IResourceName, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(IResourceName resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = await storageControlClient.TestIamPermissionsAsync(resource, permissions);
    

### TestIamPermissionsAsync(IResourceName, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(IResourceName resource, IEnumerable<string> permissions, CancellationToken cancellationToken)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = await storageControlClient.TestIamPermissionsAsync(resource, permissions);
    

### TestIamPermissionsAsync(TestIamPermissionsRequest, CallSettings)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CallSettings callSettings = null)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = await storageControlClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(TestIamPermissionsRequest, CancellationToken)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CancellationToken cancellationToken)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

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
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = await storageControlClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(string, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(string resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = await storageControlClient.TestIamPermissionsAsync(resource, permissions);
    

### TestIamPermissionsAsync(string, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(string resource, IEnumerable<string> permissions, CancellationToken cancellationToken)

Tests a set of permissions on the given bucket, object, or managed folder to see which, if any, are held by the caller. The `resource` field in the request should be `projects/_/buckets/{bucket}` for a bucket, `projects/_/buckets/{bucket}/objects/{object}` for an object, or `projects/_/buckets/{bucket}/managedFolders/{managedFolder}` for a managed folder.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = await storageControlClient.TestIamPermissionsAsync(resource, permissions);
    

### UpdateAnywhereCache(AnywhereCache, FieldMask, CallSettings)
    
    
    public virtual Operation<AnywhereCache, UpdateAnywhereCacheMetadata> UpdateAnywhereCache(AnywhereCache anywhereCache, FieldMask updateMask, CallSettings callSettings = null)

Updates an Anywhere Cache instance. Mutable fields include `ttl` and `admission_policy`.

**Parameters**  
---  
**Name** | **Description**  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. The Anywhere Cache instance to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. List of fields to be updated. Mutable fields of AnywhereCache include `ttl` and `admission_policy`. To specify ALL fields, specify a single field with the value `*`. Note: We recommend against doing this. If a new field is introduced at a later time, an older client updating with the `*` may accidentally reset the new field's value. Not specifying any fields is an error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> response = storageControlClient.UpdateAnywhereCache(anywhereCache, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> retrievedResponse = storageControlClient.PollOnceUpdateAnywhereCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateAnywhereCache(UpdateAnywhereCacheRequest, CallSettings)
    
    
    public virtual Operation<AnywhereCache, UpdateAnywhereCacheMetadata> UpdateAnywhereCache(UpdateAnywhereCacheRequest request, CallSettings callSettings = null)

Updates an Anywhere Cache instance. Mutable fields include `ttl` and `admission_policy`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::UpdateAnywhereCacheRequest request = new gcscv::UpdateAnywhereCacheRequest
    {
        AnywhereCache = new gcscv::AnywhereCache(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> response = storageControlClient.UpdateAnywhereCache(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> retrievedResponse = storageControlClient.PollOnceUpdateAnywhereCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateAnywhereCacheAsync(AnywhereCache, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<AnywhereCache, UpdateAnywhereCacheMetadata>> UpdateAnywhereCacheAsync(AnywhereCache anywhereCache, FieldMask updateMask, CallSettings callSettings = null)

Updates an Anywhere Cache instance. Mutable fields include `ttl` and `admission_policy`.

**Parameters**  
---  
**Name** | **Description**  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. The Anywhere Cache instance to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. List of fields to be updated. Mutable fields of AnywhereCache include `ttl` and `admission_policy`. To specify ALL fields, specify a single field with the value `*`. Note: We recommend against doing this. If a new field is introduced at a later time, an older client updating with the `*` may accidentally reset the new field's value. Not specifying any fields is an error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> response = await storageControlClient.UpdateAnywhereCacheAsync(anywhereCache, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceUpdateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateAnywhereCacheAsync(AnywhereCache, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<AnywhereCache, UpdateAnywhereCacheMetadata>> UpdateAnywhereCacheAsync(AnywhereCache anywhereCache, FieldMask updateMask, CancellationToken cancellationToken)

Updates an Anywhere Cache instance. Mutable fields include `ttl` and `admission_policy`.

**Parameters**  
---  
**Name** | **Description**  
`anywhereCache` | `[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)`  
Required. The Anywhere Cache instance to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. List of fields to be updated. Mutable fields of AnywhereCache include `ttl` and `admission_policy`. To specify ALL fields, specify a single field with the value `*`. Note: We recommend against doing this. If a new field is introduced at a later time, an older client updating with the `*` may accidentally reset the new field's value. Not specifying any fields is an error.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::AnywhereCache anywhereCache = new gcscv::AnywhereCache();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> response = await storageControlClient.UpdateAnywhereCacheAsync(anywhereCache, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceUpdateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateAnywhereCacheAsync(UpdateAnywhereCacheRequest, CallSettings)
    
    
    public virtual Task<Operation<AnywhereCache, UpdateAnywhereCacheMetadata>> UpdateAnywhereCacheAsync(UpdateAnywhereCacheRequest request, CallSettings callSettings = null)

Updates an Anywhere Cache instance. Mutable fields include `ttl` and `admission_policy`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateAnywhereCacheRequest request = new gcscv::UpdateAnywhereCacheRequest
    {
        AnywhereCache = new gcscv::AnywhereCache(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> response = await storageControlClient.UpdateAnywhereCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceUpdateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateAnywhereCacheAsync(UpdateAnywhereCacheRequest, CancellationToken)
    
    
    public virtual Task<Operation<AnywhereCache, UpdateAnywhereCacheMetadata>> UpdateAnywhereCacheAsync(UpdateAnywhereCacheRequest request, CancellationToken cancellationToken)

Updates an Anywhere Cache instance. Mutable fields include `ttl` and `admission_policy`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache)[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateAnywhereCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateAnywhereCacheRequest request = new gcscv::UpdateAnywhereCacheRequest
    {
        AnywhereCache = new gcscv::AnywhereCache(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> response = await storageControlClient.UpdateAnywhereCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::AnywhereCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::AnywhereCache, gcscv::UpdateAnywhereCacheMetadata> retrievedResponse = await storageControlClient.PollOnceUpdateAnywhereCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::AnywhereCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFolderIntelligenceConfig(IntelligenceConfig, FieldMask, CallSettings)
    
    
    public virtual IntelligenceConfig UpdateFolderIntelligenceConfig(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.UpdateFolderIntelligenceConfig(intelligenceConfig, updateMask);
    

### UpdateFolderIntelligenceConfig(UpdateFolderIntelligenceConfigRequest, CallSettings)
    
    
    public virtual IntelligenceConfig UpdateFolderIntelligenceConfig(UpdateFolderIntelligenceConfigRequest request, CallSettings callSettings = null)

Updates the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateFolderIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::UpdateFolderIntelligenceConfigRequest request = new gcscv::UpdateFolderIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.UpdateFolderIntelligenceConfig(request);
    

### UpdateFolderIntelligenceConfigAsync(IntelligenceConfig, FieldMask, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> UpdateFolderIntelligenceConfigAsync(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateFolderIntelligenceConfigAsync(intelligenceConfig, updateMask);
    

### UpdateFolderIntelligenceConfigAsync(IntelligenceConfig, FieldMask, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> UpdateFolderIntelligenceConfigAsync(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CancellationToken cancellationToken)

Updates the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateFolderIntelligenceConfigAsync(intelligenceConfig, updateMask);
    

### UpdateFolderIntelligenceConfigAsync(UpdateFolderIntelligenceConfigRequest, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> UpdateFolderIntelligenceConfigAsync(UpdateFolderIntelligenceConfigRequest request, CallSettings callSettings = null)

Updates the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateFolderIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateFolderIntelligenceConfigRequest request = new gcscv::UpdateFolderIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateFolderIntelligenceConfigAsync(request);
    

### UpdateFolderIntelligenceConfigAsync(UpdateFolderIntelligenceConfigRequest, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> UpdateFolderIntelligenceConfigAsync(UpdateFolderIntelligenceConfigRequest request, CancellationToken cancellationToken)

Updates the Folder scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateFolderIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateFolderIntelligenceConfigRequest request = new gcscv::UpdateFolderIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateFolderIntelligenceConfigAsync(request);
    

### UpdateManagedFolder(ManagedFolder, FieldMask, CallSettings)
    
    
    public virtual ManagedFolder UpdateManagedFolder(ManagedFolder managedFolder, FieldMask updateMask, CallSettings callSettings = null)

Updates a managed folder. Currently, this RPC only supports updating the `rapid_cache_config` field.

**Parameters**  
---  
**Name** | **Description**  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being updated. Currently, this RPC only supports updating the `rapid_cache_config` field in `managed_folder`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Update mask for managed_folder. Currently, this RPC only supports updating the `rapid_cache_config` field in `managed_folder`. This field also supports update mask for the subfields in the map of `rapid_cache_config`. The user can specify the update mask for `rapid_cache_config.policies` and `rapid_cache_config.policies.<key>`, but patching is not supported for a field within `RapidCachePolicy.policies.<key>`, like rapid_cache_config.policies.[key].ingest_on_write.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::ManagedFolder response = storageControlClient.UpdateManagedFolder(managedFolder, updateMask);
    

### UpdateManagedFolder(UpdateManagedFolderRequest, CallSettings)
    
    
    public virtual ManagedFolder UpdateManagedFolder(UpdateManagedFolderRequest request, CallSettings callSettings = null)

Updates a managed folder. Currently, this RPC only supports updating the `rapid_cache_config` field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::UpdateManagedFolderRequest request = new gcscv::UpdateManagedFolderRequest
    {
        ManagedFolder = new gcscv::ManagedFolder(),
        UpdateMask = new FieldMask(),
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        RequestId = "",
    };
    // Make the request
    gcscv::ManagedFolder response = storageControlClient.UpdateManagedFolder(request);
    

### UpdateManagedFolderAsync(ManagedFolder, FieldMask, CallSettings)
    
    
    public virtual Task<ManagedFolder> UpdateManagedFolderAsync(ManagedFolder managedFolder, FieldMask updateMask, CallSettings callSettings = null)

Updates a managed folder. Currently, this RPC only supports updating the `rapid_cache_config` field.

**Parameters**  
---  
**Name** | **Description**  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being updated. Currently, this RPC only supports updating the `rapid_cache_config` field in `managed_folder`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Update mask for managed_folder. Currently, this RPC only supports updating the `rapid_cache_config` field in `managed_folder`. This field also supports update mask for the subfields in the map of `rapid_cache_config`. The user can specify the update mask for `rapid_cache_config.policies` and `rapid_cache_config.policies.<key>`, but patching is not supported for a field within `RapidCachePolicy.policies.<key>`, like rapid_cache_config.policies.[key].ingest_on_write.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.UpdateManagedFolderAsync(managedFolder, updateMask);
    

### UpdateManagedFolderAsync(ManagedFolder, FieldMask, CancellationToken)
    
    
    public virtual Task<ManagedFolder> UpdateManagedFolderAsync(ManagedFolder managedFolder, FieldMask updateMask, CancellationToken cancellationToken)

Updates a managed folder. Currently, this RPC only supports updating the `rapid_cache_config` field.

**Parameters**  
---  
**Name** | **Description**  
`managedFolder` | `[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)`  
Required. Properties of the managed folder being updated. Currently, this RPC only supports updating the `rapid_cache_config` field in `managed_folder`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Update mask for managed_folder. Currently, this RPC only supports updating the `rapid_cache_config` field in `managed_folder`. This field also supports update mask for the subfields in the map of `rapid_cache_config`. The user can specify the update mask for `rapid_cache_config.policies` and `rapid_cache_config.policies.<key>`, but patching is not supported for a field within `RapidCachePolicy.policies.<key>`, like rapid_cache_config.policies.[key].ingest_on_write.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ManagedFolder managedFolder = new gcscv::ManagedFolder();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.UpdateManagedFolderAsync(managedFolder, updateMask);
    

### UpdateManagedFolderAsync(UpdateManagedFolderRequest, CallSettings)
    
    
    public virtual Task<ManagedFolder> UpdateManagedFolderAsync(UpdateManagedFolderRequest request, CallSettings callSettings = null)

Updates a managed folder. Currently, this RPC only supports updating the `rapid_cache_config` field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateManagedFolderRequest request = new gcscv::UpdateManagedFolderRequest
    {
        ManagedFolder = new gcscv::ManagedFolder(),
        UpdateMask = new FieldMask(),
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        RequestId = "",
    };
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.UpdateManagedFolderAsync(request);
    

### UpdateManagedFolderAsync(UpdateManagedFolderRequest, CancellationToken)
    
    
    public virtual Task<ManagedFolder> UpdateManagedFolderAsync(UpdateManagedFolderRequest request, CancellationToken cancellationToken)

Updates a managed folder. Currently, this RPC only supports updating the `rapid_cache_config` field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateManagedFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateManagedFolderRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateManagedFolderRequest request = new gcscv::UpdateManagedFolderRequest
    {
        ManagedFolder = new gcscv::ManagedFolder(),
        UpdateMask = new FieldMask(),
        IfMetagenerationMatch = 0L,
        IfMetagenerationNotMatch = 0L,
        RequestId = "",
    };
    // Make the request
    gcscv::ManagedFolder response = await storageControlClient.UpdateManagedFolderAsync(request);
    

### UpdateOrganizationIntelligenceConfig(IntelligenceConfig, FieldMask, CallSettings)
    
    
    public virtual IntelligenceConfig UpdateOrganizationIntelligenceConfig(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.UpdateOrganizationIntelligenceConfig(intelligenceConfig, updateMask);
    

### UpdateOrganizationIntelligenceConfig(UpdateOrganizationIntelligenceConfigRequest, CallSettings)
    
    
    public virtual IntelligenceConfig UpdateOrganizationIntelligenceConfig(UpdateOrganizationIntelligenceConfigRequest request, CallSettings callSettings = null)

Updates the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::UpdateOrganizationIntelligenceConfigRequest request = new gcscv::UpdateOrganizationIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.UpdateOrganizationIntelligenceConfig(request);
    

### UpdateOrganizationIntelligenceConfigAsync(IntelligenceConfig, FieldMask, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> UpdateOrganizationIntelligenceConfigAsync(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateOrganizationIntelligenceConfigAsync(intelligenceConfig, updateMask);
    

### UpdateOrganizationIntelligenceConfigAsync(IntelligenceConfig, FieldMask, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> UpdateOrganizationIntelligenceConfigAsync(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CancellationToken cancellationToken)

Updates the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateOrganizationIntelligenceConfigAsync(intelligenceConfig, updateMask);
    

### UpdateOrganizationIntelligenceConfigAsync(UpdateOrganizationIntelligenceConfigRequest, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> UpdateOrganizationIntelligenceConfigAsync(UpdateOrganizationIntelligenceConfigRequest request, CallSettings callSettings = null)

Updates the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateOrganizationIntelligenceConfigRequest request = new gcscv::UpdateOrganizationIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateOrganizationIntelligenceConfigAsync(request);
    

### UpdateOrganizationIntelligenceConfigAsync(UpdateOrganizationIntelligenceConfigRequest, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> UpdateOrganizationIntelligenceConfigAsync(UpdateOrganizationIntelligenceConfigRequest request, CancellationToken cancellationToken)

Updates the Organization scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateOrganizationIntelligenceConfigRequest request = new gcscv::UpdateOrganizationIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateOrganizationIntelligenceConfigAsync(request);
    

### UpdateProjectIntelligenceConfig(IntelligenceConfig, FieldMask, CallSettings)
    
    
    public virtual IntelligenceConfig UpdateProjectIntelligenceConfig(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.UpdateProjectIntelligenceConfig(intelligenceConfig, updateMask);
    

### UpdateProjectIntelligenceConfig(UpdateProjectIntelligenceConfigRequest, CallSettings)
    
    
    public virtual IntelligenceConfig UpdateProjectIntelligenceConfig(UpdateProjectIntelligenceConfigRequest request, CallSettings callSettings = null)

Updates the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProjectIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateProjectIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::UpdateProjectIntelligenceConfigRequest request = new gcscv::UpdateProjectIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = storageControlClient.UpdateProjectIntelligenceConfig(request);
    

### UpdateProjectIntelligenceConfigAsync(IntelligenceConfig, FieldMask, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> UpdateProjectIntelligenceConfigAsync(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateProjectIntelligenceConfigAsync(intelligenceConfig, updateMask);
    

### UpdateProjectIntelligenceConfigAsync(IntelligenceConfig, FieldMask, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> UpdateProjectIntelligenceConfigAsync(IntelligenceConfig intelligenceConfig, FieldMask updateMask, CancellationToken cancellationToken)

Updates the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`intelligenceConfig` | `[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)`  
Required. The `IntelligenceConfig` resource to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::IntelligenceConfig intelligenceConfig = new gcscv::IntelligenceConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateProjectIntelligenceConfigAsync(intelligenceConfig, updateMask);
    

### UpdateProjectIntelligenceConfigAsync(UpdateProjectIntelligenceConfigRequest, CallSettings)
    
    
    public virtual Task<IntelligenceConfig> UpdateProjectIntelligenceConfigAsync(UpdateProjectIntelligenceConfigRequest request, CallSettings callSettings = null)

Updates the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProjectIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateProjectIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateProjectIntelligenceConfigRequest request = new gcscv::UpdateProjectIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateProjectIntelligenceConfigAsync(request);
    

### UpdateProjectIntelligenceConfigAsync(UpdateProjectIntelligenceConfigRequest, CancellationToken)
    
    
    public virtual Task<IntelligenceConfig> UpdateProjectIntelligenceConfigAsync(UpdateProjectIntelligenceConfigRequest request, CancellationToken cancellationToken)

Updates the Project scoped singleton IntelligenceConfig resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProjectIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateProjectIntelligenceConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateProjectIntelligenceConfigRequest request = new gcscv::UpdateProjectIntelligenceConfigRequest
    {
        IntelligenceConfig = new gcscv::IntelligenceConfig(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    gcscv::IntelligenceConfig response = await storageControlClient.UpdateProjectIntelligenceConfigAsync(request);
    

### UpdateRapidCache(RapidCache, FieldMask, CallSettings)
    
    
    public virtual Operation<RapidCache, UpdateRapidCacheMetadata> UpdateRapidCache(RapidCache rapidCache, FieldMask updateMask, CallSettings callSettings = null)

Updates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. List of fields to be updated. Mutable fields of RapidCache include `ttl`, `admission_policy` and `ingest_on_write`. To specify ALL fields, specify a single field with the value `*`. Note: We recommend against doing this. If a new field is introduced at a later time, an older client updating with the `*` may accidentally reset the new field's value. Not specifying any fields is an error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[UpdateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> response = storageControlClient.UpdateRapidCache(rapidCache, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> retrievedResponse = storageControlClient.PollOnceUpdateRapidCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateRapidCache(UpdateRapidCacheRequest, CallSettings)
    
    
    public virtual Operation<RapidCache, UpdateRapidCacheMetadata> UpdateRapidCache(UpdateRapidCacheRequest request, CallSettings callSettings = null)

Updates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[UpdateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::UpdateRapidCacheRequest request = new gcscv::UpdateRapidCacheRequest
    {
        RapidCache = new gcscv::RapidCache(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> response = storageControlClient.UpdateRapidCache(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> retrievedResponse = storageControlClient.PollOnceUpdateRapidCache(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateRapidCacheAsync(RapidCache, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, UpdateRapidCacheMetadata>> UpdateRapidCacheAsync(RapidCache rapidCache, FieldMask updateMask, CallSettings callSettings = null)

Updates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. List of fields to be updated. Mutable fields of RapidCache include `ttl`, `admission_policy` and `ingest_on_write`. To specify ALL fields, specify a single field with the value `*`. Note: We recommend against doing this. If a new field is introduced at a later time, an older client updating with the `*` may accidentally reset the new field's value. Not specifying any fields is an error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[UpdateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> response = await storageControlClient.UpdateRapidCacheAsync(rapidCache, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceUpdateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateRapidCacheAsync(RapidCache, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<RapidCache, UpdateRapidCacheMetadata>> UpdateRapidCacheAsync(RapidCache rapidCache, FieldMask updateMask, CancellationToken cancellationToken)

Updates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`rapidCache` | `[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)`  
Required. The RapidCache to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. List of fields to be updated. Mutable fields of RapidCache include `ttl`, `admission_policy` and `ingest_on_write`. To specify ALL fields, specify a single field with the value `*`. Note: We recommend against doing this. If a new field is introduced at a later time, an older client updating with the `*` may accidentally reset the new field's value. Not specifying any fields is an error.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[UpdateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::RapidCache rapidCache = new gcscv::RapidCache();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> response = await storageControlClient.UpdateRapidCacheAsync(rapidCache, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceUpdateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateRapidCacheAsync(UpdateRapidCacheRequest, CallSettings)
    
    
    public virtual Task<Operation<RapidCache, UpdateRapidCacheMetadata>> UpdateRapidCacheAsync(UpdateRapidCacheRequest request, CallSettings callSettings = null)

Updates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[UpdateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateRapidCacheRequest request = new gcscv::UpdateRapidCacheRequest
    {
        RapidCache = new gcscv::RapidCache(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> response = await storageControlClient.UpdateRapidCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceUpdateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### UpdateRapidCacheAsync(UpdateRapidCacheRequest, CancellationToken)
    
    
    public virtual Task<Operation<RapidCache, UpdateRapidCacheMetadata>> UpdateRapidCacheAsync(UpdateRapidCacheRequest request, CancellationToken cancellationToken)

Updates a Rapid Cache instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRapidCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RapidCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.RapidCache)[UpdateRapidCacheMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateRapidCacheMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::UpdateRapidCacheRequest request = new gcscv::UpdateRapidCacheRequest
    {
        RapidCache = new gcscv::RapidCache(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> response = await storageControlClient.UpdateRapidCacheAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcscv::RapidCache result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcscv::RapidCache, gcscv::UpdateRapidCacheMetadata> retrievedResponse = await storageControlClient.PollOnceUpdateRapidCacheAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcscv::RapidCache retrievedResult = retrievedResponse.Result;
    }
    

### ViewObjectFullContext(ObjectName, long, string, CallSettings)
    
    
    public virtual ObjectFullContext ViewObjectFullContext(ObjectName name, long generation, string contextKey, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectName)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`generation` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. If present, selects a specific revision of this object (as opposed to the latest version, the default).  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ObjectName name = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]");
    long generation = 0L;
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = storageControlClient.ViewObjectFullContext(name, generation, contextKey);
    

### ViewObjectFullContext(ObjectName, string, CallSettings)
    
    
    public virtual ObjectFullContext ViewObjectFullContext(ObjectName name, string contextKey, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectName)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ObjectName name = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]");
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = storageControlClient.ViewObjectFullContext(name, contextKey);
    

### ViewObjectFullContext(ViewObjectFullContextRequest, CallSettings)
    
    
    public virtual ObjectFullContext ViewObjectFullContext(ViewObjectFullContextRequest request, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ViewObjectFullContextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    gcscv::ViewObjectFullContextRequest request = new gcscv::ViewObjectFullContextRequest
    {
        Generation = 0L,
        ContextKey = "",
        ObjectName = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]"),
    };
    // Make the request
    gcscv::ObjectFullContext response = storageControlClient.ViewObjectFullContext(request);
    

### ViewObjectFullContext(string, long, string, CallSettings)
    
    
    public virtual ObjectFullContext ViewObjectFullContext(string name, long generation, string contextKey, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`generation` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. If present, selects a specific revision of this object (as opposed to the latest version, the default).  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/objects/[OBJECT]";
    long generation = 0L;
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = storageControlClient.ViewObjectFullContext(name, generation, contextKey);
    

### ViewObjectFullContext(string, string, CallSettings)
    
    
    public virtual ObjectFullContext ViewObjectFullContext(string name, string contextKey, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | The RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = gcscv::StorageControlClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/objects/[OBJECT]";
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = storageControlClient.ViewObjectFullContext(name, contextKey);
    

### ViewObjectFullContextAsync(ObjectName, long, string, CallSettings)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(ObjectName name, long generation, string contextKey, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectName)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`generation` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. If present, selects a specific revision of this object (as opposed to the latest version, the default).  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ObjectName name = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]");
    long generation = 0L;
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(name, generation, contextKey);
    

### ViewObjectFullContextAsync(ObjectName, long, string, CancellationToken)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(ObjectName name, long generation, string contextKey, CancellationToken cancellationToken)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectName)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`generation` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. If present, selects a specific revision of this object (as opposed to the latest version, the default).  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ObjectName name = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]");
    long generation = 0L;
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(name, generation, contextKey);
    

### ViewObjectFullContextAsync(ObjectName, string, CallSettings)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(ObjectName name, string contextKey, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectName)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ObjectName name = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]");
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(name, contextKey);
    

### ViewObjectFullContextAsync(ObjectName, string, CancellationToken)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(ObjectName name, string contextKey, CancellationToken cancellationToken)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectName)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ObjectName name = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]");
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(name, contextKey);
    

### ViewObjectFullContextAsync(ViewObjectFullContextRequest, CallSettings)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(ViewObjectFullContextRequest request, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ViewObjectFullContextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ViewObjectFullContextRequest request = new gcscv::ViewObjectFullContextRequest
    {
        Generation = 0L,
        ContextKey = "",
        ObjectName = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]"),
    };
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(request);
    

### ViewObjectFullContextAsync(ViewObjectFullContextRequest, CancellationToken)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(ViewObjectFullContextRequest request, CancellationToken cancellationToken)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ViewObjectFullContextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    gcscv::ViewObjectFullContextRequest request = new gcscv::ViewObjectFullContextRequest
    {
        Generation = 0L,
        ContextKey = "",
        ObjectName = gcscv::ObjectName.FromProjectBucketObject("[PROJECT]", "[BUCKET]", "[OBJECT]"),
    };
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(request);
    

### ViewObjectFullContextAsync(string, long, string, CallSettings)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(string name, long generation, string contextKey, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`generation` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. If present, selects a specific revision of this object (as opposed to the latest version, the default).  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/objects/[OBJECT]";
    long generation = 0L;
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(name, generation, contextKey);
    

### ViewObjectFullContextAsync(string, long, string, CancellationToken)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(string name, long generation, string contextKey, CancellationToken cancellationToken)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`generation` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. If present, selects a specific revision of this object (as opposed to the latest version, the default).  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/objects/[OBJECT]";
    long generation = 0L;
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(name, generation, contextKey);
    

### ViewObjectFullContextAsync(string, string, CallSettings)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(string name, string contextKey, CallSettings callSettings = null)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/objects/[OBJECT]";
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(name, contextKey);
    

### ViewObjectFullContextAsync(string, string, CancellationToken)
    
    
    public virtual Task<ObjectFullContext> ViewObjectFullContextAsync(string name, string contextKey, CancellationToken cancellationToken)

Retrieves the full content of an object context, including its key, value, and any associated extended data for a given context key.

Object contexts can optionally contain extended data. If an object context contains extended data, the metadata payload structure will contain only its type URL. To retrieve the full extended data, call this method.

Returns the complete representation of the context as an [`ObjectFullContext`][google.storage.control.v2.ObjectFullContext].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`  
`contextKey` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The key of the object context to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ObjectFullContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectFullContext)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcscv::StorageControlClient storageControlClient = await gcscv::StorageControlClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/buckets/[BUCKET]/objects/[OBJECT]";
    string contextKey = "";
    // Make the request
    gcscv::ObjectFullContext response = await storageControlClient.ViewObjectFullContextAsync(name, contextKey);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
