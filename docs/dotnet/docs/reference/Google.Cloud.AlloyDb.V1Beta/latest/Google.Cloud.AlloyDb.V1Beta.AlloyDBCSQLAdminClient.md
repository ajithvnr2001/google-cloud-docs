---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient
title: AlloyDB v1beta API - Class AlloyDBCSQLAdminClient (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:07.571767+00:00
---

# AlloyDB v1beta API - Class AlloyDBCSQLAdminClient (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class AlloyDBCSQLAdminClient (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public abstract class AlloyDBCSQLAdminClient

Reference documentation and code samples for the AlloyDB v1beta API class AlloyDBCSQLAdminClient.

AlloyDBCSQLAdmin client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AlloyDBCSQLAdminClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AlloyDBCSQLAdminClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClientImpl)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Remarks

Service for interactions with CloudSQL.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AlloyDBCSQLAdmin service, which is a host of "alloydb.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AlloyDBCSQLAdmin scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AlloyDBCSQLAdmin scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual AlloyDBCSQLAdmin.AlloyDBCSQLAdminClient GrpcClient { get; }

The underlying gRPC AlloyDBCSQLAdmin client

**Property Value**  
---  
**Type** | **Description**  
`[AlloyDBCSQLAdmin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdmin)[AlloyDBCSQLAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdmin.AlloyDBCSQLAdminClient)` |   
  
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
  
### RestoreFromCloudSQLOperationsClient
    
    
    public virtual OperationsClient RestoreFromCloudSQLOperationsClient { get; }

The long-running operations client for `RestoreFromCloudSQL`.

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
    
    
    public static AlloyDBCSQLAdminClient Create()

Synchronously creates a [AlloyDBCSQLAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AlloyDBCSQLAdminClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBCSQLAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient)` | The created [AlloyDBCSQLAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AlloyDBCSQLAdminClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AlloyDBCSQLAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AlloyDBCSQLAdminClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AlloyDBCSQLAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient)` | The task representing the created [AlloyDBCSQLAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient).  
  
### PollOnceRestoreFromCloudSQL(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOnceRestoreFromCloudSQL(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RestoreFromCloudSQL` .

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
  
### PollOnceRestoreFromCloudSQLAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOnceRestoreFromCloudSQLAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RestoreFromCloudSQL`.

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
  
### RestoreFromCloudSQL(LocationName, string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> RestoreFromCloudSQL(LocationName parent, string clusterId, CallSettings callSettings = null)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on Cluster.name field.  
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
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBCSQLAdminClient.RestoreFromCloudSQL(parent, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQL(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreFromCloudSQL(RestoreFromCloudSQLRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> RestoreFromCloudSQL(RestoreFromCloudSQLRequest request, CallSettings callSettings = null)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreFromCloudSQLRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestoreFromCloudSQLRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.Create();
    // Initialize request argument(s)
    RestoreFromCloudSQLRequest request = new RestoreFromCloudSQLRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        CloudsqlBackupRunSource = new CloudSQLBackupRunSource(),
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBCSQLAdminClient.RestoreFromCloudSQL(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQL(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreFromCloudSQL(string, string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> RestoreFromCloudSQL(string parent, string clusterId, CallSettings callSettings = null)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on Cluster.name field.  
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
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = alloyDBCSQLAdminClient.RestoreFromCloudSQL(parent, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQL(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreFromCloudSQLAsync(LocationName, string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> RestoreFromCloudSQLAsync(LocationName parent, string clusterId, CallSettings callSettings = null)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on Cluster.name field.  
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
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = await AlloyDBCSQLAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBCSQLAdminClient.RestoreFromCloudSQLAsync(parent, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQLAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreFromCloudSQLAsync(LocationName, string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> RestoreFromCloudSQLAsync(LocationName parent, string clusterId, CancellationToken cancellationToken)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the new cluster. For the required format, see the comment on Cluster.name field.  
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
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = await AlloyDBCSQLAdminClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBCSQLAdminClient.RestoreFromCloudSQLAsync(parent, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQLAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreFromCloudSQLAsync(RestoreFromCloudSQLRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> RestoreFromCloudSQLAsync(RestoreFromCloudSQLRequest request, CallSettings callSettings = null)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreFromCloudSQLRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestoreFromCloudSQLRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = await AlloyDBCSQLAdminClient.CreateAsync();
    // Initialize request argument(s)
    RestoreFromCloudSQLRequest request = new RestoreFromCloudSQLRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        CloudsqlBackupRunSource = new CloudSQLBackupRunSource(),
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBCSQLAdminClient.RestoreFromCloudSQLAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQLAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreFromCloudSQLAsync(RestoreFromCloudSQLRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> RestoreFromCloudSQLAsync(RestoreFromCloudSQLRequest request, CancellationToken cancellationToken)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreFromCloudSQLRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.RestoreFromCloudSQLRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = await AlloyDBCSQLAdminClient.CreateAsync();
    // Initialize request argument(s)
    RestoreFromCloudSQLRequest request = new RestoreFromCloudSQLRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        CloudsqlBackupRunSource = new CloudSQLBackupRunSource(),
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBCSQLAdminClient.RestoreFromCloudSQLAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQLAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreFromCloudSQLAsync(string, string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> RestoreFromCloudSQLAsync(string parent, string clusterId, CallSettings callSettings = null)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on Cluster.name field.  
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
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = await AlloyDBCSQLAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBCSQLAdminClient.RestoreFromCloudSQLAsync(parent, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQLAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### RestoreFromCloudSQLAsync(string, string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> RestoreFromCloudSQLAsync(string parent, string clusterId, CancellationToken cancellationToken)

Restores an AlloyDB cluster from a CloudSQL resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the new cluster. For the required format, see the comment on Cluster.name field.  
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
    AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = await AlloyDBCSQLAdminClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await alloyDBCSQLAdminClient.RestoreFromCloudSQLAsync(parent, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await alloyDBCSQLAdminClient.PollOnceRestoreFromCloudSQLAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient#Google_Cloud_AlloyDb_V1Beta_AlloyDBCSQLAdminClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient#Google_Cloud_AlloyDb_V1Beta_AlloyDBCSQLAdminClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient#Google_Cloud_AlloyDb_V1Beta_AlloyDBCSQLAdminClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AlloyDBCSQLAdminClient#Google_Cloud_AlloyDb_V1Beta_AlloyDBCSQLAdminClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
