---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient
title: Dataproc Metastore v1beta API - Class DataprocMetastoreClient (2.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:50.555060+00:00
---

# Dataproc Metastore v1beta API - Class DataprocMetastoreClient (2.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1beta API - Class DataprocMetastoreClient (2.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient)
  * [ 2.0.0-beta11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/2.0.0-beta11/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/1.0.0-beta02/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient)


    
    
    public abstract class DataprocMetastoreClient

Reference documentation and code samples for the Dataproc Metastore v1beta API class DataprocMetastoreClient.

DataprocMetastore client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataprocMetastoreClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DataprocMetastoreClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClientImpl)

## Namespace

[Google.Cloud.Metastore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta)

## Assembly

Google.Cloud.Metastore.V1Beta.dll

## Remarks

Configures and manages metastore services. Metastore services are fully managed, highly available, autoscaled, autohealing, OSS-native deployments of technical metadata management software. Each metastore service exposes a network endpoint through which metadata queries are served. Metadata queries can originate from a variety of sources, including Apache Hive, Apache Presto, and Apache Spark.

The Dataproc Metastore API defines the following resource model:

  * The service works with a collection of Google Cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*` (a location must refer to a Google Cloud `region`)
  * Each location has a collection of services, named: `/services/*`
  * Dataproc Metastore services are resources with names of the form:



`/projects/{project_number}/locations/{location_id}/services/{service_id}`.

## Properties 

### AlterMetadataResourceLocationOperationsClient
    
    
    public virtual OperationsClient AlterMetadataResourceLocationOperationsClient { get; }

The long-running operations client for `AlterMetadataResourceLocation`.

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
  
### CreateMetadataImportOperationsClient
    
    
    public virtual OperationsClient CreateMetadataImportOperationsClient { get; }

The long-running operations client for `CreateMetadataImport`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateServiceOperationsClient
    
    
    public virtual OperationsClient CreateServiceOperationsClient { get; }

The long-running operations client for `CreateService`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the DataprocMetastore service, which is a host of "metastore.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default DataprocMetastore scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default DataprocMetastore scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteBackupOperationsClient
    
    
    public virtual OperationsClient DeleteBackupOperationsClient { get; }

The long-running operations client for `DeleteBackup`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteServiceOperationsClient
    
    
    public virtual OperationsClient DeleteServiceOperationsClient { get; }

The long-running operations client for `DeleteService`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ExportMetadataOperationsClient
    
    
    public virtual OperationsClient ExportMetadataOperationsClient { get; }

The long-running operations client for `ExportMetadata`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual DataprocMetastore.DataprocMetastoreClient GrpcClient { get; }

The underlying gRPC DataprocMetastore client

**Property Value**  
---  
**Type** | **Description**  
`[DataprocMetastore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastore)[DataprocMetastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastore.DataprocMetastoreClient)` |   
  
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
  
### MoveTableToDatabaseOperationsClient
    
    
    public virtual OperationsClient MoveTableToDatabaseOperationsClient { get; }

The long-running operations client for `MoveTableToDatabase`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### QueryMetadataOperationsClient
    
    
    public virtual OperationsClient QueryMetadataOperationsClient { get; }

The long-running operations client for `QueryMetadata`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### RestoreServiceOperationsClient
    
    
    public virtual OperationsClient RestoreServiceOperationsClient { get; }

The long-running operations client for `RestoreService`.

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
  
### UpdateMetadataImportOperationsClient
    
    
    public virtual OperationsClient UpdateMetadataImportOperationsClient { get; }

The long-running operations client for `UpdateMetadataImport`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateServiceOperationsClient
    
    
    public virtual OperationsClient UpdateServiceOperationsClient { get; }

The long-running operations client for `UpdateService`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### AlterMetadataResourceLocation(AlterMetadataResourceLocationRequest, CallSettings)
    
    
    public virtual Operation<AlterMetadataResourceLocationResponse, OperationMetadata> AlterMetadataResourceLocation(AlterMetadataResourceLocationRequest request, CallSettings callSettings = null)

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.AlterMetadataResourceLocationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.AlterMetadataResourceLocationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    AlterMetadataResourceLocationRequest request = new AlterMetadataResourceLocationRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        ResourceName = "",
        LocationUri = "",
    };
    // Make the request
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> response = dataprocMetastoreClient.AlterMetadataResourceLocation(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AlterMetadataResourceLocationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceAlterMetadataResourceLocation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AlterMetadataResourceLocationResponse retrievedResult = retrievedResponse.Result;
    }
    

### AlterMetadataResourceLocationAsync(AlterMetadataResourceLocationRequest, CallSettings)
    
    
    public virtual Task<Operation<AlterMetadataResourceLocationResponse, OperationMetadata>> AlterMetadataResourceLocationAsync(AlterMetadataResourceLocationRequest request, CallSettings callSettings = null)

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.AlterMetadataResourceLocationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.AlterMetadataResourceLocationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    AlterMetadataResourceLocationRequest request = new AlterMetadataResourceLocationRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        ResourceName = "",
        LocationUri = "",
    };
    // Make the request
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> response = await dataprocMetastoreClient.AlterMetadataResourceLocationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AlterMetadataResourceLocationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceAlterMetadataResourceLocationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AlterMetadataResourceLocationResponse retrievedResult = retrievedResponse.Result;
    }
    

### AlterMetadataResourceLocationAsync(AlterMetadataResourceLocationRequest, CancellationToken)
    
    
    public virtual Task<Operation<AlterMetadataResourceLocationResponse, OperationMetadata>> AlterMetadataResourceLocationAsync(AlterMetadataResourceLocationRequest request, CancellationToken cancellationToken)

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.AlterMetadataResourceLocationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.AlterMetadataResourceLocationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    AlterMetadataResourceLocationRequest request = new AlterMetadataResourceLocationRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        ResourceName = "",
        LocationUri = "",
    };
    // Make the request
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> response = await dataprocMetastoreClient.AlterMetadataResourceLocationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AlterMetadataResourceLocationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AlterMetadataResourceLocationResponse, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceAlterMetadataResourceLocationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AlterMetadataResourceLocationResponse retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static DataprocMetastoreClient Create()

Synchronously creates a [DataprocMetastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataprocMetastoreClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient)` | The created [DataprocMetastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DataprocMetastoreClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DataprocMetastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataprocMetastoreClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataprocMetastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient)` | The task representing the created [DataprocMetastoreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient).  
  
### CreateBackup(CreateBackupRequest, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> CreateBackup(CreateBackupRequest request, CallSettings callSettings = null)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    CreateBackupRequest request = new CreateBackupRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        BackupId = "",
        Backup = new Backup(),
        RequestId = "",
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = dataprocMetastoreClient.CreateBackup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackup(ServiceName, Backup, string, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> CreateBackup(ServiceName parent, Backup backup, string backupId, CallSettings callSettings = null)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)`  
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = dataprocMetastoreClient.CreateBackup(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackup(string, Backup, string, CallSettings)
    
    
    public virtual Operation<Backup, OperationMetadata> CreateBackup(string parent, Backup backup, string backupId, CallSettings callSettings = null)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)`  
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = dataprocMetastoreClient.CreateBackup(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(CreateBackupRequest, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(CreateBackupRequest request, CallSettings callSettings = null)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    CreateBackupRequest request = new CreateBackupRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        BackupId = "",
        Backup = new Backup(),
        RequestId = "",
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = await dataprocMetastoreClient.CreateBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(CreateBackupRequest, CancellationToken)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(CreateBackupRequest request, CancellationToken cancellationToken)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    CreateBackupRequest request = new CreateBackupRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        BackupId = "",
        Backup = new Backup(),
        RequestId = "",
    };
    // Make the request
    Operation<Backup, OperationMetadata> response = await dataprocMetastoreClient.CreateBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(ServiceName, Backup, string, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(ServiceName parent, Backup backup, string backupId, CallSettings callSettings = null)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)`  
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = await dataprocMetastoreClient.CreateBackupAsync(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(ServiceName, Backup, string, CancellationToken)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(ServiceName parent, Backup backup, string backupId, CancellationToken cancellationToken)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)`  
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = await dataprocMetastoreClient.CreateBackupAsync(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(string, Backup, string, CallSettings)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(string parent, Backup backup, string backupId, CallSettings callSettings = null)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)`  
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = await dataprocMetastoreClient.CreateBackupAsync(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateBackupAsync(string, Backup, string, CancellationToken)
    
    
    public virtual Task<Operation<Backup, OperationMetadata>> CreateBackupAsync(string parent, Backup backup, string backupId, CancellationToken cancellationToken)

Creates a new backup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`backup` | `[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)`  
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    Backup backup = new Backup();
    string backupId = "";
    // Make the request
    Operation<Backup, OperationMetadata> response = await dataprocMetastoreClient.CreateBackupAsync(parent, backup, backupId);
    
    // Poll until the returned long-running operation is complete
    Operation<Backup, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Backup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Backup, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Backup retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImport(CreateMetadataImportRequest, CallSettings)
    
    
    public virtual Operation<MetadataImport, OperationMetadata> CreateMetadataImport(CreateMetadataImportRequest request, CallSettings callSettings = null)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    CreateMetadataImportRequest request = new CreateMetadataImportRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        MetadataImportId = "",
        MetadataImport = new MetadataImport(),
        RequestId = "",
    };
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = dataprocMetastoreClient.CreateMetadataImport(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateMetadataImport(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImport(ServiceName, MetadataImport, string, CallSettings)
    
    
    public virtual Operation<MetadataImport, OperationMetadata> CreateMetadataImport(ServiceName parent, MetadataImport metadataImport, string metadataImportId, CallSettings callSettings = null)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    MetadataImport metadataImport = new MetadataImport();
    string metadataImportId = "";
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = dataprocMetastoreClient.CreateMetadataImport(parent, metadataImport, metadataImportId);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateMetadataImport(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImport(string, MetadataImport, string, CallSettings)
    
    
    public virtual Operation<MetadataImport, OperationMetadata> CreateMetadataImport(string parent, MetadataImport metadataImport, string metadataImportId, CallSettings callSettings = null)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    MetadataImport metadataImport = new MetadataImport();
    string metadataImportId = "";
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = dataprocMetastoreClient.CreateMetadataImport(parent, metadataImport, metadataImportId);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateMetadataImport(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImportAsync(CreateMetadataImportRequest, CallSettings)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> CreateMetadataImportAsync(CreateMetadataImportRequest request, CallSettings callSettings = null)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    CreateMetadataImportRequest request = new CreateMetadataImportRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        MetadataImportId = "",
        MetadataImport = new MetadataImport(),
        RequestId = "",
    };
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.CreateMetadataImportAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImportAsync(CreateMetadataImportRequest, CancellationToken)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> CreateMetadataImportAsync(CreateMetadataImportRequest request, CancellationToken cancellationToken)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    CreateMetadataImportRequest request = new CreateMetadataImportRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        MetadataImportId = "",
        MetadataImport = new MetadataImport(),
        RequestId = "",
    };
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.CreateMetadataImportAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImportAsync(ServiceName, MetadataImport, string, CallSettings)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> CreateMetadataImportAsync(ServiceName parent, MetadataImport metadataImport, string metadataImportId, CallSettings callSettings = null)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    MetadataImport metadataImport = new MetadataImport();
    string metadataImportId = "";
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.CreateMetadataImportAsync(parent, metadataImport, metadataImportId);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImportAsync(ServiceName, MetadataImport, string, CancellationToken)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> CreateMetadataImportAsync(ServiceName parent, MetadataImport metadataImport, string metadataImportId, CancellationToken cancellationToken)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    MetadataImport metadataImport = new MetadataImport();
    string metadataImportId = "";
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.CreateMetadataImportAsync(parent, metadataImport, metadataImportId);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImportAsync(string, MetadataImport, string, CallSettings)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> CreateMetadataImportAsync(string parent, MetadataImport metadataImport, string metadataImportId, CallSettings callSettings = null)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    MetadataImport metadataImport = new MetadataImport();
    string metadataImportId = "";
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.CreateMetadataImportAsync(parent, metadataImport, metadataImportId);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateMetadataImportAsync(string, MetadataImport, string, CancellationToken)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> CreateMetadataImportAsync(string parent, MetadataImport metadataImport, string metadataImportId, CancellationToken cancellationToken)

Creates a new MetadataImport in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    MetadataImport metadataImport = new MetadataImport();
    string metadataImportId = "";
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.CreateMetadataImportAsync(parent, metadataImport, metadataImportId);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### CreateService(LocationName, Service, string, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> CreateService(LocationName parent, Service service, string serviceId, CallSettings callSettings = null)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = dataprocMetastoreClient.CreateService(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateService(CreateServiceRequest, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> CreateService(CreateServiceRequest request, CallSettings callSettings = null)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    CreateServiceRequest request = new CreateServiceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ServiceId = "",
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = dataprocMetastoreClient.CreateService(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateService(string, Service, string, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> CreateService(string parent, Service service, string serviceId, CallSettings callSettings = null)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = dataprocMetastoreClient.CreateService(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceCreateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(LocationName, Service, string, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(LocationName parent, Service service, string serviceId, CallSettings callSettings = null)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.CreateServiceAsync(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(LocationName, Service, string, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(LocationName parent, Service service, string serviceId, CancellationToken cancellationToken)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.CreateServiceAsync(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(CreateServiceRequest, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(CreateServiceRequest request, CallSettings callSettings = null)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    CreateServiceRequest request = new CreateServiceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ServiceId = "",
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.CreateServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(CreateServiceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(CreateServiceRequest request, CancellationToken cancellationToken)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    CreateServiceRequest request = new CreateServiceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ServiceId = "",
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.CreateServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(string, Service, string, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(string parent, Service service, string serviceId, CallSettings callSettings = null)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.CreateServiceAsync(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### CreateServiceAsync(string, Service, string, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> CreateServiceAsync(string parent, Service service, string serviceId, CancellationToken cancellationToken)

Creates a metastore service in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Service service = new Service();
    string serviceId = "";
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.CreateServiceAsync(parent, service, serviceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceCreateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackup(BackupName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteBackup(BackupName name, CallSettings callSettings = null)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreClient.DeleteBackup(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceDeleteBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackup(DeleteBackupRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteBackup(DeleteBackupRequest request, CallSettings callSettings = null)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    DeleteBackupRequest request = new DeleteBackupRequest
    {
        BackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreClient.DeleteBackup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceDeleteBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackup(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteBackup(string name, CallSettings callSettings = null)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreClient.DeleteBackup(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceDeleteBackup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(BackupName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(BackupName name, CallSettings callSettings = null)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteBackupAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(BackupName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(BackupName name, CancellationToken cancellationToken)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteBackupAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(DeleteBackupRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(DeleteBackupRequest request, CallSettings callSettings = null)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteBackupRequest request = new DeleteBackupRequest
    {
        BackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(DeleteBackupRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(DeleteBackupRequest request, CancellationToken cancellationToken)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteBackupRequest request = new DeleteBackupRequest
    {
        BackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteBackupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(string name, CallSettings callSettings = null)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteBackupAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteBackupAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteBackupAsync(string name, CancellationToken cancellationToken)

Deletes a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteBackupAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteBackupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteService(DeleteServiceRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteService(DeleteServiceRequest request, CallSettings callSettings = null)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    DeleteServiceRequest request = new DeleteServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreClient.DeleteService(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceDeleteService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteService(ServiceName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteService(ServiceName name, CallSettings callSettings = null)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreClient.DeleteService(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceDeleteService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteService(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteService(string name, CallSettings callSettings = null)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreClient.DeleteService(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceDeleteService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(DeleteServiceRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(DeleteServiceRequest request, CallSettings callSettings = null)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteServiceRequest request = new DeleteServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(DeleteServiceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(DeleteServiceRequest request, CancellationToken cancellationToken)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteServiceRequest request = new DeleteServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(ServiceName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(ServiceName name, CallSettings callSettings = null)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteServiceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(ServiceName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(ServiceName name, CancellationToken cancellationToken)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteServiceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(string name, CallSettings callSettings = null)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteServiceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteServiceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteServiceAsync(string name, CancellationToken cancellationToken)

Deletes a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreClient.DeleteServiceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceDeleteServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### ExportMetadata(ExportMetadataRequest, CallSettings)
    
    
    public virtual Operation<MetadataExport, OperationMetadata> ExportMetadata(ExportMetadataRequest request, CallSettings callSettings = null)

Exports metadata from a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ExportMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataExport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ExportMetadataRequest request = new ExportMetadataRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        DestinationGcsFolder = "",
        RequestId = "",
        DatabaseDumpType = DatabaseDumpSpec.Types.Type.Unspecified,
    };
    // Make the request
    Operation<MetadataExport, OperationMetadata> response = dataprocMetastoreClient.ExportMetadata(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataExport, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MetadataExport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataExport, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceExportMetadata(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataExport retrievedResult = retrievedResponse.Result;
    }
    

### ExportMetadataAsync(ExportMetadataRequest, CallSettings)
    
    
    public virtual Task<Operation<MetadataExport, OperationMetadata>> ExportMetadataAsync(ExportMetadataRequest request, CallSettings callSettings = null)

Exports metadata from a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ExportMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataExport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ExportMetadataRequest request = new ExportMetadataRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        DestinationGcsFolder = "",
        RequestId = "",
        DatabaseDumpType = DatabaseDumpSpec.Types.Type.Unspecified,
    };
    // Make the request
    Operation<MetadataExport, OperationMetadata> response = await dataprocMetastoreClient.ExportMetadataAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataExport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataExport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataExport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceExportMetadataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataExport retrievedResult = retrievedResponse.Result;
    }
    

### ExportMetadataAsync(ExportMetadataRequest, CancellationToken)
    
    
    public virtual Task<Operation<MetadataExport, OperationMetadata>> ExportMetadataAsync(ExportMetadataRequest request, CancellationToken cancellationToken)

Exports metadata from a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ExportMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataExport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ExportMetadataRequest request = new ExportMetadataRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        DestinationGcsFolder = "",
        RequestId = "",
        DatabaseDumpType = DatabaseDumpSpec.Types.Type.Unspecified,
    };
    // Make the request
    Operation<MetadataExport, OperationMetadata> response = await dataprocMetastoreClient.ExportMetadataAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataExport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataExport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataExport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceExportMetadataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataExport retrievedResult = retrievedResponse.Result;
    }
    

### GetBackup(BackupName, CallSettings)
    
    
    public virtual Backup GetBackup(BackupName name, CallSettings callSettings = null)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Backup response = dataprocMetastoreClient.GetBackup(name);
    

### GetBackup(GetBackupRequest, CallSettings)
    
    
    public virtual Backup GetBackup(GetBackupRequest request, CallSettings callSettings = null)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    GetBackupRequest request = new GetBackupRequest
    {
        BackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
    };
    // Make the request
    Backup response = dataprocMetastoreClient.GetBackup(request);
    

### GetBackup(string, CallSettings)
    
    
    public virtual Backup GetBackup(string name, CallSettings callSettings = null)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Backup response = dataprocMetastoreClient.GetBackup(name);
    

### GetBackupAsync(BackupName, CallSettings)
    
    
    public virtual Task<Backup> GetBackupAsync(BackupName name, CallSettings callSettings = null)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Backup response = await dataprocMetastoreClient.GetBackupAsync(name);
    

### GetBackupAsync(BackupName, CancellationToken)
    
    
    public virtual Task<Backup> GetBackupAsync(BackupName name, CancellationToken cancellationToken)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    BackupName name = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Backup response = await dataprocMetastoreClient.GetBackupAsync(name);
    

### GetBackupAsync(GetBackupRequest, CallSettings)
    
    
    public virtual Task<Backup> GetBackupAsync(GetBackupRequest request, CallSettings callSettings = null)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    GetBackupRequest request = new GetBackupRequest
    {
        BackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
    };
    // Make the request
    Backup response = await dataprocMetastoreClient.GetBackupAsync(request);
    

### GetBackupAsync(GetBackupRequest, CancellationToken)
    
    
    public virtual Task<Backup> GetBackupAsync(GetBackupRequest request, CancellationToken cancellationToken)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    GetBackupRequest request = new GetBackupRequest
    {
        BackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
    };
    // Make the request
    Backup response = await dataprocMetastoreClient.GetBackupAsync(request);
    

### GetBackupAsync(string, CallSettings)
    
    
    public virtual Task<Backup> GetBackupAsync(string name, CallSettings callSettings = null)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Backup response = await dataprocMetastoreClient.GetBackupAsync(name);
    

### GetBackupAsync(string, CancellationToken)
    
    
    public virtual Task<Backup> GetBackupAsync(string name, CancellationToken cancellationToken)

Gets details of a single backup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Backup response = await dataprocMetastoreClient.GetBackupAsync(name);
    

### GetMetadataImport(GetMetadataImportRequest, CallSettings)
    
    
    public virtual MetadataImport GetMetadataImport(GetMetadataImportRequest request, CallSettings callSettings = null)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    GetMetadataImportRequest request = new GetMetadataImportRequest
    {
        MetadataImportName = MetadataImportName.FromProjectLocationServiceMetadataImport("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]"),
    };
    // Make the request
    MetadataImport response = dataprocMetastoreClient.GetMetadataImport(request);
    

### GetMetadataImport(MetadataImportName, CallSettings)
    
    
    public virtual MetadataImport GetMetadataImport(MetadataImportName name, CallSettings callSettings = null)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImportName)`  
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    MetadataImportName name = MetadataImportName.FromProjectLocationServiceMetadataImport("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]");
    // Make the request
    MetadataImport response = dataprocMetastoreClient.GetMetadataImport(name);
    

### GetMetadataImport(string, CallSettings)
    
    
    public virtual MetadataImport GetMetadataImport(string name, CallSettings callSettings = null)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/metadataImports/[METADATA_IMPORT]";
    // Make the request
    MetadataImport response = dataprocMetastoreClient.GetMetadataImport(name);
    

### GetMetadataImportAsync(GetMetadataImportRequest, CallSettings)
    
    
    public virtual Task<MetadataImport> GetMetadataImportAsync(GetMetadataImportRequest request, CallSettings callSettings = null)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    GetMetadataImportRequest request = new GetMetadataImportRequest
    {
        MetadataImportName = MetadataImportName.FromProjectLocationServiceMetadataImport("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]"),
    };
    // Make the request
    MetadataImport response = await dataprocMetastoreClient.GetMetadataImportAsync(request);
    

### GetMetadataImportAsync(GetMetadataImportRequest, CancellationToken)
    
    
    public virtual Task<MetadataImport> GetMetadataImportAsync(GetMetadataImportRequest request, CancellationToken cancellationToken)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    GetMetadataImportRequest request = new GetMetadataImportRequest
    {
        MetadataImportName = MetadataImportName.FromProjectLocationServiceMetadataImport("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]"),
    };
    // Make the request
    MetadataImport response = await dataprocMetastoreClient.GetMetadataImportAsync(request);
    

### GetMetadataImportAsync(MetadataImportName, CallSettings)
    
    
    public virtual Task<MetadataImport> GetMetadataImportAsync(MetadataImportName name, CallSettings callSettings = null)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImportName)`  
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    MetadataImportName name = MetadataImportName.FromProjectLocationServiceMetadataImport("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]");
    // Make the request
    MetadataImport response = await dataprocMetastoreClient.GetMetadataImportAsync(name);
    

### GetMetadataImportAsync(MetadataImportName, CancellationToken)
    
    
    public virtual Task<MetadataImport> GetMetadataImportAsync(MetadataImportName name, CancellationToken cancellationToken)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImportName)`  
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    MetadataImportName name = MetadataImportName.FromProjectLocationServiceMetadataImport("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]");
    // Make the request
    MetadataImport response = await dataprocMetastoreClient.GetMetadataImportAsync(name);
    

### GetMetadataImportAsync(string, CallSettings)
    
    
    public virtual Task<MetadataImport> GetMetadataImportAsync(string name, CallSettings callSettings = null)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/metadataImports/[METADATA_IMPORT]";
    // Make the request
    MetadataImport response = await dataprocMetastoreClient.GetMetadataImportAsync(name);
    

### GetMetadataImportAsync(string, CancellationToken)
    
    
    public virtual Task<MetadataImport> GetMetadataImportAsync(string name, CancellationToken cancellationToken)

Gets details of a single import.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/metadataImports/[METADATA_IMPORT]";
    // Make the request
    MetadataImport response = await dataprocMetastoreClient.GetMetadataImportAsync(name);
    

### GetService(GetServiceRequest, CallSettings)
    
    
    public virtual Service GetService(GetServiceRequest request, CallSettings callSettings = null)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    GetServiceRequest request = new GetServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
    };
    // Make the request
    Service response = dataprocMetastoreClient.GetService(request);
    

### GetService(ServiceName, CallSettings)
    
    
    public virtual Service GetService(ServiceName name, CallSettings callSettings = null)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    Service response = dataprocMetastoreClient.GetService(name);
    

### GetService(string, CallSettings)
    
    
    public virtual Service GetService(string name, CallSettings callSettings = null)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    Service response = dataprocMetastoreClient.GetService(name);
    

### GetServiceAsync(GetServiceRequest, CallSettings)
    
    
    public virtual Task<Service> GetServiceAsync(GetServiceRequest request, CallSettings callSettings = null)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    GetServiceRequest request = new GetServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
    };
    // Make the request
    Service response = await dataprocMetastoreClient.GetServiceAsync(request);
    

### GetServiceAsync(GetServiceRequest, CancellationToken)
    
    
    public virtual Task<Service> GetServiceAsync(GetServiceRequest request, CancellationToken cancellationToken)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    GetServiceRequest request = new GetServiceRequest
    {
        ServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
    };
    // Make the request
    Service response = await dataprocMetastoreClient.GetServiceAsync(request);
    

### GetServiceAsync(ServiceName, CallSettings)
    
    
    public virtual Task<Service> GetServiceAsync(ServiceName name, CallSettings callSettings = null)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    Service response = await dataprocMetastoreClient.GetServiceAsync(name);
    

### GetServiceAsync(ServiceName, CancellationToken)
    
    
    public virtual Task<Service> GetServiceAsync(ServiceName name, CancellationToken cancellationToken)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName name = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    Service response = await dataprocMetastoreClient.GetServiceAsync(name);
    

### GetServiceAsync(string, CallSettings)
    
    
    public virtual Task<Service> GetServiceAsync(string name, CallSettings callSettings = null)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    Service response = await dataprocMetastoreClient.GetServiceAsync(name);
    

### GetServiceAsync(string, CancellationToken)
    
    
    public virtual Task<Service> GetServiceAsync(string name, CancellationToken cancellationToken)

Gets the details of a single service.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    Service response = await dataprocMetastoreClient.GetServiceAsync(name);
    

### ListBackups(ListBackupsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListBackupsResponse, Backup> ListBackups(ListBackupsRequest request, CallSettings callSettings = null)

Lists backups in a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A pageable sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ListBackupsRequest request = new ListBackupsRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListBackupsResponse, Backup> response = dataprocMetastoreClient.ListBackups(request);
    
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
    

### ListBackups(ServiceName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListBackupsResponse, Backup> ListBackups(ServiceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists backups in a service.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service whose backups to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A pageable sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    PagedEnumerable<ListBackupsResponse, Backup> response = dataprocMetastoreClient.ListBackups(parent);
    
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

Lists backups in a service.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service whose backups to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A pageable sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    PagedEnumerable<ListBackupsResponse, Backup> response = dataprocMetastoreClient.ListBackups(parent);
    
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
    

### ListBackupsAsync(ListBackupsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListBackupsResponse, Backup> ListBackupsAsync(ListBackupsRequest request, CallSettings callSettings = null)

Lists backups in a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A pageable asynchronous sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ListBackupsRequest request = new ListBackupsRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListBackupsResponse, Backup> response = dataprocMetastoreClient.ListBackupsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Backup item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListBackupsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
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
    

### ListBackupsAsync(ServiceName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListBackupsResponse, Backup> ListBackupsAsync(ServiceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists backups in a service.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service whose backups to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A pageable asynchronous sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    PagedAsyncEnumerable<ListBackupsResponse, Backup> response = dataprocMetastoreClient.ListBackupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Backup item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListBackupsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
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

Lists backups in a service.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service whose backups to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListBackupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListBackupsResponse)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)` | A pageable asynchronous sequence of [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    PagedAsyncEnumerable<ListBackupsResponse, Backup> response = dataprocMetastoreClient.ListBackupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Backup item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListBackupsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Backup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
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
    

### ListMetadataImports(ListMetadataImportsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListMetadataImportsResponse, MetadataImport> ListMetadataImports(ListMetadataImportsRequest request, CallSettings callSettings = null)

Lists imports in a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMetadataImportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListMetadataImportsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListMetadataImportsResponse)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A pageable sequence of [MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ListMetadataImportsRequest request = new ListMetadataImportsRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListMetadataImportsResponse, MetadataImport> response = dataprocMetastoreClient.ListMetadataImports(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MetadataImport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMetadataImportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MetadataImport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MetadataImport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MetadataImport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMetadataImports(ServiceName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMetadataImportsResponse, MetadataImport> ListMetadataImports(ServiceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists imports in a service.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service whose metadata imports to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListMetadataImportsResponse)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A pageable sequence of [MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    PagedEnumerable<ListMetadataImportsResponse, MetadataImport> response = dataprocMetastoreClient.ListMetadataImports(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MetadataImport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMetadataImportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MetadataImport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MetadataImport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MetadataImport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMetadataImports(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMetadataImportsResponse, MetadataImport> ListMetadataImports(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists imports in a service.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service whose metadata imports to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListMetadataImportsResponse)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A pageable sequence of [MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    PagedEnumerable<ListMetadataImportsResponse, MetadataImport> response = dataprocMetastoreClient.ListMetadataImports(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MetadataImport item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMetadataImportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MetadataImport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MetadataImport> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MetadataImport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMetadataImportsAsync(ListMetadataImportsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMetadataImportsResponse, MetadataImport> ListMetadataImportsAsync(ListMetadataImportsRequest request, CallSettings callSettings = null)

Lists imports in a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMetadataImportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListMetadataImportsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListMetadataImportsResponse)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A pageable asynchronous sequence of [MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ListMetadataImportsRequest request = new ListMetadataImportsRequest
    {
        ParentAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListMetadataImportsResponse, MetadataImport> response = dataprocMetastoreClient.ListMetadataImportsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((MetadataImport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListMetadataImportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MetadataImport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MetadataImport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MetadataImport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMetadataImportsAsync(ServiceName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMetadataImportsResponse, MetadataImport> ListMetadataImportsAsync(ServiceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists imports in a service.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the service whose metadata imports to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListMetadataImportsResponse)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A pageable asynchronous sequence of [MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName parent = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    // Make the request
    PagedAsyncEnumerable<ListMetadataImportsResponse, MetadataImport> response = dataprocMetastoreClient.ListMetadataImportsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((MetadataImport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListMetadataImportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MetadataImport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MetadataImport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MetadataImport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMetadataImportsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMetadataImportsResponse, MetadataImport> ListMetadataImportsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists imports in a service.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the service whose metadata imports to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMetadataImportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListMetadataImportsResponse)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)` | A pageable asynchronous sequence of [MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    // Make the request
    PagedAsyncEnumerable<ListMetadataImportsResponse, MetadataImport> response = dataprocMetastoreClient.ListMetadataImportsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((MetadataImport item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListMetadataImportsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MetadataImport item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MetadataImport> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MetadataImport item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServices(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListServicesResponse, Service> ListServices(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists services in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location of metastore services to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A pageable sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListServicesResponse, Service> response = dataprocMetastoreClient.ListServices(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServices(ListServicesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListServicesResponse, Service> ListServices(ListServicesRequest request, CallSettings callSettings = null)

Lists services in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListServicesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A pageable sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ListServicesRequest request = new ListServicesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListServicesResponse, Service> response = dataprocMetastoreClient.ListServices(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServices(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListServicesResponse, Service> ListServices(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists services in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location of metastore services to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A pageable sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListServicesResponse, Service> response = dataprocMetastoreClient.ListServices(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Service item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServicesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServicesResponse, Service> ListServicesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists services in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location of metastore services to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A pageable asynchronous sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListServicesResponse, Service> response = dataprocMetastoreClient.ListServicesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Service item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListServicesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServicesAsync(ListServicesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServicesResponse, Service> ListServicesAsync(ListServicesRequest request, CallSettings callSettings = null)

Lists services in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListServicesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A pageable asynchronous sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ListServicesRequest request = new ListServicesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListServicesResponse, Service> response = dataprocMetastoreClient.ListServicesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Service item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListServicesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListServicesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListServicesResponse, Service> ListServicesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists services in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location of metastore services to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListServicesResponse)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)` | A pageable asynchronous sequence of [Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListServicesResponse, Service> response = dataprocMetastoreClient.ListServicesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Service item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListServicesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Service item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Service> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Service item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### MoveTableToDatabase(MoveTableToDatabaseRequest, CallSettings)
    
    
    public virtual Operation<MoveTableToDatabaseResponse, OperationMetadata> MoveTableToDatabase(MoveTableToDatabaseRequest request, CallSettings callSettings = null)

Move a table to another database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveTableToDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MoveTableToDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MoveTableToDatabaseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MoveTableToDatabaseResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    MoveTableToDatabaseRequest request = new MoveTableToDatabaseRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        TableName = "",
        DbName = "",
        DestinationDbName = "",
    };
    // Make the request
    Operation<MoveTableToDatabaseResponse, OperationMetadata> response = dataprocMetastoreClient.MoveTableToDatabase(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MoveTableToDatabaseResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MoveTableToDatabaseResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MoveTableToDatabaseResponse, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceMoveTableToDatabase(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MoveTableToDatabaseResponse retrievedResult = retrievedResponse.Result;
    }
    

### MoveTableToDatabaseAsync(MoveTableToDatabaseRequest, CallSettings)
    
    
    public virtual Task<Operation<MoveTableToDatabaseResponse, OperationMetadata>> MoveTableToDatabaseAsync(MoveTableToDatabaseRequest request, CallSettings callSettings = null)

Move a table to another database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveTableToDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MoveTableToDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MoveTableToDatabaseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MoveTableToDatabaseResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    MoveTableToDatabaseRequest request = new MoveTableToDatabaseRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        TableName = "",
        DbName = "",
        DestinationDbName = "",
    };
    // Make the request
    Operation<MoveTableToDatabaseResponse, OperationMetadata> response = await dataprocMetastoreClient.MoveTableToDatabaseAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MoveTableToDatabaseResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MoveTableToDatabaseResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MoveTableToDatabaseResponse, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceMoveTableToDatabaseAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MoveTableToDatabaseResponse retrievedResult = retrievedResponse.Result;
    }
    

### MoveTableToDatabaseAsync(MoveTableToDatabaseRequest, CancellationToken)
    
    
    public virtual Task<Operation<MoveTableToDatabaseResponse, OperationMetadata>> MoveTableToDatabaseAsync(MoveTableToDatabaseRequest request, CancellationToken cancellationToken)

Move a table to another database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveTableToDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MoveTableToDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MoveTableToDatabaseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MoveTableToDatabaseResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    MoveTableToDatabaseRequest request = new MoveTableToDatabaseRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        TableName = "",
        DbName = "",
        DestinationDbName = "",
    };
    // Make the request
    Operation<MoveTableToDatabaseResponse, OperationMetadata> response = await dataprocMetastoreClient.MoveTableToDatabaseAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MoveTableToDatabaseResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MoveTableToDatabaseResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MoveTableToDatabaseResponse, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceMoveTableToDatabaseAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MoveTableToDatabaseResponse retrievedResult = retrievedResponse.Result;
    }
    

### PollOnceAlterMetadataResourceLocation(string, CallSettings)
    
    
    public virtual Operation<AlterMetadataResourceLocationResponse, OperationMetadata> PollOnceAlterMetadataResourceLocation(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `AlterMetadataResourceLocation`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.AlterMetadataResourceLocationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceAlterMetadataResourceLocationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AlterMetadataResourceLocationResponse, OperationMetadata>> PollOnceAlterMetadataResourceLocationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `AlterMetadataResourceLocation`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.AlterMetadataResourceLocationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Backup)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateMetadataImport(string, CallSettings)
    
    
    public virtual Operation<MetadataImport, OperationMetadata> PollOnceCreateMetadataImport(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateMetadataImport` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateMetadataImportAsync(string, CallSettings)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> PollOnceCreateMetadataImportAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateMetadataImport`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateService(string, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> PollOnceCreateService(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateService`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> PollOnceCreateServiceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateService`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteService(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteService(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteService`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteServiceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteService`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceExportMetadata(string, CallSettings)
    
    
    public virtual Operation<MetadataExport, OperationMetadata> PollOnceExportMetadata(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ExportMetadata`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataExport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceExportMetadataAsync(string, CallSettings)
    
    
    public virtual Task<Operation<MetadataExport, OperationMetadata>> PollOnceExportMetadataAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ExportMetadata`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataExport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceMoveTableToDatabase(string, CallSettings)
    
    
    public virtual Operation<MoveTableToDatabaseResponse, OperationMetadata> PollOnceMoveTableToDatabase(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `MoveTableToDatabase` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MoveTableToDatabaseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MoveTableToDatabaseResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceMoveTableToDatabaseAsync(string, CallSettings)
    
    
    public virtual Task<Operation<MoveTableToDatabaseResponse, OperationMetadata>> PollOnceMoveTableToDatabaseAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `MoveTableToDatabase`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MoveTableToDatabaseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MoveTableToDatabaseResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceQueryMetadata(string, CallSettings)
    
    
    public virtual Operation<QueryMetadataResponse, OperationMetadata> PollOnceQueryMetadata(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `QueryMetadata`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[QueryMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.QueryMetadataResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceQueryMetadataAsync(string, CallSettings)
    
    
    public virtual Task<Operation<QueryMetadataResponse, OperationMetadata>> PollOnceQueryMetadataAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `QueryMetadata`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[QueryMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.QueryMetadataResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRestoreService(string, CallSettings)
    
    
    public virtual Operation<Restore, OperationMetadata> PollOnceRestoreService(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RestoreService`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRestoreServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Restore, OperationMetadata>> PollOnceRestoreServiceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RestoreService`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateMetadataImport(string, CallSettings)
    
    
    public virtual Operation<MetadataImport, OperationMetadata> PollOnceUpdateMetadataImport(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateMetadataImport` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateMetadataImportAsync(string, CallSettings)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> PollOnceUpdateMetadataImportAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateMetadataImport`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateService(string, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> PollOnceUpdateService(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateService`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateServiceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> PollOnceUpdateServiceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateService`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### QueryMetadata(QueryMetadataRequest, CallSettings)
    
    
    public virtual Operation<QueryMetadataResponse, OperationMetadata> QueryMetadata(QueryMetadataRequest request, CallSettings callSettings = null)

Query DPMS metadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.QueryMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[QueryMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.QueryMetadataResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    QueryMetadataRequest request = new QueryMetadataRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        Query = "",
    };
    // Make the request
    Operation<QueryMetadataResponse, OperationMetadata> response = dataprocMetastoreClient.QueryMetadata(request);
    
    // Poll until the returned long-running operation is complete
    Operation<QueryMetadataResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    QueryMetadataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<QueryMetadataResponse, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceQueryMetadata(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        QueryMetadataResponse retrievedResult = retrievedResponse.Result;
    }
    

### QueryMetadataAsync(QueryMetadataRequest, CallSettings)
    
    
    public virtual Task<Operation<QueryMetadataResponse, OperationMetadata>> QueryMetadataAsync(QueryMetadataRequest request, CallSettings callSettings = null)

Query DPMS metadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.QueryMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[QueryMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.QueryMetadataResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    QueryMetadataRequest request = new QueryMetadataRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        Query = "",
    };
    // Make the request
    Operation<QueryMetadataResponse, OperationMetadata> response = await dataprocMetastoreClient.QueryMetadataAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<QueryMetadataResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    QueryMetadataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<QueryMetadataResponse, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceQueryMetadataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        QueryMetadataResponse retrievedResult = retrievedResponse.Result;
    }
    

### QueryMetadataAsync(QueryMetadataRequest, CancellationToken)
    
    
    public virtual Task<Operation<QueryMetadataResponse, OperationMetadata>> QueryMetadataAsync(QueryMetadataRequest request, CancellationToken cancellationToken)

Query DPMS metadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.QueryMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[QueryMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.QueryMetadataResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    QueryMetadataRequest request = new QueryMetadataRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        Query = "",
    };
    // Make the request
    Operation<QueryMetadataResponse, OperationMetadata> response = await dataprocMetastoreClient.QueryMetadataAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<QueryMetadataResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    QueryMetadataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<QueryMetadataResponse, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceQueryMetadataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        QueryMetadataResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveIamPolicy(RemoveIamPolicyRequest, CallSettings)
    
    
    public virtual RemoveIamPolicyResponse RemoveIamPolicy(RemoveIamPolicyRequest request, CallSettings callSettings = null)

Removes the attached IAM policies for a resource

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RemoveIamPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveIamPolicyResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RemoveIamPolicyResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    RemoveIamPolicyRequest request = new RemoveIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Asynchronous = false,
    };
    // Make the request
    RemoveIamPolicyResponse response = dataprocMetastoreClient.RemoveIamPolicy(request);
    

### RemoveIamPolicyAsync(RemoveIamPolicyRequest, CallSettings)
    
    
    public virtual Task<RemoveIamPolicyResponse> RemoveIamPolicyAsync(RemoveIamPolicyRequest request, CallSettings callSettings = null)

Removes the attached IAM policies for a resource

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RemoveIamPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveIamPolicyResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RemoveIamPolicyResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    RemoveIamPolicyRequest request = new RemoveIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Asynchronous = false,
    };
    // Make the request
    RemoveIamPolicyResponse response = await dataprocMetastoreClient.RemoveIamPolicyAsync(request);
    

### RemoveIamPolicyAsync(RemoveIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<RemoveIamPolicyResponse> RemoveIamPolicyAsync(RemoveIamPolicyRequest request, CancellationToken cancellationToken)

Removes the attached IAM policies for a resource

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RemoveIamPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveIamPolicyResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RemoveIamPolicyResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    RemoveIamPolicyRequest request = new RemoveIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Asynchronous = false,
    };
    // Make the request
    RemoveIamPolicyResponse response = await dataprocMetastoreClient.RemoveIamPolicyAsync(request);
    

### RestoreService(RestoreServiceRequest, CallSettings)
    
    
    public virtual Operation<Restore, OperationMetadata> RestoreService(RestoreServiceRequest request, CallSettings callSettings = null)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RestoreServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    RestoreServiceRequest request = new RestoreServiceRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        BackupAsBackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
        RestoreType = Restore.Types.RestoreType.Unspecified,
        RequestId = "",
    };
    // Make the request
    Operation<Restore, OperationMetadata> response = dataprocMetastoreClient.RestoreService(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceRestoreService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### RestoreService(ServiceName, BackupName, CallSettings)
    
    
    public virtual Operation<Restore, OperationMetadata> RestoreService(ServiceName service, BackupName backup, CallSettings callSettings = null)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    ServiceName service = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    BackupName backup = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Operation<Restore, OperationMetadata> response = dataprocMetastoreClient.RestoreService(service, backup);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceRestoreService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### RestoreService(string, string, CallSettings)
    
    
    public virtual Operation<Restore, OperationMetadata> RestoreService(string service, string backup, CallSettings callSettings = null)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    string service = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    string backup = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Operation<Restore, OperationMetadata> response = dataprocMetastoreClient.RestoreService(service, backup);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceRestoreService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### RestoreServiceAsync(RestoreServiceRequest, CallSettings)
    
    
    public virtual Task<Operation<Restore, OperationMetadata>> RestoreServiceAsync(RestoreServiceRequest request, CallSettings callSettings = null)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RestoreServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    RestoreServiceRequest request = new RestoreServiceRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        BackupAsBackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
        RestoreType = Restore.Types.RestoreType.Unspecified,
        RequestId = "",
    };
    // Make the request
    Operation<Restore, OperationMetadata> response = await dataprocMetastoreClient.RestoreServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceRestoreServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### RestoreServiceAsync(RestoreServiceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Restore, OperationMetadata>> RestoreServiceAsync(RestoreServiceRequest request, CancellationToken cancellationToken)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.RestoreServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    RestoreServiceRequest request = new RestoreServiceRequest
    {
        ServiceAsServiceName = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]"),
        BackupAsBackupName = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]"),
        RestoreType = Restore.Types.RestoreType.Unspecified,
        RequestId = "",
    };
    // Make the request
    Operation<Restore, OperationMetadata> response = await dataprocMetastoreClient.RestoreServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceRestoreServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### RestoreServiceAsync(ServiceName, BackupName, CallSettings)
    
    
    public virtual Task<Operation<Restore, OperationMetadata>> RestoreServiceAsync(ServiceName service, BackupName backup, CallSettings callSettings = null)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName service = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    BackupName backup = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Operation<Restore, OperationMetadata> response = await dataprocMetastoreClient.RestoreServiceAsync(service, backup);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceRestoreServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### RestoreServiceAsync(ServiceName, BackupName, CancellationToken)
    
    
    public virtual Task<Operation<Restore, OperationMetadata>> RestoreServiceAsync(ServiceName service, BackupName backup, CancellationToken cancellationToken)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ServiceName)`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.BackupName)`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    ServiceName service = ServiceName.FromProjectLocationService("[PROJECT]", "[LOCATION]", "[SERVICE]");
    BackupName backup = BackupName.FromProjectLocationServiceBackup("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
    // Make the request
    Operation<Restore, OperationMetadata> response = await dataprocMetastoreClient.RestoreServiceAsync(service, backup);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceRestoreServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### RestoreServiceAsync(string, string, CallSettings)
    
    
    public virtual Task<Operation<Restore, OperationMetadata>> RestoreServiceAsync(string service, string backup, CallSettings callSettings = null)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string service = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    string backup = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Operation<Restore, OperationMetadata> response = await dataprocMetastoreClient.RestoreServiceAsync(service, backup);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceRestoreServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### RestoreServiceAsync(string, string, CancellationToken)
    
    
    public virtual Task<Operation<Restore, OperationMetadata>> RestoreServiceAsync(string service, string backup, CancellationToken cancellationToken)

Restores a service from a backup.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Restore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Restore)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    string service = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
    string backup = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/backups/[BACKUP]";
    // Make the request
    Operation<Restore, OperationMetadata> response = await dataprocMetastoreClient.RestoreServiceAsync(service, backup);
    
    // Poll until the returned long-running operation is complete
    Operation<Restore, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Restore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Restore, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceRestoreServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Restore retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient#Google_Cloud_Metastore_V1Beta_DataprocMetastoreClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient#Google_Cloud_Metastore_V1Beta_DataprocMetastoreClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient#Google_Cloud_Metastore_V1Beta_DataprocMetastoreClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreClient#Google_Cloud_Metastore_V1Beta_DataprocMetastoreClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateMetadataImport(MetadataImport, FieldMask, CallSettings)
    
    
    public virtual Operation<MetadataImport, OperationMetadata> UpdateMetadataImport(MetadataImport metadataImport, FieldMask updateMask, CallSettings callSettings = null)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

**Parameters**  
---  
**Name** | **Description**  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to update. The server only merges fields in the import if they are specified in `update_mask`. The metadata import's `name` field is used to identify the metastore import to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metadata import resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    MetadataImport metadataImport = new MetadataImport();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = dataprocMetastoreClient.UpdateMetadataImport(metadataImport, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceUpdateMetadataImport(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMetadataImport(UpdateMetadataImportRequest, CallSettings)
    
    
    public virtual Operation<MetadataImport, OperationMetadata> UpdateMetadataImport(UpdateMetadataImportRequest request, CallSettings callSettings = null)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    UpdateMetadataImportRequest request = new UpdateMetadataImportRequest
    {
        UpdateMask = new FieldMask(),
        MetadataImport = new MetadataImport(),
        RequestId = "",
    };
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = dataprocMetastoreClient.UpdateMetadataImport(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceUpdateMetadataImport(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMetadataImportAsync(MetadataImport, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> UpdateMetadataImportAsync(MetadataImport metadataImport, FieldMask updateMask, CallSettings callSettings = null)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

**Parameters**  
---  
**Name** | **Description**  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to update. The server only merges fields in the import if they are specified in `update_mask`. The metadata import's `name` field is used to identify the metastore import to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metadata import resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    MetadataImport metadataImport = new MetadataImport();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.UpdateMetadataImportAsync(metadataImport, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceUpdateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMetadataImportAsync(MetadataImport, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> UpdateMetadataImportAsync(MetadataImport metadataImport, FieldMask updateMask, CancellationToken cancellationToken)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

**Parameters**  
---  
**Name** | **Description**  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)`  
Required. The metadata import to update. The server only merges fields in the import if they are specified in `update_mask`. The metadata import's `name` field is used to identify the metastore import to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metadata import resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    MetadataImport metadataImport = new MetadataImport();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.UpdateMetadataImportAsync(metadataImport, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceUpdateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMetadataImportAsync(UpdateMetadataImportRequest, CallSettings)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> UpdateMetadataImportAsync(UpdateMetadataImportRequest request, CallSettings callSettings = null)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateMetadataImportRequest request = new UpdateMetadataImportRequest
    {
        UpdateMask = new FieldMask(),
        MetadataImport = new MetadataImport(),
        RequestId = "",
    };
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.UpdateMetadataImportAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceUpdateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMetadataImportAsync(UpdateMetadataImportRequest, CancellationToken)
    
    
    public virtual Task<Operation<MetadataImport, OperationMetadata>> UpdateMetadataImportAsync(UpdateMetadataImportRequest request, CancellationToken cancellationToken)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMetadataImportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MetadataImport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.MetadataImport)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateMetadataImportRequest request = new UpdateMetadataImportRequest
    {
        UpdateMask = new FieldMask(),
        MetadataImport = new MetadataImport(),
        RequestId = "",
    };
    // Make the request
    Operation<MetadataImport, OperationMetadata> response = await dataprocMetastoreClient.UpdateMetadataImportAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MetadataImport, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MetadataImport result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MetadataImport, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceUpdateMetadataImportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MetadataImport retrievedResult = retrievedResponse.Result;
    }
    

### UpdateService(Service, FieldMask, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> UpdateService(Service service, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single service.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The metastore service to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore service's `name` field is used to identify the metastore service to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metastore service resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    Service service = new Service();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Service, OperationMetadata> response = dataprocMetastoreClient.UpdateService(service, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceUpdateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateService(UpdateServiceRequest, CallSettings)
    
    
    public virtual Operation<Service, OperationMetadata> UpdateService(UpdateServiceRequest request, CallSettings callSettings = null)

Updates the parameters of a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.Create();
    // Initialize request argument(s)
    UpdateServiceRequest request = new UpdateServiceRequest
    {
        UpdateMask = new FieldMask(),
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = dataprocMetastoreClient.UpdateService(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = dataprocMetastoreClient.PollOnceUpdateService(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateServiceAsync(Service, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> UpdateServiceAsync(Service service, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single service.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The metastore service to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore service's `name` field is used to identify the metastore service to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metastore service resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    Service service = new Service();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.UpdateServiceAsync(service, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceUpdateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateServiceAsync(Service, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> UpdateServiceAsync(Service service, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single service.

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)`  
Required. The metastore service to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore service's `name` field is used to identify the metastore service to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metastore service resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    Service service = new Service();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.UpdateServiceAsync(service, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceUpdateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateServiceAsync(UpdateServiceRequest, CallSettings)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> UpdateServiceAsync(UpdateServiceRequest request, CallSettings callSettings = null)

Updates the parameters of a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateServiceRequest request = new UpdateServiceRequest
    {
        UpdateMask = new FieldMask(),
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.UpdateServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceUpdateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

### UpdateServiceAsync(UpdateServiceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Service, OperationMetadata>> UpdateServiceAsync(UpdateServiceRequest request, CancellationToken cancellationToken)

Updates the parameters of a single service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Service)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreClient dataprocMetastoreClient = await DataprocMetastoreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateServiceRequest request = new UpdateServiceRequest
    {
        UpdateMask = new FieldMask(),
        Service = new Service(),
        RequestId = "",
    };
    // Make the request
    Operation<Service, OperationMetadata> response = await dataprocMetastoreClient.UpdateServiceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Service, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Service result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Service, OperationMetadata> retrievedResponse = await dataprocMetastoreClient.PollOnceUpdateServiceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Service retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
