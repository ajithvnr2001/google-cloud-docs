---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient
title: AlloyDB v1beta API - Class AlloyDBAdminClient (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:06.716036+00:00
---

# AlloyDB v1beta API - Class AlloyDBAdminClient (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class AlloyDBAdminClient (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public abstract class AlloyDBAdminClient

Reference documentation and code samples for the AlloyDB v1beta API class AlloyDBAdminClient.

AlloyDBAdmin client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AlloyDBAdminClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AlloyDBAdminClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClientImpl)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Remarks

Service describing handlers for resources

## Properties 

### BatchCreateInstancesOperationsClient
    
    
    public virtual OperationsClient BatchCreateInstancesOperationsClient { get; }

The long-running operations client for `BatchCreateInstances`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateBackupOperationsClient
    
    
    public virtual OperationsClient CreateBackupOperationsClient { get; }

The long-running operations client for `CreateBackup`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateClusterOperationsClient
    
    
    public virtual OperationsClient CreateClusterOperationsClient { get; }

The long-running operations client for `CreateCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateInstanceOperationsClient
    
    
    public virtual OperationsClient CreateInstanceOperationsClient { get; }

The long-running operations client for `CreateInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateSecondaryClusterOperationsClient
    
    
    public virtual OperationsClient CreateSecondaryClusterOperationsClient { get; }

The long-running operations client for `CreateSecondaryCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateSecondaryInstanceOperationsClient
    
    
    public virtual OperationsClient CreateSecondaryInstanceOperationsClient { get; }

The long-running operations client for `CreateSecondaryInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AlloyDBAdmin service, which is a host of "alloydb.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AlloyDBAdmin scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AlloyDBAdmin scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteBackupOperationsClient
    
    
    public virtual OperationsClient DeleteBackupOperationsClient { get; }

The long-running operations client for `DeleteBackup`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteClusterOperationsClient
    
    
    public virtual OperationsClient DeleteClusterOperationsClient { get; }

The long-running operations client for `DeleteCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteInstanceOperationsClient
    
    
    public virtual OperationsClient DeleteInstanceOperationsClient { get; }

The long-running operations client for `DeleteInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ExportClusterOperationsClient
    
    
    public virtual OperationsClient ExportClusterOperationsClient { get; }

The long-running operations client for `ExportCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### FailoverInstanceOperationsClient
    
    
    public virtual OperationsClient FailoverInstanceOperationsClient { get; }

The long-running operations client for `FailoverInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual AlloyDBAdmin.AlloyDBAdminClient GrpcClient { get; }

The underlying gRPC AlloyDBAdmin client

**Property Value**  
---  
**Type** | **Description**  
`[AlloyDBAdmin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdmin)[AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdmin.AlloyDBAdminClient)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
### ImportClusterOperationsClient
    
    
    public virtual OperationsClient ImportClusterOperationsClient { get; }

The long-running operations client for `ImportCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### InjectFaultOperationsClient
    
    
    public virtual OperationsClient InjectFaultOperationsClient { get; }

The long-running operations client for `InjectFault`.

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
  
### PromoteClusterOperationsClient
    
    
    public virtual OperationsClient PromoteClusterOperationsClient { get; }

The long-running operations client for `PromoteCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### RestartInstanceOperationsClient
    
    
    public virtual OperationsClient RestartInstanceOperationsClient { get; }

The long-running operations client for `RestartInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### RestoreClusterOperationsClient
    
    
    public virtual OperationsClient RestoreClusterOperationsClient { get; }

The long-running operations client for `RestoreCluster`.

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
  
### SwitchoverClusterOperationsClient
    
    
    public virtual OperationsClient SwitchoverClusterOperationsClient { get; }

The long-running operations client for `SwitchoverCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateBackupOperationsClient
    
    
    public virtual OperationsClient UpdateBackupOperationsClient { get; }

The long-running operations client for `UpdateBackup`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateClusterOperationsClient
    
    
    public virtual OperationsClient UpdateClusterOperationsClient { get; }

The long-running operations client for `UpdateCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateInstanceOperationsClient
    
    
    public virtual OperationsClient UpdateInstanceOperationsClient { get; }

The long-running operations client for `UpdateInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpgradeClusterOperationsClient
    
    
    public virtual OperationsClient UpgradeClusterOperationsClient { get; }

The long-running operations client for `UpgradeCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### BatchCreateInstances(BatchCreateInstancesRequest, CallSettings)
    
    
    public virtual Operation<BatchCreateInstancesResponse, OperationMetadata> BatchCreateInstances(BatchCreateInstancesRequest request, CallSettings callSettings = null)

Creates new instances under the given project, location and cluster. There can be only one primary instance in a cluster. If the primary instance exists in the cluster as well as this request, then API will throw an error. The primary instance should exist before any read pool instance is created. If the primary instance is a part of the request payload, then the API will take care of creating instances in the correct order. This method is here to support Google-internal use cases, and is not meant for external customers to consume. Please do not start relying on it; its behavior is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    BatchCreateInstancesRequest request = new BatchCreateInstancesRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Requests = new CreateInstanceRequests(),
        RequestId = "",
    };
    // Make the request
    Operation<BatchCreateInstancesResponse, OperationMetadata> response = alloyDBAdminClient.BatchCreateInstances(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateInstancesResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchCreateInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateInstancesResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceBatchCreateInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateInstancesAsync(BatchCreateInstancesRequest, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateInstancesResponse, OperationMetadata>> BatchCreateInstancesAsync(BatchCreateInstancesRequest request, CallSettings callSettings = null)

Creates new instances under the given project, location and cluster. There can be only one primary instance in a cluster. If the primary instance exists in the cluster as well as this request, then API will throw an error. The primary instance should exist before any read pool instance is created. If the primary instance is a part of the request payload, then the API will take care of creating instances in the correct order. This method is here to support Google-internal use cases, and is not meant for external customers to consume. Please do not start relying on it; its behavior is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    BatchCreateInstancesRequest request = new BatchCreateInstancesRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Requests = new CreateInstanceRequests(),
        RequestId = "",
    };
    // Make the request
    Operation<BatchCreateInstancesResponse, OperationMetadata> response = await alloyDBAdminClient.BatchCreateInstancesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateInstancesResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceBatchCreateInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateInstancesAsync(BatchCreateInstancesRequest, CancellationToken)
    
    
    public virtual Task<Operation<BatchCreateInstancesResponse, OperationMetadata>> BatchCreateInstancesAsync(BatchCreateInstancesRequest request, CancellationToken cancellationToken)

Creates new instances under the given project, location and cluster. There can be only one primary instance in a cluster. If the primary instance exists in the cluster as well as this request, then API will throw an error. The primary instance should exist before any read pool instance is created. If the primary instance is a part of the request payload, then the API will take care of creating instances in the correct order. This method is here to support Google-internal use cases, and is not meant for external customers to consume. Please do not start relying on it; its behavior is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    BatchCreateInstancesRequest request = new BatchCreateInstancesRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Requests = new CreateInstanceRequests(),
        RequestId = "",
    };
    // Make the request
    Operation<BatchCreateInstancesResponse, OperationMetadata> response = await alloyDBAdminClient.BatchCreateInstancesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateInstancesResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceBatchCreateInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static AlloyDBAdminClient Create()

Synchronously creates a [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AlloyDBAdminClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient)` | The created [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AlloyDBAdminClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AlloyDBAdminClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient)` | The task representing the created [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient).  
  
### CreateBackup(LocationName, Backup, string, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> CreateBackup(LocationName parent, Backup backup, string backupId, CallSettings callSettings = null)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being created  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = alloyDBAdminClient.CreateBackup(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackup(CreateBackupRequest, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> CreateBackup(CreateBackupRequest request, CallSettings callSettings = null)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    CreateBackupRequest request = new CreateBackupRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        BackupId = "",
        Backup = new Backup(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = alloyDBAdminClient.CreateBackup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackup(string, Backup, string, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> CreateBackup(string parent, Backup backup, string backupId, CallSettings callSettings = null)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being created  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = alloyDBAdminClient.CreateBackup(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(LocationName, Backup, string, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(LocationName parent, Backup backup, string backupId, CallSettings callSettings = null)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being created  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.CreateBackupAsync(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(LocationName, Backup, string, CancellationToken)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(LocationName parent, Backup backup, string backupId, CancellationToken cancellationToken)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being created  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.CreateBackupAsync(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(CreateBackupRequest, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(CreateBackupRequest request, CallSettings callSettings = null)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateBackupRequest request = new CreateBackupRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        BackupId = "",
        Backup = new Backup(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.CreateBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(CreateBackupRequest, CancellationToken)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(CreateBackupRequest request, CancellationToken cancellationToken)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateBackupRequest request = new CreateBackupRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        BackupId = "",
        Backup = new Backup(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.CreateBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(string, Backup, string, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(string parent, Backup backup, string backupId, CallSettings callSettings = null)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being created  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.CreateBackupAsync(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(string, Backup, string, CancellationToken)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(string parent, Backup backup, string backupId, CancellationToken cancellationToken)

Creates a new Backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being created  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.CreateBackupAsync(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateCluster(LocationName, Cluster, string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateCluster(LocationName parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being created  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.CreateCluster(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateCluster(CreateClusterRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateCluster(CreateClusterRequest request, CallSettings callSettings = null)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    CreateClusterRequest request = new CreateClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.CreateCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateCluster(string, Cluster, string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateCluster(string parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being created  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.CreateCluster(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(LocationName, Cluster, string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(LocationName parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being created  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(LocationName, Cluster, string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(LocationName parent, Cluster cluster, string clusterId, CancellationToken cancellationToken)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being created  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(CreateClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(CreateClusterRequest request, CallSettings callSettings = null)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateClusterRequest request = new CreateClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(CreateClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(CreateClusterRequest request, CancellationToken cancellationToken)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateClusterRequest request = new CreateClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(string, Cluster, string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(string parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being created  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(string, Cluster, string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(string parent, Cluster cluster, string clusterId, CancellationToken cancellationToken)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being created  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateDatabase(ClusterName, Database, string, CallSettings)
    
    
    public virtual Database CreateDatabase(ClusterName parent, Database database, string databaseId, CallSettings callSettings = null)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Value for parent.  
`database` | `[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)`  
Required. The resource being created.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Database database = new Database();
    string databaseId = "";
    // Make the request
    Database response = alloyDBAdminClient.CreateDatabase(parent, database, databaseId);
    

### CreateDatabase(CreateDatabaseRequest, CallSettings)
    
    
    public virtual Database CreateDatabase(CreateDatabaseRequest request, CallSettings callSettings = null)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    CreateDatabaseRequest request = new CreateDatabaseRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        DatabaseId = "",
        Database = new Database(),
    };
    // Make the request
    Database response = alloyDBAdminClient.CreateDatabase(request);
    

### CreateDatabase(string, Database, string, CallSettings)
    
    
    public virtual Database CreateDatabase(string parent, Database database, string databaseId, CallSettings callSettings = null)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`database` | `[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)`  
Required. The resource being created.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Database database = new Database();
    string databaseId = "";
    // Make the request
    Database response = alloyDBAdminClient.CreateDatabase(parent, database, databaseId);
    

### CreateDatabaseAsync(ClusterName, Database, string, CallSettings)
    
    
    public virtual Task<Database> CreateDatabaseAsync(ClusterName parent, Database database, string databaseId, CallSettings callSettings = null)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Value for parent.  
`database` | `[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)`  
Required. The resource being created.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Database database = new Database();
    string databaseId = "";
    // Make the request
    Database response = await alloyDBAdminClient.CreateDatabaseAsync(parent, database, databaseId);
    

### CreateDatabaseAsync(ClusterName, Database, string, CancellationToken)
    
    
    public virtual Task<Database> CreateDatabaseAsync(ClusterName parent, Database database, string databaseId, CancellationToken cancellationToken)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Value for parent.  
`database` | `[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)`  
Required. The resource being created.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Database database = new Database();
    string databaseId = "";
    // Make the request
    Database response = await alloyDBAdminClient.CreateDatabaseAsync(parent, database, databaseId);
    

### CreateDatabaseAsync(CreateDatabaseRequest, CallSettings)
    
    
    public virtual Task<Database> CreateDatabaseAsync(CreateDatabaseRequest request, CallSettings callSettings = null)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateDatabaseRequest request = new CreateDatabaseRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        DatabaseId = "",
        Database = new Database(),
    };
    // Make the request
    Database response = await alloyDBAdminClient.CreateDatabaseAsync(request);
    

### CreateDatabaseAsync(CreateDatabaseRequest, CancellationToken)
    
    
    public virtual Task<Database> CreateDatabaseAsync(CreateDatabaseRequest request, CancellationToken cancellationToken)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateDatabaseRequest request = new CreateDatabaseRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        DatabaseId = "",
        Database = new Database(),
    };
    // Make the request
    Database response = await alloyDBAdminClient.CreateDatabaseAsync(request);
    

### CreateDatabaseAsync(string, Database, string, CallSettings)
    
    
    public virtual Task<Database> CreateDatabaseAsync(string parent, Database database, string databaseId, CallSettings callSettings = null)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`database` | `[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)`  
Required. The resource being created.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Database database = new Database();
    string databaseId = "";
    // Make the request
    Database response = await alloyDBAdminClient.CreateDatabaseAsync(parent, database, databaseId);
    

### CreateDatabaseAsync(string, Database, string, CancellationToken)
    
    
    public virtual Task<Database> CreateDatabaseAsync(string parent, Database database, string databaseId, CancellationToken cancellationToken)

Creates a new Database in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`database` | `[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)`  
Required. The resource being created.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Database database = new Database();
    string databaseId = "";
    // Make the request
    Database response = await alloyDBAdminClient.CreateDatabaseAsync(parent, database, databaseId);
    

### CreateInstance(ClusterName, Instance, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(ClusterName parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.CreateInstance(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstance(CreateInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(CreateInstanceRequest request, CallSettings callSettings = null)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.CreateInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstance(string, Instance, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(string parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.CreateInstance(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(ClusterName, Instance, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(ClusterName parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(ClusterName, Instance, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(ClusterName parent, Instance instance, string instanceId, CancellationToken cancellationToken)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(CreateInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(CreateInstanceRequest request, CallSettings callSettings = null)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(CreateInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(CreateInstanceRequest request, CancellationToken cancellationToken)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(string, Instance, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(string parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(string, Instance, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(string parent, Instance instance, string instanceId, CancellationToken cancellationToken)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryCluster(LocationName, Cluster, string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateSecondaryCluster(LocationName parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. Configuration of the requesting object (the secondary cluster).  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object (the secondary cluster).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.CreateSecondaryCluster(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateSecondaryCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryCluster(CreateSecondaryClusterRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateSecondaryCluster(CreateSecondaryClusterRequest request, CallSettings callSettings = null)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecondaryClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    CreateSecondaryClusterRequest request = new CreateSecondaryClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.CreateSecondaryCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateSecondaryCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryCluster(string, Cluster, string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateSecondaryCluster(string parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. Configuration of the requesting object (the secondary cluster).  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object (the secondary cluster).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.CreateSecondaryCluster(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateSecondaryCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryClusterAsync(LocationName, Cluster, string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateSecondaryClusterAsync(LocationName parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. Configuration of the requesting object (the secondary cluster).  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object (the secondary cluster).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryClusterAsync(LocationName, Cluster, string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateSecondaryClusterAsync(LocationName parent, Cluster cluster, string clusterId, CancellationToken cancellationToken)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. Configuration of the requesting object (the secondary cluster).  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object (the secondary cluster).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryClusterAsync(CreateSecondaryClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateSecondaryClusterAsync(CreateSecondaryClusterRequest request, CallSettings callSettings = null)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecondaryClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateSecondaryClusterRequest request = new CreateSecondaryClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryClusterAsync(CreateSecondaryClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateSecondaryClusterAsync(CreateSecondaryClusterRequest request, CancellationToken cancellationToken)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecondaryClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateSecondaryClusterRequest request = new CreateSecondaryClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryClusterAsync(string, Cluster, string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateSecondaryClusterAsync(string parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. Configuration of the requesting object (the secondary cluster).  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object (the secondary cluster).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryClusterAsync(string, Cluster, string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateSecondaryClusterAsync(string parent, Cluster cluster, string clusterId, CancellationToken cancellationToken)

Creates a cluster of type SECONDARY in the given location using the primary cluster as the source.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on the Cluster.name field.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. Configuration of the requesting object (the secondary cluster).  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object (the secondary cluster).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstance(ClusterName, Instance, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateSecondaryInstance(ClusterName parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.CreateSecondaryInstance(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateSecondaryInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstance(CreateSecondaryInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateSecondaryInstance(CreateSecondaryInstanceRequest request, CallSettings callSettings = null)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    CreateSecondaryInstanceRequest request = new CreateSecondaryInstanceRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.CreateSecondaryInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateSecondaryInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstance(string, Instance, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateSecondaryInstance(string parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.CreateSecondaryInstance(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceCreateSecondaryInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstanceAsync(ClusterName, Instance, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateSecondaryInstanceAsync(ClusterName parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstanceAsync(ClusterName, Instance, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateSecondaryInstanceAsync(ClusterName parent, Instance instance, string instanceId, CancellationToken cancellationToken)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstanceAsync(CreateSecondaryInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateSecondaryInstanceAsync(CreateSecondaryInstanceRequest request, CallSettings callSettings = null)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateSecondaryInstanceRequest request = new CreateSecondaryInstanceRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstanceAsync(CreateSecondaryInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateSecondaryInstanceAsync(CreateSecondaryInstanceRequest request, CancellationToken cancellationToken)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateSecondaryInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateSecondaryInstanceRequest request = new CreateSecondaryInstanceRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstanceAsync(string, Instance, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateSecondaryInstanceAsync(string parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateSecondaryInstanceAsync(string, Instance, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateSecondaryInstanceAsync(string parent, Instance instance, string instanceId, CancellationToken cancellationToken)

Creates a new SECONDARY Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.CreateSecondaryInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceCreateSecondaryInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateUser(ClusterName, User, string, CallSettings)
    
    
    public virtual User CreateUser(ClusterName parent, User user, string userId, CallSettings callSettings = null)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Value for parent.  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being created  
`userId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    User user = new User();
    string userId = "";
    // Make the request
    User response = alloyDBAdminClient.CreateUser(parent, user, userId);
    

### CreateUser(CreateUserRequest, CallSettings)
    
    
    public virtual User CreateUser(CreateUserRequest request, CallSettings callSettings = null)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateUserRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    CreateUserRequest request = new CreateUserRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        UserId = "",
        User = new User(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    User response = alloyDBAdminClient.CreateUser(request);
    

### CreateUser(string, User, string, CallSettings)
    
    
    public virtual User CreateUser(string parent, User user, string userId, CallSettings callSettings = null)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being created  
`userId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    User user = new User();
    string userId = "";
    // Make the request
    User response = alloyDBAdminClient.CreateUser(parent, user, userId);
    

### CreateUserAsync(ClusterName, User, string, CallSettings)
    
    
    public virtual Task<User> CreateUserAsync(ClusterName parent, User user, string userId, CallSettings callSettings = null)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Value for parent.  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being created  
`userId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    User user = new User();
    string userId = "";
    // Make the request
    User response = await alloyDBAdminClient.CreateUserAsync(parent, user, userId);
    

### CreateUserAsync(ClusterName, User, string, CancellationToken)
    
    
    public virtual Task<User> CreateUserAsync(ClusterName parent, User user, string userId, CancellationToken cancellationToken)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Value for parent.  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being created  
`userId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    User user = new User();
    string userId = "";
    // Make the request
    User response = await alloyDBAdminClient.CreateUserAsync(parent, user, userId);
    

### CreateUserAsync(CreateUserRequest, CallSettings)
    
    
    public virtual Task<User> CreateUserAsync(CreateUserRequest request, CallSettings callSettings = null)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateUserRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateUserRequest request = new CreateUserRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        UserId = "",
        User = new User(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    User response = await alloyDBAdminClient.CreateUserAsync(request);
    

### CreateUserAsync(CreateUserRequest, CancellationToken)
    
    
    public virtual Task<User> CreateUserAsync(CreateUserRequest request, CancellationToken cancellationToken)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CreateUserRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    CreateUserRequest request = new CreateUserRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        UserId = "",
        User = new User(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    User response = await alloyDBAdminClient.CreateUserAsync(request);
    

### CreateUserAsync(string, User, string, CallSettings)
    
    
    public virtual Task<User> CreateUserAsync(string parent, User user, string userId, CallSettings callSettings = null)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being created  
`userId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    User user = new User();
    string userId = "";
    // Make the request
    User response = await alloyDBAdminClient.CreateUserAsync(parent, user, userId);
    

### CreateUserAsync(string, User, string, CancellationToken)
    
    
    public virtual Task<User> CreateUserAsync(string parent, User user, string userId, CancellationToken cancellationToken)

Creates a new User in a given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being created  
`userId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    User user = new User();
    string userId = "";
    // Make the request
    User response = await alloyDBAdminClient.CreateUserAsync(parent, user, userId);
    

### DeleteBackup(BackupName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteBackup(BackupName name, CallSettings callSettings = null)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BackupName)`  
Required. Name of the resource. For the required format, see the comment on the Backup.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteBackup(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackup(DeleteBackupRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteBackup(DeleteBackupRequest request, CallSettings callSettings = null)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    DeleteBackupRequest request = new DeleteBackupRequest
    {
        BackupName = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]"),
        RequestId = "",
        ValidateOnly = false,
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteBackup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackup(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteBackup(string name, CallSettings callSettings = null)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource. For the required format, see the comment on the Backup.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/backups/[BACKUP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteBackup(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(BackupName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(BackupName name, CallSettings callSettings = null)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BackupName)`  
Required. Name of the resource. For the required format, see the comment on the Backup.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteBackupAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(BackupName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(BackupName name, CancellationToken cancellationToken)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BackupName)`  
Required. Name of the resource. For the required format, see the comment on the Backup.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteBackupAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(DeleteBackupRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(DeleteBackupRequest request, CallSettings callSettings = null)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    DeleteBackupRequest request = new DeleteBackupRequest
    {
        BackupName = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]"),
        RequestId = "",
        ValidateOnly = false,
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(DeleteBackupRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(DeleteBackupRequest request, CancellationToken cancellationToken)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    DeleteBackupRequest request = new DeleteBackupRequest
    {
        BackupName = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]"),
        RequestId = "",
        ValidateOnly = false,
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(string name, CallSettings callSettings = null)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource. For the required format, see the comment on the Backup.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/backups/[BACKUP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteBackupAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(string name, CancellationToken cancellationToken)

Deletes a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource. For the required format, see the comment on the Backup.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/backups/[BACKUP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteBackupAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCluster(ClusterName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteCluster(ClusterName name, CallSettings callSettings = null)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCluster(DeleteClusterRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteCluster(DeleteClusterRequest request, CallSettings callSettings = null)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    DeleteClusterRequest request = new DeleteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCluster(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteCluster(string name, CallSettings callSettings = null)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(ClusterName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(ClusterName name, CallSettings callSettings = null)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(ClusterName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(ClusterName name, CancellationToken cancellationToken)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(DeleteClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(DeleteClusterRequest request, CallSettings callSettings = null)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    DeleteClusterRequest request = new DeleteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(DeleteClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(DeleteClusterRequest request, CancellationToken cancellationToken)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    DeleteClusterRequest request = new DeleteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(string name, CallSettings callSettings = null)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(string name, CancellationToken cancellationToken)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(DeleteInstanceRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(DeleteInstanceRequest request, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(InstanceName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(InstanceName name, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(string name, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = alloyDBAdminClient.DeleteInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(DeleteInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(DeleteInstanceRequest request, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(DeleteInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(DeleteInstanceRequest request, CancellationToken cancellationToken)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(InstanceName name, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(string name, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(string name, CancellationToken cancellationToken)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await alloyDBAdminClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteUser(DeleteUserRequest, CallSettings)
    
    
    public virtual void DeleteUser(DeleteUserRequest request, CallSettings callSettings = null)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteUserRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    DeleteUserRequest request = new DeleteUserRequest
    {
        UserName = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    alloyDBAdminClient.DeleteUser(request);
    

### DeleteUser(UserName, CallSettings)
    
    
    public virtual void DeleteUser(UserName name, CallSettings callSettings = null)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UserName)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    UserName name = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]");
    // Make the request
    alloyDBAdminClient.DeleteUser(name);
    

### DeleteUser(string, CallSettings)
    
    
    public virtual void DeleteUser(string name, CallSettings callSettings = null)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/users/[USER]";
    // Make the request
    alloyDBAdminClient.DeleteUser(name);
    

### DeleteUserAsync(DeleteUserRequest, CallSettings)
    
    
    public virtual Task DeleteUserAsync(DeleteUserRequest request, CallSettings callSettings = null)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteUserRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    DeleteUserRequest request = new DeleteUserRequest
    {
        UserName = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    await alloyDBAdminClient.DeleteUserAsync(request);
    

### DeleteUserAsync(DeleteUserRequest, CancellationToken)
    
    
    public virtual Task DeleteUserAsync(DeleteUserRequest request, CancellationToken cancellationToken)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DeleteUserRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    DeleteUserRequest request = new DeleteUserRequest
    {
        UserName = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    await alloyDBAdminClient.DeleteUserAsync(request);
    

### DeleteUserAsync(UserName, CallSettings)
    
    
    public virtual Task DeleteUserAsync(UserName name, CallSettings callSettings = null)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UserName)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UserName name = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]");
    // Make the request
    await alloyDBAdminClient.DeleteUserAsync(name);
    

### DeleteUserAsync(UserName, CancellationToken)
    
    
    public virtual Task DeleteUserAsync(UserName name, CancellationToken cancellationToken)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UserName)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UserName name = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]");
    // Make the request
    await alloyDBAdminClient.DeleteUserAsync(name);
    

### DeleteUserAsync(string, CallSettings)
    
    
    public virtual Task DeleteUserAsync(string name, CallSettings callSettings = null)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/users/[USER]";
    // Make the request
    await alloyDBAdminClient.DeleteUserAsync(name);
    

### DeleteUserAsync(string, CancellationToken)
    
    
    public virtual Task DeleteUserAsync(string name, CancellationToken cancellationToken)

Deletes a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/users/[USER]";
    // Make the request
    await alloyDBAdminClient.DeleteUserAsync(name);
    

### ExecuteSql(ExecuteSqlRequest, CallSettings)
    
    
    public virtual ExecuteSqlResponse ExecuteSql(ExecuteSqlRequest request, CallSettings callSettings = null)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteSqlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ExecuteSqlRequest request = new ExecuteSqlRequest
    {
        InstanceAsInstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        Database = "",
        User = "",
        SqlStatement = "",
        Password = "",
        ValidateOnly = false,
    };
    // Make the request
    ExecuteSqlResponse response = alloyDBAdminClient.ExecuteSql(request);
    

### ExecuteSql(InstanceName, string, string, string, string, CallSettings)
    
    
    public virtual ExecuteSqlResponse ExecuteSql(InstanceName instance, string database, string user, string sqlStatement, string password, CallSettings callSettings = null)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`sqlStatement` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements.  
`password` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The database native user’s password.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InstanceName instance = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    string database = "";
    string user = "";
    string sqlStatement = "";
    string password = "";
    // Make the request
    ExecuteSqlResponse response = alloyDBAdminClient.ExecuteSql(instance, database, user, sqlStatement, password);
    

### ExecuteSql(string, string, string, string, string, CallSettings)
    
    
    public virtual ExecuteSqlResponse ExecuteSql(string instance, string database, string user, string sqlStatement, string password, CallSettings callSettings = null)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`sqlStatement` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements.  
`password` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The database native user’s password.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string instance = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    string database = "";
    string user = "";
    string sqlStatement = "";
    string password = "";
    // Make the request
    ExecuteSqlResponse response = alloyDBAdminClient.ExecuteSql(instance, database, user, sqlStatement, password);
    

### ExecuteSqlAsync(ExecuteSqlRequest, CallSettings)
    
    
    public virtual Task<ExecuteSqlResponse> ExecuteSqlAsync(ExecuteSqlRequest request, CallSettings callSettings = null)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteSqlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ExecuteSqlRequest request = new ExecuteSqlRequest
    {
        InstanceAsInstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        Database = "",
        User = "",
        SqlStatement = "",
        Password = "",
        ValidateOnly = false,
    };
    // Make the request
    ExecuteSqlResponse response = await alloyDBAdminClient.ExecuteSqlAsync(request);
    

### ExecuteSqlAsync(ExecuteSqlRequest, CancellationToken)
    
    
    public virtual Task<ExecuteSqlResponse> ExecuteSqlAsync(ExecuteSqlRequest request, CancellationToken cancellationToken)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteSqlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ExecuteSqlRequest request = new ExecuteSqlRequest
    {
        InstanceAsInstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        Database = "",
        User = "",
        SqlStatement = "",
        Password = "",
        ValidateOnly = false,
    };
    // Make the request
    ExecuteSqlResponse response = await alloyDBAdminClient.ExecuteSqlAsync(request);
    

### ExecuteSqlAsync(InstanceName, string, string, string, string, CallSettings)
    
    
    public virtual Task<ExecuteSqlResponse> ExecuteSqlAsync(InstanceName instance, string database, string user, string sqlStatement, string password, CallSettings callSettings = null)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`sqlStatement` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements.  
`password` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The database native user’s password.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName instance = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    string database = "";
    string user = "";
    string sqlStatement = "";
    string password = "";
    // Make the request
    ExecuteSqlResponse response = await alloyDBAdminClient.ExecuteSqlAsync(instance, database, user, sqlStatement, password);
    

### ExecuteSqlAsync(InstanceName, string, string, string, string, CancellationToken)
    
    
    public virtual Task<ExecuteSqlResponse> ExecuteSqlAsync(InstanceName instance, string database, string user, string sqlStatement, string password, CancellationToken cancellationToken)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`sqlStatement` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements.  
`password` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The database native user’s password.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName instance = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    string database = "";
    string user = "";
    string sqlStatement = "";
    string password = "";
    // Make the request
    ExecuteSqlResponse response = await alloyDBAdminClient.ExecuteSqlAsync(instance, database, user, sqlStatement, password);
    

### ExecuteSqlAsync(string, string, string, string, string, CallSettings)
    
    
    public virtual Task<ExecuteSqlResponse> ExecuteSqlAsync(string instance, string database, string user, string sqlStatement, string password, CallSettings callSettings = null)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`sqlStatement` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements.  
`password` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The database native user’s password.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string instance = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    string database = "";
    string user = "";
    string sqlStatement = "";
    string password = "";
    // Make the request
    ExecuteSqlResponse response = await alloyDBAdminClient.ExecuteSqlAsync(instance, database, user, sqlStatement, password);
    

### ExecuteSqlAsync(string, string, string, string, string, CancellationToken)
    
    
    public virtual Task<ExecuteSqlResponse> ExecuteSqlAsync(string instance, string database, string user, string sqlStatement, string password, CancellationToken cancellationToken)

Executes a SQL statement in a database inside an AlloyDB instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance where the SQL will be executed. For the required format, see the comment on the Instance.name field.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the query will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Database user to be used for executing the SQL. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`sqlStatement` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. SQL statement to execute on database. Any valid statement is permitted, including DDL, DML, DQL statements.  
`password` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The database native user’s password.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string instance = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    string database = "";
    string user = "";
    string sqlStatement = "";
    string password = "";
    // Make the request
    ExecuteSqlResponse response = await alloyDBAdminClient.ExecuteSqlAsync(instance, database, user, sqlStatement, password);
    

### ExportCluster(ClusterName, GcsDestination, string, CsvExportOptions, SqlExportOptions, CallSettings)
    
    
    public virtual Operation<ExportClusterResponse, OperationMetadata> ExportCluster(ClusterName name, GcsDestination gcsDestination, string database, ExportClusterRequest.Types.CsvExportOptions csvExportOptions, ExportClusterRequest.Types.SqlExportOptions sqlExportOptions, CallSettings callSettings = null)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`gcsDestination` | `[GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GcsDestination)`  
Required. Option to export data to cloud storage.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the export command will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`csvExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[CsvExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.CsvExportOptions)`  
Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[SqlExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.SqlExportOptions)`  
Options for exporting data in SQL format. Required field to be set for SQL file type.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    GcsDestination gcsDestination = new GcsDestination();
    string database = "";
    ExportClusterRequest.Types.CsvExportOptions csvExportOptions = new ExportClusterRequest.Types.CsvExportOptions();
    ExportClusterRequest.Types.SqlExportOptions sqlExportOptions = new ExportClusterRequest.Types.SqlExportOptions();
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = alloyDBAdminClient.ExportCluster(name, gcsDestination, database, csvExportOptions, sqlExportOptions);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceExportCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportCluster(ExportClusterRequest, CallSettings)
    
    
    public virtual Operation<ExportClusterResponse, OperationMetadata> ExportCluster(ExportClusterRequest request, CallSettings callSettings = null)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ExportClusterRequest request = new ExportClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        GcsDestination = new GcsDestination(),
        Database = "",
        CsvExportOptions = new ExportClusterRequest.Types.CsvExportOptions(),
    };
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = alloyDBAdminClient.ExportCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceExportCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportCluster(string, GcsDestination, string, CsvExportOptions, SqlExportOptions, CallSettings)
    
    
    public virtual Operation<ExportClusterResponse, OperationMetadata> ExportCluster(string name, GcsDestination gcsDestination, string database, ExportClusterRequest.Types.CsvExportOptions csvExportOptions, ExportClusterRequest.Types.SqlExportOptions sqlExportOptions, CallSettings callSettings = null)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`gcsDestination` | `[GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GcsDestination)`  
Required. Option to export data to cloud storage.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the export command will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`csvExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[CsvExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.CsvExportOptions)`  
Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[SqlExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.SqlExportOptions)`  
Options for exporting data in SQL format. Required field to be set for SQL file type.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    GcsDestination gcsDestination = new GcsDestination();
    string database = "";
    ExportClusterRequest.Types.CsvExportOptions csvExportOptions = new ExportClusterRequest.Types.CsvExportOptions();
    ExportClusterRequest.Types.SqlExportOptions sqlExportOptions = new ExportClusterRequest.Types.SqlExportOptions();
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = alloyDBAdminClient.ExportCluster(name, gcsDestination, database, csvExportOptions, sqlExportOptions);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceExportCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportClusterAsync(ClusterName, GcsDestination, string, CsvExportOptions, SqlExportOptions, CallSettings)
    
    
    public virtual Task<Operation<ExportClusterResponse, OperationMetadata>> ExportClusterAsync(ClusterName name, GcsDestination gcsDestination, string database, ExportClusterRequest.Types.CsvExportOptions csvExportOptions, ExportClusterRequest.Types.SqlExportOptions sqlExportOptions, CallSettings callSettings = null)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`gcsDestination` | `[GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GcsDestination)`  
Required. Option to export data to cloud storage.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the export command will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`csvExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[CsvExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.CsvExportOptions)`  
Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[SqlExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.SqlExportOptions)`  
Options for exporting data in SQL format. Required field to be set for SQL file type.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    GcsDestination gcsDestination = new GcsDestination();
    string database = "";
    ExportClusterRequest.Types.CsvExportOptions csvExportOptions = new ExportClusterRequest.Types.CsvExportOptions();
    ExportClusterRequest.Types.SqlExportOptions sqlExportOptions = new ExportClusterRequest.Types.SqlExportOptions();
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ExportClusterAsync(name, gcsDestination, database, csvExportOptions, sqlExportOptions);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceExportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportClusterAsync(ClusterName, GcsDestination, string, CsvExportOptions, SqlExportOptions, CancellationToken)
    
    
    public virtual Task<Operation<ExportClusterResponse, OperationMetadata>> ExportClusterAsync(ClusterName name, GcsDestination gcsDestination, string database, ExportClusterRequest.Types.CsvExportOptions csvExportOptions, ExportClusterRequest.Types.SqlExportOptions sqlExportOptions, CancellationToken cancellationToken)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`gcsDestination` | `[GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GcsDestination)`  
Required. Option to export data to cloud storage.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the export command will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`csvExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[CsvExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.CsvExportOptions)`  
Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[SqlExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.SqlExportOptions)`  
Options for exporting data in SQL format. Required field to be set for SQL file type.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    GcsDestination gcsDestination = new GcsDestination();
    string database = "";
    ExportClusterRequest.Types.CsvExportOptions csvExportOptions = new ExportClusterRequest.Types.CsvExportOptions();
    ExportClusterRequest.Types.SqlExportOptions sqlExportOptions = new ExportClusterRequest.Types.SqlExportOptions();
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ExportClusterAsync(name, gcsDestination, database, csvExportOptions, sqlExportOptions);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceExportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportClusterAsync(ExportClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<ExportClusterResponse, OperationMetadata>> ExportClusterAsync(ExportClusterRequest request, CallSettings callSettings = null)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ExportClusterRequest request = new ExportClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        GcsDestination = new GcsDestination(),
        Database = "",
        CsvExportOptions = new ExportClusterRequest.Types.CsvExportOptions(),
    };
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ExportClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceExportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportClusterAsync(ExportClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<ExportClusterResponse, OperationMetadata>> ExportClusterAsync(ExportClusterRequest request, CancellationToken cancellationToken)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ExportClusterRequest request = new ExportClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        GcsDestination = new GcsDestination(),
        Database = "",
        CsvExportOptions = new ExportClusterRequest.Types.CsvExportOptions(),
    };
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ExportClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceExportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportClusterAsync(string, GcsDestination, string, CsvExportOptions, SqlExportOptions, CallSettings)
    
    
    public virtual Task<Operation<ExportClusterResponse, OperationMetadata>> ExportClusterAsync(string name, GcsDestination gcsDestination, string database, ExportClusterRequest.Types.CsvExportOptions csvExportOptions, ExportClusterRequest.Types.SqlExportOptions sqlExportOptions, CallSettings callSettings = null)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`gcsDestination` | `[GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GcsDestination)`  
Required. Option to export data to cloud storage.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the export command will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`csvExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[CsvExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.CsvExportOptions)`  
Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[SqlExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.SqlExportOptions)`  
Options for exporting data in SQL format. Required field to be set for SQL file type.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    GcsDestination gcsDestination = new GcsDestination();
    string database = "";
    ExportClusterRequest.Types.CsvExportOptions csvExportOptions = new ExportClusterRequest.Types.CsvExportOptions();
    ExportClusterRequest.Types.SqlExportOptions sqlExportOptions = new ExportClusterRequest.Types.SqlExportOptions();
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ExportClusterAsync(name, gcsDestination, database, csvExportOptions, sqlExportOptions);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceExportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportClusterAsync(string, GcsDestination, string, CsvExportOptions, SqlExportOptions, CancellationToken)
    
    
    public virtual Task<Operation<ExportClusterResponse, OperationMetadata>> ExportClusterAsync(string name, GcsDestination gcsDestination, string database, ExportClusterRequest.Types.CsvExportOptions csvExportOptions, ExportClusterRequest.Types.SqlExportOptions sqlExportOptions, CancellationToken cancellationToken)

Exports data from the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`gcsDestination` | `[GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GcsDestination)`  
Required. Option to export data to cloud storage.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the database where the export command will be executed. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`csvExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[CsvExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.CsvExportOptions)`  
Options for exporting data in CSV format. Required field to be set for CSV file type.  
`sqlExportOptions` | `[ExportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types)[SqlExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterRequest.Types.SqlExportOptions)`  
Options for exporting data in SQL format. Required field to be set for SQL file type.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    GcsDestination gcsDestination = new GcsDestination();
    string database = "";
    ExportClusterRequest.Types.CsvExportOptions csvExportOptions = new ExportClusterRequest.Types.CsvExportOptions();
    ExportClusterRequest.Types.SqlExportOptions sqlExportOptions = new ExportClusterRequest.Types.SqlExportOptions();
    // Make the request
    Operation<ExportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ExportClusterAsync(name, gcsDestination, database, csvExportOptions, sqlExportOptions);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceExportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstance(FailoverInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> FailoverInstance(FailoverInstanceRequest request, CallSettings callSettings = null)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.FailoverInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    FailoverInstanceRequest request = new FailoverInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.FailoverInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceFailoverInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstance(InstanceName, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> FailoverInstance(InstanceName name, CallSettings callSettings = null)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.FailoverInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceFailoverInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> FailoverInstance(string name, CallSettings callSettings = null)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.FailoverInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceFailoverInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstanceAsync(FailoverInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> FailoverInstanceAsync(FailoverInstanceRequest request, CallSettings callSettings = null)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.FailoverInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    FailoverInstanceRequest request = new FailoverInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.FailoverInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceFailoverInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstanceAsync(FailoverInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> FailoverInstanceAsync(FailoverInstanceRequest request, CancellationToken cancellationToken)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.FailoverInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    FailoverInstanceRequest request = new FailoverInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.FailoverInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceFailoverInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> FailoverInstanceAsync(InstanceName name, CallSettings callSettings = null)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.FailoverInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceFailoverInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> FailoverInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.FailoverInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceFailoverInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> FailoverInstanceAsync(string name, CallSettings callSettings = null)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.FailoverInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceFailoverInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### FailoverInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> FailoverInstanceAsync(string name, CancellationToken cancellationToken)

Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.FailoverInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceFailoverInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### GenerateClientCertificate(ClusterName, CallSettings)
    
    
    public virtual GenerateClientCertificateResponse GenerateClientCertificate(ClusterName parent, CallSettings callSettings = null)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}/clusters/{cluster}

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    GenerateClientCertificateResponse response = alloyDBAdminClient.GenerateClientCertificate(parent);
    

### GenerateClientCertificate(GenerateClientCertificateRequest, CallSettings)
    
    
    public virtual GenerateClientCertificateResponse GenerateClientCertificate(GenerateClientCertificateRequest request, CallSettings callSettings = null)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateClientCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    GenerateClientCertificateRequest request = new GenerateClientCertificateRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        CertDuration = new Duration(),
        PublicKey = "",
        UseMetadataExchange = false,
    };
    // Make the request
    GenerateClientCertificateResponse response = alloyDBAdminClient.GenerateClientCertificate(request);
    

### GenerateClientCertificate(string, CallSettings)
    
    
    public virtual GenerateClientCertificateResponse GenerateClientCertificate(string parent, CallSettings callSettings = null)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}/clusters/{cluster}

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    GenerateClientCertificateResponse response = alloyDBAdminClient.GenerateClientCertificate(parent);
    

### GenerateClientCertificateAsync(ClusterName, CallSettings)
    
    
    public virtual Task<GenerateClientCertificateResponse> GenerateClientCertificateAsync(ClusterName parent, CallSettings callSettings = null)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}/clusters/{cluster}

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    GenerateClientCertificateResponse response = await alloyDBAdminClient.GenerateClientCertificateAsync(parent);
    

### GenerateClientCertificateAsync(ClusterName, CancellationToken)
    
    
    public virtual Task<GenerateClientCertificateResponse> GenerateClientCertificateAsync(ClusterName parent, CancellationToken cancellationToken)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}/clusters/{cluster}

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    GenerateClientCertificateResponse response = await alloyDBAdminClient.GenerateClientCertificateAsync(parent);
    

### GenerateClientCertificateAsync(GenerateClientCertificateRequest, CallSettings)
    
    
    public virtual Task<GenerateClientCertificateResponse> GenerateClientCertificateAsync(GenerateClientCertificateRequest request, CallSettings callSettings = null)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateClientCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GenerateClientCertificateRequest request = new GenerateClientCertificateRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        CertDuration = new Duration(),
        PublicKey = "",
        UseMetadataExchange = false,
    };
    // Make the request
    GenerateClientCertificateResponse response = await alloyDBAdminClient.GenerateClientCertificateAsync(request);
    

### GenerateClientCertificateAsync(GenerateClientCertificateRequest, CancellationToken)
    
    
    public virtual Task<GenerateClientCertificateResponse> GenerateClientCertificateAsync(GenerateClientCertificateRequest request, CancellationToken cancellationToken)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateClientCertificateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GenerateClientCertificateRequest request = new GenerateClientCertificateRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        CertDuration = new Duration(),
        PublicKey = "",
        UseMetadataExchange = false,
    };
    // Make the request
    GenerateClientCertificateResponse response = await alloyDBAdminClient.GenerateClientCertificateAsync(request);
    

### GenerateClientCertificateAsync(string, CallSettings)
    
    
    public virtual Task<GenerateClientCertificateResponse> GenerateClientCertificateAsync(string parent, CallSettings callSettings = null)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}/clusters/{cluster}

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    GenerateClientCertificateResponse response = await alloyDBAdminClient.GenerateClientCertificateAsync(parent);
    

### GenerateClientCertificateAsync(string, CancellationToken)
    
    
    public virtual Task<GenerateClientCertificateResponse> GenerateClientCertificateAsync(string parent, CancellationToken cancellationToken)

Generate a client certificate signed by a Cluster CA. The sole purpose of this endpoint is to support AlloyDB connectors and the Auth Proxy client. The endpoint's behavior is subject to change without notice, so do not rely on its behavior remaining constant. Future changes will not break AlloyDB connectors or the Auth Proxy client.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}/clusters/{cluster}

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateClientCertificateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GenerateClientCertificateResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    GenerateClientCertificateResponse response = await alloyDBAdminClient.GenerateClientCertificateAsync(parent);
    

### GetBackup(BackupName, CallSettings)
    
    
    public virtual Backup GetBackup(BackupName name, CallSettings callSettings = null)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BackupName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]");
    // Make the request
    Backup response = alloyDBAdminClient.GetBackup(name);
    

### GetBackup(GetBackupRequest, CallSettings)
    
    
    public virtual Backup GetBackup(GetBackupRequest request, CallSettings callSettings = null)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    GetBackupRequest request = new GetBackupRequest
    {
        BackupName = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]"),
    };
    // Make the request
    Backup response = alloyDBAdminClient.GetBackup(request);
    

### GetBackup(string, CallSettings)
    
    
    public virtual Backup GetBackup(string name, CallSettings callSettings = null)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/backups/[BACKUP]";
    // Make the request
    Backup response = alloyDBAdminClient.GetBackup(name);
    

### GetBackupAsync(BackupName, CallSettings)
    
    
    public virtual Task<Backup> GetBackupAsync(BackupName name, CallSettings callSettings = null)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BackupName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]");
    // Make the request
    Backup response = await alloyDBAdminClient.GetBackupAsync(name);
    

### GetBackupAsync(BackupName, CancellationToken)
    
    
    public virtual Task<Backup> GetBackupAsync(BackupName name, CancellationToken cancellationToken)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BackupName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]");
    // Make the request
    Backup response = await alloyDBAdminClient.GetBackupAsync(name);
    

### GetBackupAsync(GetBackupRequest, CallSettings)
    
    
    public virtual Task<Backup> GetBackupAsync(GetBackupRequest request, CallSettings callSettings = null)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetBackupRequest request = new GetBackupRequest
    {
        BackupName = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]"),
    };
    // Make the request
    Backup response = await alloyDBAdminClient.GetBackupAsync(request);
    

### GetBackupAsync(GetBackupRequest, CancellationToken)
    
    
    public virtual Task<Backup> GetBackupAsync(GetBackupRequest request, CancellationToken cancellationToken)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetBackupRequest request = new GetBackupRequest
    {
        BackupName = BackupName.FromProjectLocationBackup("[PROJECT]", "[LOCATION]", "[BACKUP]"),
    };
    // Make the request
    Backup response = await alloyDBAdminClient.GetBackupAsync(request);
    

### GetBackupAsync(string, CallSettings)
    
    
    public virtual Task<Backup> GetBackupAsync(string name, CallSettings callSettings = null)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/backups/[BACKUP]";
    // Make the request
    Backup response = await alloyDBAdminClient.GetBackupAsync(name);
    

### GetBackupAsync(string, CancellationToken)
    
    
    public virtual Task<Backup> GetBackupAsync(string name, CancellationToken cancellationToken)

Gets details of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/backups/[BACKUP]";
    // Make the request
    Backup response = await alloyDBAdminClient.GetBackupAsync(name);
    

### GetCluster(ClusterName, CallSettings)
    
    
    public virtual Cluster GetCluster(ClusterName name, CallSettings callSettings = null)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Cluster response = alloyDBAdminClient.GetCluster(name);
    

### GetCluster(GetClusterRequest, CallSettings)
    
    
    public virtual Cluster GetCluster(GetClusterRequest request, CallSettings callSettings = null)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    GetClusterRequest request = new GetClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        View = ClusterView.Unspecified,
    };
    // Make the request
    Cluster response = alloyDBAdminClient.GetCluster(request);
    

### GetCluster(string, CallSettings)
    
    
    public virtual Cluster GetCluster(string name, CallSettings callSettings = null)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Cluster response = alloyDBAdminClient.GetCluster(name);
    

### GetClusterAsync(ClusterName, CallSettings)
    
    
    public virtual Task<Cluster> GetClusterAsync(ClusterName name, CallSettings callSettings = null)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Cluster response = await alloyDBAdminClient.GetClusterAsync(name);
    

### GetClusterAsync(ClusterName, CancellationToken)
    
    
    public virtual Task<Cluster> GetClusterAsync(ClusterName name, CancellationToken cancellationToken)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Cluster response = await alloyDBAdminClient.GetClusterAsync(name);
    

### GetClusterAsync(GetClusterRequest, CallSettings)
    
    
    public virtual Task<Cluster> GetClusterAsync(GetClusterRequest request, CallSettings callSettings = null)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetClusterRequest request = new GetClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        View = ClusterView.Unspecified,
    };
    // Make the request
    Cluster response = await alloyDBAdminClient.GetClusterAsync(request);
    

### GetClusterAsync(GetClusterRequest, CancellationToken)
    
    
    public virtual Task<Cluster> GetClusterAsync(GetClusterRequest request, CancellationToken cancellationToken)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetClusterRequest request = new GetClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        View = ClusterView.Unspecified,
    };
    // Make the request
    Cluster response = await alloyDBAdminClient.GetClusterAsync(request);
    

### GetClusterAsync(string, CallSettings)
    
    
    public virtual Task<Cluster> GetClusterAsync(string name, CallSettings callSettings = null)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Cluster response = await alloyDBAdminClient.GetClusterAsync(name);
    

### GetClusterAsync(string, CancellationToken)
    
    
    public virtual Task<Cluster> GetClusterAsync(string name, CancellationToken cancellationToken)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Cluster response = await alloyDBAdminClient.GetClusterAsync(name);
    

### GetConnectionInfo(GetConnectionInfoRequest, CallSettings)
    
    
    public virtual ConnectionInfo GetConnectionInfo(GetConnectionInfoRequest request, CallSettings callSettings = null)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetConnectionInfoRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    GetConnectionInfoRequest request = new GetConnectionInfoRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
    };
    // Make the request
    ConnectionInfo response = alloyDBAdminClient.GetConnectionInfo(request);
    

### GetConnectionInfo(InstanceName, CallSettings)
    
    
    public virtual ConnectionInfo GetConnectionInfo(InstanceName parent, CallSettings callSettings = null)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    ConnectionInfo response = alloyDBAdminClient.GetConnectionInfo(parent);
    

### GetConnectionInfo(string, CallSettings)
    
    
    public virtual ConnectionInfo GetConnectionInfo(string parent, CallSettings callSettings = null)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    ConnectionInfo response = alloyDBAdminClient.GetConnectionInfo(parent);
    

### GetConnectionInfoAsync(GetConnectionInfoRequest, CallSettings)
    
    
    public virtual Task<ConnectionInfo> GetConnectionInfoAsync(GetConnectionInfoRequest request, CallSettings callSettings = null)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetConnectionInfoRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetConnectionInfoRequest request = new GetConnectionInfoRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
    };
    // Make the request
    ConnectionInfo response = await alloyDBAdminClient.GetConnectionInfoAsync(request);
    

### GetConnectionInfoAsync(GetConnectionInfoRequest, CancellationToken)
    
    
    public virtual Task<ConnectionInfo> GetConnectionInfoAsync(GetConnectionInfoRequest request, CancellationToken cancellationToken)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetConnectionInfoRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetConnectionInfoRequest request = new GetConnectionInfoRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
    };
    // Make the request
    ConnectionInfo response = await alloyDBAdminClient.GetConnectionInfoAsync(request);
    

### GetConnectionInfoAsync(InstanceName, CallSettings)
    
    
    public virtual Task<ConnectionInfo> GetConnectionInfoAsync(InstanceName parent, CallSettings callSettings = null)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    ConnectionInfo response = await alloyDBAdminClient.GetConnectionInfoAsync(parent);
    

### GetConnectionInfoAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<ConnectionInfo> GetConnectionInfoAsync(InstanceName parent, CancellationToken cancellationToken)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    ConnectionInfo response = await alloyDBAdminClient.GetConnectionInfoAsync(parent);
    

### GetConnectionInfoAsync(string, CallSettings)
    
    
    public virtual Task<ConnectionInfo> GetConnectionInfoAsync(string parent, CallSettings callSettings = null)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    ConnectionInfo response = await alloyDBAdminClient.GetConnectionInfoAsync(parent);
    

### GetConnectionInfoAsync(string, CancellationToken)
    
    
    public virtual Task<ConnectionInfo> GetConnectionInfoAsync(string parent, CancellationToken cancellationToken)

Get instance metadata used for a connection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. The required format is: projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ConnectionInfo)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    ConnectionInfo response = await alloyDBAdminClient.GetConnectionInfoAsync(parent);
    

### GetInstance(GetInstanceRequest, CallSettings)
    
    
    public virtual Instance GetInstance(GetInstanceRequest request, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        View = InstanceView.Unspecified,
    };
    // Make the request
    Instance response = alloyDBAdminClient.GetInstance(request);
    

### GetInstance(InstanceName, CallSettings)
    
    
    public virtual Instance GetInstance(InstanceName name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Instance response = alloyDBAdminClient.GetInstance(name);
    

### GetInstance(string, CallSettings)
    
    
    public virtual Instance GetInstance(string name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Instance response = alloyDBAdminClient.GetInstance(name);
    

### GetInstanceAsync(GetInstanceRequest, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(GetInstanceRequest request, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        View = InstanceView.Unspecified,
    };
    // Make the request
    Instance response = await alloyDBAdminClient.GetInstanceAsync(request);
    

### GetInstanceAsync(GetInstanceRequest, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(GetInstanceRequest request, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        View = InstanceView.Unspecified,
    };
    // Make the request
    Instance response = await alloyDBAdminClient.GetInstanceAsync(request);
    

### GetInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(InstanceName name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Instance response = await alloyDBAdminClient.GetInstanceAsync(name);
    

### GetInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Instance response = await alloyDBAdminClient.GetInstanceAsync(name);
    

### GetInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(string name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Instance response = await alloyDBAdminClient.GetInstanceAsync(name);
    

### GetInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(string name, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Instance response = await alloyDBAdminClient.GetInstanceAsync(name);
    

### GetUser(GetUserRequest, CallSettings)
    
    
    public virtual User GetUser(GetUserRequest request, CallSettings callSettings = null)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetUserRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    GetUserRequest request = new GetUserRequest
    {
        UserName = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]"),
    };
    // Make the request
    User response = alloyDBAdminClient.GetUser(request);
    

### GetUser(UserName, CallSettings)
    
    
    public virtual User GetUser(UserName name, CallSettings callSettings = null)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UserName)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    UserName name = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]");
    // Make the request
    User response = alloyDBAdminClient.GetUser(name);
    

### GetUser(string, CallSettings)
    
    
    public virtual User GetUser(string name, CallSettings callSettings = null)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/users/[USER]";
    // Make the request
    User response = alloyDBAdminClient.GetUser(name);
    

### GetUserAsync(GetUserRequest, CallSettings)
    
    
    public virtual Task<User> GetUserAsync(GetUserRequest request, CallSettings callSettings = null)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetUserRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetUserRequest request = new GetUserRequest
    {
        UserName = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]"),
    };
    // Make the request
    User response = await alloyDBAdminClient.GetUserAsync(request);
    

### GetUserAsync(GetUserRequest, CancellationToken)
    
    
    public virtual Task<User> GetUserAsync(GetUserRequest request, CancellationToken cancellationToken)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GetUserRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    GetUserRequest request = new GetUserRequest
    {
        UserName = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]"),
    };
    // Make the request
    User response = await alloyDBAdminClient.GetUserAsync(request);
    

### GetUserAsync(UserName, CallSettings)
    
    
    public virtual Task<User> GetUserAsync(UserName name, CallSettings callSettings = null)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UserName)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UserName name = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]");
    // Make the request
    User response = await alloyDBAdminClient.GetUserAsync(name);
    

### GetUserAsync(UserName, CancellationToken)
    
    
    public virtual Task<User> GetUserAsync(UserName name, CancellationToken cancellationToken)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UserName)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UserName name = UserName.FromProjectLocationClusterUser("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[USER]");
    // Make the request
    User response = await alloyDBAdminClient.GetUserAsync(name);
    

### GetUserAsync(string, CallSettings)
    
    
    public virtual Task<User> GetUserAsync(string name, CallSettings callSettings = null)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/users/[USER]";
    // Make the request
    User response = await alloyDBAdminClient.GetUserAsync(name);
    

### GetUserAsync(string, CancellationToken)
    
    
    public virtual Task<User> GetUserAsync(string name, CancellationToken cancellationToken)

Gets details of a single User.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the User.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/users/[USER]";
    // Make the request
    User response = await alloyDBAdminClient.GetUserAsync(name);
    

### ImportCluster(ClusterName, string, string, string, CallSettings)
    
    
    public virtual Operation<ImportClusterResponse, OperationMetadata> ImportCluster(ClusterName name, string gcsUri, string database, string user, CallSettings callSettings = null)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`gcsUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    string gcsUri = "";
    string database = "";
    string user = "";
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = alloyDBAdminClient.ImportCluster(name, gcsUri, database, user);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceImportCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportCluster(ImportClusterRequest, CallSettings)
    
    
    public virtual Operation<ImportClusterResponse, OperationMetadata> ImportCluster(ImportClusterRequest request, CallSettings callSettings = null)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ImportClusterRequest request = new ImportClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        GcsUri = "",
        Database = "",
        SqlImportOptions = new ImportClusterRequest.Types.SqlImportOptions(),
        User = "",
    };
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = alloyDBAdminClient.ImportCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceImportCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportCluster(string, string, string, string, CallSettings)
    
    
    public virtual Operation<ImportClusterResponse, OperationMetadata> ImportCluster(string name, string gcsUri, string database, string user, CallSettings callSettings = null)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`gcsUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    string gcsUri = "";
    string database = "";
    string user = "";
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = alloyDBAdminClient.ImportCluster(name, gcsUri, database, user);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceImportCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportClusterAsync(ClusterName, string, string, string, CallSettings)
    
    
    public virtual Task<Operation<ImportClusterResponse, OperationMetadata>> ImportClusterAsync(ClusterName name, string gcsUri, string database, string user, CallSettings callSettings = null)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`gcsUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    string gcsUri = "";
    string database = "";
    string user = "";
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ImportClusterAsync(name, gcsUri, database, user);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceImportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportClusterAsync(ClusterName, string, string, string, CancellationToken)
    
    
    public virtual Task<Operation<ImportClusterResponse, OperationMetadata>> ImportClusterAsync(ClusterName name, string gcsUri, string database, string user, CancellationToken cancellationToken)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`gcsUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    string gcsUri = "";
    string database = "";
    string user = "";
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ImportClusterAsync(name, gcsUri, database, user);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceImportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportClusterAsync(ImportClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportClusterResponse, OperationMetadata>> ImportClusterAsync(ImportClusterRequest request, CallSettings callSettings = null)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ImportClusterRequest request = new ImportClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        GcsUri = "",
        Database = "",
        SqlImportOptions = new ImportClusterRequest.Types.SqlImportOptions(),
        User = "",
    };
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ImportClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceImportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportClusterAsync(ImportClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportClusterResponse, OperationMetadata>> ImportClusterAsync(ImportClusterRequest request, CancellationToken cancellationToken)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ImportClusterRequest request = new ImportClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        GcsUri = "",
        Database = "",
        SqlImportOptions = new ImportClusterRequest.Types.SqlImportOptions(),
        User = "",
    };
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ImportClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceImportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportClusterAsync(string, string, string, string, CallSettings)
    
    
    public virtual Task<Operation<ImportClusterResponse, OperationMetadata>> ImportClusterAsync(string name, string gcsUri, string database, string user, CallSettings callSettings = null)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`gcsUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    string gcsUri = "";
    string database = "";
    string user = "";
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ImportClusterAsync(name, gcsUri, database, user);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceImportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportClusterAsync(string, string, string, string, CancellationToken)
    
    
    public virtual Task<Operation<ImportClusterResponse, OperationMetadata>> ImportClusterAsync(string name, string gcsUri, string database, string user, CancellationToken cancellationToken)

Imports data to the cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`gcsUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The path to the file in Google Cloud Storage where the source file for import will be stored. The URI is in the form `gs://bucketName/fileName`.  
`database` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Name of the database to which the import will be done. For import from SQL file, this is required only if the file does not specify a database. Note - Value provided should be the same as expected from `SELECT current_database();` and NOT as a resource reference.  
`user` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Database user to be used for importing the data. Note - Value provided should be the same as expected from `SELECT current_user;` and NOT as a resource reference.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    string gcsUri = "";
    string database = "";
    string user = "";
    // Make the request
    Operation<ImportClusterResponse, OperationMetadata> response = await alloyDBAdminClient.ImportClusterAsync(name, gcsUri, database, user);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceImportClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### InjectFault(InjectFaultRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> InjectFault(InjectFaultRequest request, CallSettings callSettings = null)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InjectFaultRequest request = new InjectFaultRequest
    {
        FaultType = InjectFaultRequest.Types.FaultType.Unspecified,
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.InjectFault(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceInjectFault(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### InjectFault(FaultType, InstanceName, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> InjectFault(InjectFaultRequest.Types.FaultType faultType, InstanceName name, CallSettings callSettings = null)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`faultType` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types)[FaultType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types.FaultType)`  
Required. The type of fault to be injected in an instance.  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InjectFaultRequest.Types.FaultType faultType = InjectFaultRequest.Types.FaultType.Unspecified;
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.InjectFault(faultType, name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceInjectFault(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### InjectFault(FaultType, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> InjectFault(InjectFaultRequest.Types.FaultType faultType, string name, CallSettings callSettings = null)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`faultType` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types)[FaultType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types.FaultType)`  
Required. The type of fault to be injected in an instance.  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InjectFaultRequest.Types.FaultType faultType = InjectFaultRequest.Types.FaultType.Unspecified;
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.InjectFault(faultType, name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceInjectFault(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### InjectFaultAsync(InjectFaultRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> InjectFaultAsync(InjectFaultRequest request, CallSettings callSettings = null)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InjectFaultRequest request = new InjectFaultRequest
    {
        FaultType = InjectFaultRequest.Types.FaultType.Unspecified,
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.InjectFaultAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceInjectFaultAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### InjectFaultAsync(InjectFaultRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> InjectFaultAsync(InjectFaultRequest request, CancellationToken cancellationToken)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InjectFaultRequest request = new InjectFaultRequest
    {
        FaultType = InjectFaultRequest.Types.FaultType.Unspecified,
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.InjectFaultAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceInjectFaultAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### InjectFaultAsync(FaultType, InstanceName, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> InjectFaultAsync(InjectFaultRequest.Types.FaultType faultType, InstanceName name, CallSettings callSettings = null)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`faultType` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types)[FaultType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types.FaultType)`  
Required. The type of fault to be injected in an instance.  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InjectFaultRequest.Types.FaultType faultType = InjectFaultRequest.Types.FaultType.Unspecified;
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.InjectFaultAsync(faultType, name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceInjectFaultAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### InjectFaultAsync(FaultType, InstanceName, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> InjectFaultAsync(InjectFaultRequest.Types.FaultType faultType, InstanceName name, CancellationToken cancellationToken)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`faultType` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types)[FaultType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types.FaultType)`  
Required. The type of fault to be injected in an instance.  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InjectFaultRequest.Types.FaultType faultType = InjectFaultRequest.Types.FaultType.Unspecified;
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.InjectFaultAsync(faultType, name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceInjectFaultAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### InjectFaultAsync(FaultType, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> InjectFaultAsync(InjectFaultRequest.Types.FaultType faultType, string name, CallSettings callSettings = null)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`faultType` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types)[FaultType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types.FaultType)`  
Required. The type of fault to be injected in an instance.  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InjectFaultRequest.Types.FaultType faultType = InjectFaultRequest.Types.FaultType.Unspecified;
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.InjectFaultAsync(faultType, name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceInjectFaultAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### InjectFaultAsync(FaultType, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> InjectFaultAsync(InjectFaultRequest.Types.FaultType faultType, string name, CancellationToken cancellationToken)

Injects fault in an instance. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`faultType` | `[InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types)[FaultType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InjectFaultRequest.Types.FaultType)`  
Required. The type of fault to be injected in an instance.  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InjectFaultRequest.Types.FaultType faultType = InjectFaultRequest.Types.FaultType.Unspecified;
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.InjectFaultAsync(faultType, name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceInjectFaultAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ListBackups(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListBackupsResponse, Backup> ListBackups(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Backups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListBackupsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A pageable sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListBackupsResponse, Backup> response = alloyDBAdminClient.ListBackups(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Backup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListBackupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Backup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Backup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListBackups(ListBackupsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListBackupsResponse, Backup> ListBackups(ListBackupsRequest request, CallSettings callSettings = null)

Lists Backups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A pageable sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ListBackupsRequest request = new ListBackupsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListBackupsResponse, Backup> response = alloyDBAdminClient.ListBackups(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Backup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListBackupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Backup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Backup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListBackups(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListBackupsResponse, Backup> ListBackups(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Backups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListBackupsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A pageable sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListBackupsResponse, Backup> response = alloyDBAdminClient.ListBackups(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Backup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListBackupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Backup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Backup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListBackupsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListBackupsResponse, Backup> ListBackupsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Backups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListBackupsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A pageable asynchronous sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListBackupsResponse, Backup> response = alloyDBAdminClient.ListBackupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Backup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListBackupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Backup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Backup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListBackupsAsync(ListBackupsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListBackupsResponse, Backup> ListBackupsAsync(ListBackupsRequest request, CallSettings callSettings = null)

Lists Backups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A pageable asynchronous sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ListBackupsRequest request = new ListBackupsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListBackupsResponse, Backup> response = alloyDBAdminClient.ListBackupsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Backup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListBackupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Backup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Backup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListBackupsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListBackupsResponse, Backup> ListBackupsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Backups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListBackupsRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)` | A pageable asynchronous sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListBackupsResponse, Backup> response = alloyDBAdminClient.ListBackupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Backup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListBackupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Backup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Backup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClusters(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListClustersResponse, Cluster> ListClusters(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format:

  * projects/{project}/locations/-

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A pageable sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListClustersResponse, Cluster> response = alloyDBAdminClient.ListClusters(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClusters(ListClustersRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListClustersResponse, Cluster> ListClusters(ListClustersRequest request, CallSettings callSettings = null)

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListClustersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A pageable sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ListClustersRequest request = new ListClustersRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListClustersResponse, Cluster> response = alloyDBAdminClient.ListClusters(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClusters(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListClustersResponse, Cluster> ListClusters(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format:

  * projects/{project}/locations/-

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A pageable sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListClustersResponse, Cluster> response = alloyDBAdminClient.ListClusters(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClustersAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListClustersResponse, Cluster> ListClustersAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format:

  * projects/{project}/locations/-

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A pageable asynchronous sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListClustersResponse, Cluster> response = alloyDBAdminClient.ListClustersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClustersAsync(ListClustersRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListClustersResponse, Cluster> ListClustersAsync(ListClustersRequest request, CallSettings callSettings = null)

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListClustersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A pageable asynchronous sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ListClustersRequest request = new ListClustersRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListClustersResponse, Cluster> response = alloyDBAdminClient.ListClustersAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClustersAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListClustersResponse, Cluster> ListClustersAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format:

  * projects/{project}/locations/-

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)` | A pageable asynchronous sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListClustersResponse, Cluster> response = alloyDBAdminClient.ListClustersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDatabases(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDatabasesResponse, Database> ListDatabases(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Parent value for ListDatabasesRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListDatabasesResponse)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A pageable sequence of [Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedEnumerable<ListDatabasesResponse, Database> response = alloyDBAdminClient.ListDatabases(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Database item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDatabasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Database item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Database> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Database item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDatabases(ListDatabasesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDatabasesResponse, Database> ListDatabases(ListDatabasesRequest request, CallSettings callSettings = null)

Lists Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListDatabasesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListDatabasesResponse)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A pageable sequence of [Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ListDatabasesRequest request = new ListDatabasesRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListDatabasesResponse, Database> response = alloyDBAdminClient.ListDatabases(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Database item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDatabasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Database item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Database> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Database item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDatabases(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDatabasesResponse, Database> ListDatabases(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListDatabasesRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListDatabasesResponse)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A pageable sequence of [Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedEnumerable<ListDatabasesResponse, Database> response = alloyDBAdminClient.ListDatabases(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Database item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDatabasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Database item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Database> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Database item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDatabasesAsync(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDatabasesResponse, Database> ListDatabasesAsync(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Parent value for ListDatabasesRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListDatabasesResponse)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A pageable asynchronous sequence of [Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedAsyncEnumerable<ListDatabasesResponse, Database> response = alloyDBAdminClient.ListDatabasesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Database item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDatabasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Database item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Database> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Database item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDatabasesAsync(ListDatabasesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDatabasesResponse, Database> ListDatabasesAsync(ListDatabasesRequest request, CallSettings callSettings = null)

Lists Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListDatabasesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListDatabasesResponse)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A pageable asynchronous sequence of [Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ListDatabasesRequest request = new ListDatabasesRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListDatabasesResponse, Database> response = alloyDBAdminClient.ListDatabasesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Database item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDatabasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Database item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Database> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Database item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDatabasesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDatabasesResponse, Database> ListDatabasesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Databases in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListDatabasesRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDatabasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListDatabasesResponse)[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database)` | A pageable asynchronous sequence of [Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Database) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedAsyncEnumerable<ListDatabasesResponse, Database> response = alloyDBAdminClient.ListDatabasesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Database item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDatabasesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Database item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Database> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Database item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstances(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListInstancesResponse, Instance> ListInstances(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. Additionally, you can perform an aggregated list operation by specifying a value with one of the following formats:

  * projects/{project}/locations/-/clusters/-
  * projects/{project}/locations/{region}/clusters/-

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = alloyDBAdminClient.ListInstances(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstances(ListInstancesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListInstancesResponse, Instance> ListInstances(ListInstancesRequest request, CallSettings callSettings = null)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ListInstancesRequest request = new ListInstancesRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = alloyDBAdminClient.ListInstances(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstances(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListInstancesResponse, Instance> ListInstances(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. Additionally, you can perform an aggregated list operation by specifying a value with one of the following formats:

  * projects/{project}/locations/-/clusters/-
  * projects/{project}/locations/{region}/clusters/-

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = alloyDBAdminClient.ListInstances(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstancesAsync(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInstancesResponse, Instance> ListInstancesAsync(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. Additionally, you can perform an aggregated list operation by specifying a value with one of the following formats:

  * projects/{project}/locations/-/clusters/-
  * projects/{project}/locations/{region}/clusters/-

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = alloyDBAdminClient.ListInstancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstancesAsync(ListInstancesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInstancesResponse, Instance> ListInstancesAsync(ListInstancesRequest request, CallSettings callSettings = null)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ListInstancesRequest request = new ListInstancesRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = alloyDBAdminClient.ListInstancesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstancesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInstancesResponse, Instance> ListInstancesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. Additionally, you can perform an aggregated list operation by specifying a value with one of the following formats:

  * projects/{project}/locations/-/clusters/-
  * projects/{project}/locations/{region}/clusters/-

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = alloyDBAdminClient.ListInstancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSupportedDatabaseFlags(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> ListSupportedDatabaseFlags(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SupportedDatabaseFlags for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}

Regardless of the parent specified here, as long it is contains a valid project and location, the service will return a static list of supported flags resources. Note that we do not yet support region-specific flags.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListSupportedDatabaseFlagsResponse)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag)` | A pageable sequence of [SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> response = alloyDBAdminClient.ListSupportedDatabaseFlags(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SupportedDatabaseFlag item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSupportedDatabaseFlagsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SupportedDatabaseFlag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SupportedDatabaseFlag> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SupportedDatabaseFlag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSupportedDatabaseFlags(ListSupportedDatabaseFlagsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> ListSupportedDatabaseFlags(ListSupportedDatabaseFlagsRequest request, CallSettings callSettings = null)

Lists SupportedDatabaseFlags for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListSupportedDatabaseFlagsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListSupportedDatabaseFlagsResponse)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag)` | A pageable sequence of [SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ListSupportedDatabaseFlagsRequest request = new ListSupportedDatabaseFlagsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Scope = SupportedDatabaseFlag.Types.Scope.Unspecified,
    };
    // Make the request
    PagedEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> response = alloyDBAdminClient.ListSupportedDatabaseFlags(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SupportedDatabaseFlag item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSupportedDatabaseFlagsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SupportedDatabaseFlag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SupportedDatabaseFlag> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SupportedDatabaseFlag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSupportedDatabaseFlags(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> ListSupportedDatabaseFlags(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SupportedDatabaseFlags for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}

Regardless of the parent specified here, as long it is contains a valid project and location, the service will return a static list of supported flags resources. Note that we do not yet support region-specific flags.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListSupportedDatabaseFlagsResponse)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag)` | A pageable sequence of [SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> response = alloyDBAdminClient.ListSupportedDatabaseFlags(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SupportedDatabaseFlag item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSupportedDatabaseFlagsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SupportedDatabaseFlag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SupportedDatabaseFlag> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SupportedDatabaseFlag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSupportedDatabaseFlagsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> ListSupportedDatabaseFlagsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SupportedDatabaseFlags for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}

Regardless of the parent specified here, as long it is contains a valid project and location, the service will return a static list of supported flags resources. Note that we do not yet support region-specific flags.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListSupportedDatabaseFlagsResponse)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag)` | A pageable asynchronous sequence of [SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> response = alloyDBAdminClient.ListSupportedDatabaseFlagsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SupportedDatabaseFlag item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSupportedDatabaseFlagsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SupportedDatabaseFlag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SupportedDatabaseFlag> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SupportedDatabaseFlag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSupportedDatabaseFlagsAsync(ListSupportedDatabaseFlagsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> ListSupportedDatabaseFlagsAsync(ListSupportedDatabaseFlagsRequest request, CallSettings callSettings = null)

Lists SupportedDatabaseFlags for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListSupportedDatabaseFlagsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListSupportedDatabaseFlagsResponse)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag)` | A pageable asynchronous sequence of [SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ListSupportedDatabaseFlagsRequest request = new ListSupportedDatabaseFlagsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Scope = SupportedDatabaseFlag.Types.Scope.Unspecified,
    };
    // Make the request
    PagedAsyncEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> response = alloyDBAdminClient.ListSupportedDatabaseFlagsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SupportedDatabaseFlag item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSupportedDatabaseFlagsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SupportedDatabaseFlag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SupportedDatabaseFlag> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SupportedDatabaseFlag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSupportedDatabaseFlagsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> ListSupportedDatabaseFlagsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SupportedDatabaseFlags for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource. The required format is:

  * projects/{project}/locations/{location}

Regardless of the parent specified here, as long it is contains a valid project and location, the service will return a static list of supported flags resources. Note that we do not yet support region-specific flags.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListSupportedDatabaseFlagsResponse)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag)` | A pageable asynchronous sequence of [SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SupportedDatabaseFlag) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListSupportedDatabaseFlagsResponse, SupportedDatabaseFlag> response = alloyDBAdminClient.ListSupportedDatabaseFlagsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SupportedDatabaseFlag item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSupportedDatabaseFlagsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SupportedDatabaseFlag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SupportedDatabaseFlag> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SupportedDatabaseFlag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUsers(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUsersResponse, User> ListUsers(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Users in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Parent value for ListUsersRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUsersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListUsersResponse)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A pageable sequence of [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedEnumerable<ListUsersResponse, User> response = alloyDBAdminClient.ListUsers(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (User item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUsersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (User item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<User> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (User item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUsers(ListUsersRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListUsersResponse, User> ListUsers(ListUsersRequest request, CallSettings callSettings = null)

Lists Users in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListUsersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUsersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListUsersResponse)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A pageable sequence of [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ListUsersRequest request = new ListUsersRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListUsersResponse, User> response = alloyDBAdminClient.ListUsers(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (User item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUsersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (User item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<User> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (User item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUsers(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUsersResponse, User> ListUsers(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Users in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListUsersRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUsersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListUsersResponse)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A pageable sequence of [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedEnumerable<ListUsersResponse, User> response = alloyDBAdminClient.ListUsers(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (User item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListUsersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (User item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<User> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (User item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUsersAsync(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUsersResponse, User> ListUsersAsync(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Users in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. Parent value for ListUsersRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUsersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListUsersResponse)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A pageable asynchronous sequence of [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedAsyncEnumerable<ListUsersResponse, User> response = alloyDBAdminClient.ListUsersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (User item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUsersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (User item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<User> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (User item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUsersAsync(ListUsersRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUsersResponse, User> ListUsersAsync(ListUsersRequest request, CallSettings callSettings = null)

Lists Users in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListUsersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUsersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListUsersResponse)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A pageable asynchronous sequence of [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ListUsersRequest request = new ListUsersRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListUsersResponse, User> response = alloyDBAdminClient.ListUsersAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (User item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUsersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (User item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<User> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (User item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUsersAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUsersResponse, User> ListUsersAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Users in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListUsersRequest  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUsersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ListUsersResponse)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A pageable asynchronous sequence of [User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User) resources.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedAsyncEnumerable<ListUsersResponse, User> response = alloyDBAdminClient.ListUsersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (User item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListUsersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (User item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<User> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (User item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceBatchCreateInstances(string, CallSettings)
    
    
    public virtual Operation<BatchCreateInstancesResponse, OperationMetadata> PollOnceBatchCreateInstances(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `BatchCreateInstances` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceBatchCreateInstancesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateInstancesResponse, OperationMetadata>> PollOnceBatchCreateInstancesAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `BatchCreateInstances`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BatchCreateInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateBackup(string, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> PollOnceCreateBackup(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateBackup`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateBackupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> PollOnceCreateBackupAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateBackup`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOnceCreateCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOnceCreateClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceCreateInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceCreateInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateSecondaryCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOnceCreateSecondaryCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateSecondaryCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateSecondaryClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOnceCreateSecondaryClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateSecondaryCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateSecondaryInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceCreateSecondaryInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateSecondaryInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateSecondaryInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceCreateSecondaryInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateSecondaryInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteBackup(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteBackup(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteBackup`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteBackupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteBackupAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteBackup`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteCluster(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteInstance(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceExportCluster(string, CallSettings)
    
    
    public virtual Operation<ExportClusterResponse, OperationMetadata> PollOnceExportCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ExportCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceExportClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ExportClusterResponse, OperationMetadata>> PollOnceExportClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ExportCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceFailoverInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceFailoverInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `FailoverInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceFailoverInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceFailoverInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `FailoverInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceImportCluster(string, CallSettings)
    
    
    public virtual Operation<ImportClusterResponse, OperationMetadata> PollOnceImportCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceImportClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportClusterResponse, OperationMetadata>> PollOnceImportClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ImportClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceInjectFault(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceInjectFault(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `InjectFault`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceInjectFaultAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceInjectFaultAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `InjectFault`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOncePromoteCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOncePromoteCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `PromoteCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOncePromoteClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOncePromoteClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `PromoteCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRestartInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceRestartInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RestartInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRestartInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceRestartInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RestartInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRestoreCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOnceRestoreCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RestoreCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRestoreClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOnceRestoreClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RestoreCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceSwitchoverCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOnceSwitchoverCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `SwitchoverCluster` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceSwitchoverClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOnceSwitchoverClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `SwitchoverCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateBackup(string, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> PollOnceUpdateBackup(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateBackup`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateBackupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> PollOnceUpdateBackupAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateBackup`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOnceUpdateCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOnceUpdateClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceUpdateInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceUpdateInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpgradeCluster(string, CallSettings)
    
    
    public virtual Operation<UpgradeClusterResponse, OperationMetadata> PollOnceUpgradeCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpgradeCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpgradeClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<UpgradeClusterResponse, OperationMetadata>> PollOnceUpgradeClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpgradeCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PromoteCluster(ClusterName, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PromoteCluster(ClusterName name, CallSettings callSettings = null)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.PromoteCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOncePromoteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### PromoteCluster(PromoteClusterRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PromoteCluster(PromoteClusterRequest request, CallSettings callSettings = null)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PromoteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.PromoteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    PromoteClusterRequest request = new PromoteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.PromoteCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOncePromoteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### PromoteCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PromoteCluster(string name, CallSettings callSettings = null)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.PromoteCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOncePromoteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### PromoteClusterAsync(ClusterName, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PromoteClusterAsync(ClusterName name, CallSettings callSettings = null)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.PromoteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOncePromoteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### PromoteClusterAsync(ClusterName, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PromoteClusterAsync(ClusterName name, CancellationToken cancellationToken)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.PromoteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOncePromoteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### PromoteClusterAsync(PromoteClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PromoteClusterAsync(PromoteClusterRequest request, CallSettings callSettings = null)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PromoteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.PromoteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    PromoteClusterRequest request = new PromoteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.PromoteClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOncePromoteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### PromoteClusterAsync(PromoteClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PromoteClusterAsync(PromoteClusterRequest request, CancellationToken cancellationToken)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PromoteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.PromoteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    PromoteClusterRequest request = new PromoteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        Etag = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.PromoteClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOncePromoteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### PromoteClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PromoteClusterAsync(string name, CallSettings callSettings = null)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.PromoteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOncePromoteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### PromoteClusterAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PromoteClusterAsync(string name, CancellationToken cancellationToken)

Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.PromoteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOncePromoteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstance(InstanceName, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RestartInstance(InstanceName name, CallSettings callSettings = null)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.RestartInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceRestartInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstance(RestartInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RestartInstance(RestartInstanceRequest request, CallSettings callSettings = null)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestartInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    RestartInstanceRequest request = new RestartInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
        NodeIds = { "", },
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.RestartInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceRestartInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RestartInstance(string name, CallSettings callSettings = null)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.RestartInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceRestartInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RestartInstanceAsync(InstanceName name, CallSettings callSettings = null)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.RestartInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceRestartInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RestartInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.InstanceName)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]");
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.RestartInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceRestartInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstanceAsync(RestartInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RestartInstanceAsync(RestartInstanceRequest request, CallSettings callSettings = null)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestartInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    RestartInstanceRequest request = new RestartInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
        NodeIds = { "", },
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.RestartInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceRestartInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstanceAsync(RestartInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RestartInstanceAsync(RestartInstanceRequest request, CancellationToken cancellationToken)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestartInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    RestartInstanceRequest request = new RestartInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationClusterInstance("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[INSTANCE]"),
        RequestId = "",
        ValidateOnly = false,
        NodeIds = { "", },
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.RestartInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceRestartInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RestartInstanceAsync(string name, CallSettings callSettings = null)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.RestartInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceRestartInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestartInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RestartInstanceAsync(string name, CancellationToken cancellationToken)

Restart an Instance in a cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Instance.name field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.RestartInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceRestartInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RestoreCluster(RestoreClusterRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> RestoreCluster(RestoreClusterRequest request, CallSettings callSettings = null)

Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestoreClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    RestoreClusterRequest request = new RestoreClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        BackupSource = new BackupSource(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.RestoreCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceRestoreCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreClusterAsync(RestoreClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> RestoreClusterAsync(RestoreClusterRequest request, CallSettings callSettings = null)

Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestoreClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    RestoreClusterRequest request = new RestoreClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        BackupSource = new BackupSource(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.RestoreClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceRestoreClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreClusterAsync(RestoreClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> RestoreClusterAsync(RestoreClusterRequest request, CancellationToken cancellationToken)

Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestoreClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    RestoreClusterRequest request = new RestoreClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        BackupSource = new BackupSource(),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.RestoreClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceRestoreClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient#Google_Cloud_AlloyDb_V1Beta_AlloyDBAdminClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient#Google_Cloud_AlloyDb_V1Beta_AlloyDBAdminClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient#Google_Cloud_AlloyDb_V1Beta_AlloyDBAdminClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBAdminClient#Google_Cloud_AlloyDb_V1Beta_AlloyDBAdminClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### SwitchoverCluster(ClusterName, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> SwitchoverCluster(ClusterName name, CallSettings callSettings = null)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.SwitchoverCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceSwitchoverCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### SwitchoverCluster(SwitchoverClusterRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> SwitchoverCluster(SwitchoverClusterRequest request, CallSettings callSettings = null)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SwitchoverClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SwitchoverClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    SwitchoverClusterRequest request = new SwitchoverClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.SwitchoverCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceSwitchoverCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### SwitchoverCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> SwitchoverCluster(string name, CallSettings callSettings = null)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.SwitchoverCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceSwitchoverCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### SwitchoverClusterAsync(ClusterName, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> SwitchoverClusterAsync(ClusterName name, CallSettings callSettings = null)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.SwitchoverClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceSwitchoverClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### SwitchoverClusterAsync(ClusterName, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> SwitchoverClusterAsync(ClusterName name, CancellationToken cancellationToken)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.SwitchoverClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceSwitchoverClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### SwitchoverClusterAsync(SwitchoverClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> SwitchoverClusterAsync(SwitchoverClusterRequest request, CallSettings callSettings = null)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SwitchoverClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SwitchoverClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    SwitchoverClusterRequest request = new SwitchoverClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.SwitchoverClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceSwitchoverClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### SwitchoverClusterAsync(SwitchoverClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> SwitchoverClusterAsync(SwitchoverClusterRequest request, CancellationToken cancellationToken)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SwitchoverClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SwitchoverClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    SwitchoverClusterRequest request = new SwitchoverClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
        ValidateOnly = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.SwitchoverClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceSwitchoverClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### SwitchoverClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> SwitchoverClusterAsync(string name, CallSettings callSettings = null)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.SwitchoverClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceSwitchoverClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### SwitchoverClusterAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> SwitchoverClusterAsync(string name, CancellationToken cancellationToken)

Switches the roles of PRIMARY and SECONDARY clusters without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up the original PRIMARY cluster to replicate from this newly promoted cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the resource. For the required format, see the comment on the Cluster.name field  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.SwitchoverClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceSwitchoverClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBackup(Backup, FieldMask, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> UpdateBackup(Backup backup, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    Backup backup = new Backup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Backup, OperationMetadata> response = alloyDBAdminClient.UpdateBackup(backup, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpdateBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBackup(UpdateBackupRequest, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> UpdateBackup(UpdateBackupRequest request, CallSettings callSettings = null)

Updates the parameters of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    UpdateBackupRequest request = new UpdateBackupRequest
    {
        UpdateMask = new FieldMask(),
        Backup = new Backup(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = alloyDBAdminClient.UpdateBackup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpdateBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBackupAsync(Backup, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> UpdateBackupAsync(Backup backup, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    Backup backup = new Backup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.UpdateBackupAsync(backup, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBackupAsync(Backup, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> UpdateBackupAsync(Backup backup, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    Backup backup = new Backup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.UpdateBackupAsync(backup, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBackupAsync(UpdateBackupRequest, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> UpdateBackupAsync(UpdateBackupRequest request, CallSettings callSettings = null)

Updates the parameters of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateBackupRequest request = new UpdateBackupRequest
    {
        UpdateMask = new FieldMask(),
        Backup = new Backup(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.UpdateBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateBackupAsync(UpdateBackupRequest, CancellationToken)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> UpdateBackupAsync(UpdateBackupRequest request, CancellationToken cancellationToken)

Updates the parameters of a single Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateBackupRequest request = new UpdateBackupRequest
    {
        UpdateMask = new FieldMask(),
        Backup = new Backup(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = await alloyDBAdminClient.UpdateBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateCluster(Cluster, FieldMask, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> UpdateCluster(Cluster cluster, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    Cluster cluster = new Cluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.UpdateCluster(cluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpdateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateCluster(UpdateClusterRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> UpdateCluster(UpdateClusterRequest request, CallSettings callSettings = null)

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    UpdateClusterRequest request = new UpdateClusterRequest
    {
        UpdateMask = new FieldMask(),
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBAdminClient.UpdateCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpdateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateClusterAsync(Cluster, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> UpdateClusterAsync(Cluster cluster, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    Cluster cluster = new Cluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.UpdateClusterAsync(cluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateClusterAsync(Cluster, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> UpdateClusterAsync(Cluster cluster, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    Cluster cluster = new Cluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.UpdateClusterAsync(cluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateClusterAsync(UpdateClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> UpdateClusterAsync(UpdateClusterRequest request, CallSettings callSettings = null)

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateClusterRequest request = new UpdateClusterRequest
    {
        UpdateMask = new FieldMask(),
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.UpdateClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateClusterAsync(UpdateClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> UpdateClusterAsync(UpdateClusterRequest request, CancellationToken cancellationToken)

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateClusterRequest request = new UpdateClusterRequest
    {
        UpdateMask = new FieldMask(),
        Cluster = new Cluster(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBAdminClient.UpdateClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstance(Instance, FieldMask, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateInstance(Instance instance, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.UpdateInstance(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpdateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstance(UpdateInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateInstance(UpdateInstanceRequest request, CallSettings callSettings = null)

Updates the parameters of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = alloyDBAdminClient.UpdateInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpdateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(Instance, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(Instance instance, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.UpdateInstanceAsync(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(Instance, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(Instance instance, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.UpdateInstanceAsync(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(UpdateInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(UpdateInstanceRequest request, CallSettings callSettings = null)

Updates the parameters of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.UpdateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(UpdateInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(UpdateInstanceRequest request, CancellationToken cancellationToken)

Updates the parameters of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await alloyDBAdminClient.UpdateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateUser(UpdateUserRequest, CallSettings)
    
    
    public virtual User UpdateUser(UpdateUserRequest request, CallSettings callSettings = null)

Updates the parameters of a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateUserRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    UpdateUserRequest request = new UpdateUserRequest
    {
        UpdateMask = new FieldMask(),
        User = new User(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    User response = alloyDBAdminClient.UpdateUser(request);
    

### UpdateUser(User, FieldMask, CallSettings)
    
    
    public virtual User UpdateUser(User user, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single User.

**Parameters**  
---  
**Name** | **Description**  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the User resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    User user = new User();
    FieldMask updateMask = new FieldMask();
    // Make the request
    User response = alloyDBAdminClient.UpdateUser(user, updateMask);
    

### UpdateUserAsync(UpdateUserRequest, CallSettings)
    
    
    public virtual Task<User> UpdateUserAsync(UpdateUserRequest request, CallSettings callSettings = null)

Updates the parameters of a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateUserRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateUserRequest request = new UpdateUserRequest
    {
        UpdateMask = new FieldMask(),
        User = new User(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    User response = await alloyDBAdminClient.UpdateUserAsync(request);
    

### UpdateUserAsync(UpdateUserRequest, CancellationToken)
    
    
    public virtual Task<User> UpdateUserAsync(UpdateUserRequest request, CancellationToken cancellationToken)

Updates the parameters of a single User.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpdateUserRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpdateUserRequest request = new UpdateUserRequest
    {
        UpdateMask = new FieldMask(),
        User = new User(),
        RequestId = "",
        ValidateOnly = false,
        AllowMissing = false,
    };
    // Make the request
    User response = await alloyDBAdminClient.UpdateUserAsync(request);
    

### UpdateUserAsync(User, FieldMask, CallSettings)
    
    
    public virtual Task<User> UpdateUserAsync(User user, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single User.

**Parameters**  
---  
**Name** | **Description**  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the User resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    User user = new User();
    FieldMask updateMask = new FieldMask();
    // Make the request
    User response = await alloyDBAdminClient.UpdateUserAsync(user, updateMask);
    

### UpdateUserAsync(User, FieldMask, CancellationToken)
    
    
    public virtual Task<User> UpdateUserAsync(User user, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single User.

**Parameters**  
---  
**Name** | **Description**  
`user` | `[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the User resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[User](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.User)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    User user = new User();
    FieldMask updateMask = new FieldMask();
    // Make the request
    User response = await alloyDBAdminClient.UpdateUserAsync(user, updateMask);
    

### UpgradeCluster(ClusterName, DatabaseVersion, CallSettings)
    
    
    public virtual Operation<UpgradeClusterResponse, OperationMetadata> UpgradeCluster(ClusterName name, DatabaseVersion version, CallSettings callSettings = null)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`version` | `[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DatabaseVersion)`  
Required. The version the cluster is going to be upgraded to.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    DatabaseVersion version = DatabaseVersion.Unspecified;
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = alloyDBAdminClient.UpgradeCluster(name, version);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpgradeCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpgradeCluster(UpgradeClusterRequest, CallSettings)
    
    
    public virtual Operation<UpgradeClusterResponse, OperationMetadata> UpgradeCluster(UpgradeClusterRequest request, CallSettings callSettings = null)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    UpgradeClusterRequest request = new UpgradeClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Version = DatabaseVersion.Unspecified,
        RequestId = "",
        ValidateOnly = false,
        Etag = "",
    };
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = alloyDBAdminClient.UpgradeCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpgradeCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpgradeCluster(string, DatabaseVersion, CallSettings)
    
    
    public virtual Operation<UpgradeClusterResponse, OperationMetadata> UpgradeCluster(string name, DatabaseVersion version, CallSettings callSettings = null)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`version` | `[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DatabaseVersion)`  
Required. The version the cluster is going to be upgraded to.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = AlloyDBAdminClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    DatabaseVersion version = DatabaseVersion.Unspecified;
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = alloyDBAdminClient.UpgradeCluster(name, version);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.PollOnceUpgradeCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpgradeClusterAsync(ClusterName, DatabaseVersion, CallSettings)
    
    
    public virtual Task<Operation<UpgradeClusterResponse, OperationMetadata>> UpgradeClusterAsync(ClusterName name, DatabaseVersion version, CallSettings callSettings = null)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`version` | `[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DatabaseVersion)`  
Required. The version the cluster is going to be upgraded to.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    DatabaseVersion version = DatabaseVersion.Unspecified;
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = await alloyDBAdminClient.UpgradeClusterAsync(name, version);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpgradeClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpgradeClusterAsync(ClusterName, DatabaseVersion, CancellationToken)
    
    
    public virtual Task<Operation<UpgradeClusterResponse, OperationMetadata>> UpgradeClusterAsync(ClusterName name, DatabaseVersion version, CancellationToken cancellationToken)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)`  
Required. The resource name of the cluster.  
`version` | `[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DatabaseVersion)`  
Required. The version the cluster is going to be upgraded to.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    DatabaseVersion version = DatabaseVersion.Unspecified;
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = await alloyDBAdminClient.UpgradeClusterAsync(name, version);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpgradeClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpgradeClusterAsync(UpgradeClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<UpgradeClusterResponse, OperationMetadata>> UpgradeClusterAsync(UpgradeClusterRequest request, CallSettings callSettings = null)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpgradeClusterRequest request = new UpgradeClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Version = DatabaseVersion.Unspecified,
        RequestId = "",
        ValidateOnly = false,
        Etag = "",
    };
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = await alloyDBAdminClient.UpgradeClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpgradeClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpgradeClusterAsync(UpgradeClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<UpgradeClusterResponse, OperationMetadata>> UpgradeClusterAsync(UpgradeClusterRequest request, CancellationToken cancellationToken)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    UpgradeClusterRequest request = new UpgradeClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        Version = DatabaseVersion.Unspecified,
        RequestId = "",
        ValidateOnly = false,
        Etag = "",
    };
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = await alloyDBAdminClient.UpgradeClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpgradeClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpgradeClusterAsync(string, DatabaseVersion, CallSettings)
    
    
    public virtual Task<Operation<UpgradeClusterResponse, OperationMetadata>> UpgradeClusterAsync(string name, DatabaseVersion version, CallSettings callSettings = null)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`version` | `[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DatabaseVersion)`  
Required. The version the cluster is going to be upgraded to.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    DatabaseVersion version = DatabaseVersion.Unspecified;
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = await alloyDBAdminClient.UpgradeClusterAsync(name, version);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpgradeClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpgradeClusterAsync(string, DatabaseVersion, CancellationToken)
    
    
    public virtual Task<Operation<UpgradeClusterResponse, OperationMetadata>> UpgradeClusterAsync(string name, DatabaseVersion version, CancellationToken cancellationToken)

Upgrades a single Cluster. Imperative only.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the cluster.  
`version` | `[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DatabaseVersion)`  
Required. The version the cluster is going to be upgraded to.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBAdminClient alloyDBAdminClient = await AlloyDBAdminClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    DatabaseVersion version = DatabaseVersion.Unspecified;
    // Make the request
    Operation<UpgradeClusterResponse, OperationMetadata> response = await alloyDBAdminClient.UpgradeClusterAsync(name, version);
    
    // Poll until the returned long-running operation is complete
    Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpgradeClusterResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = await alloyDBAdminClient.PollOnceUpgradeClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpgradeClusterResponse retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
