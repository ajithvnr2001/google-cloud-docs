---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient
title: Dataproc Metastore v1beta API - Class DataprocMetastoreFederationClient (2.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:19.685559+00:00
---

# Dataproc Metastore v1beta API - Class DataprocMetastoreFederationClient (2.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1beta API - Class DataprocMetastoreFederationClient (2.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient)
  * [ 2.0.0-beta11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/2.0.0-beta11/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/1.0.0-beta02/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient)


    
    
    public abstract class DataprocMetastoreFederationClient

Reference documentation and code samples for the Dataproc Metastore v1beta API class DataprocMetastoreFederationClient.

DataprocMetastoreFederation client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataprocMetastoreFederationClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DataprocMetastoreFederationClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClientImpl)

## Namespace

[Google.Cloud.Metastore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta)

## Assembly

Google.Cloud.Metastore.V1Beta.dll

## Remarks

Configures and manages metastore federation services. Dataproc Metastore Federation Service allows federating a collection of backend metastores like BigQuery, Dataplex Lakes, and other Dataproc Metastores. The Federation Service exposes a gRPC URL through which metadata from the backend metastores are served at query time.

The Dataproc Metastore Federation API defines the following resource model:

  * The service works with a collection of Google Cloud projects.
  * Each project has a collection of available locations.
  * Each location has a collection of federations.
  * Dataproc Metastore Federations are resources with names of the form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.



## Properties 

### CreateFederationOperationsClient
    
    
    public virtual OperationsClient CreateFederationOperationsClient { get; }

The long-running operations client for `CreateFederation`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the DataprocMetastoreFederation service, which is a host of "metastore.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default DataprocMetastoreFederation scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default DataprocMetastoreFederation scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteFederationOperationsClient
    
    
    public virtual OperationsClient DeleteFederationOperationsClient { get; }

The long-running operations client for `DeleteFederation`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual DataprocMetastoreFederation.DataprocMetastoreFederationClient GrpcClient { get; }

The underlying gRPC DataprocMetastoreFederation client

**Property Value**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederation)[DataprocMetastoreFederationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederation.DataprocMetastoreFederationClient)` |   
  
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
  
### UpdateFederationOperationsClient
    
    
    public virtual OperationsClient UpdateFederationOperationsClient { get; }

The long-running operations client for `UpdateFederation`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static DataprocMetastoreFederationClient Create()

Synchronously creates a [DataprocMetastoreFederationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataprocMetastoreFederationClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient)` | The created [DataprocMetastoreFederationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DataprocMetastoreFederationClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DataprocMetastoreFederationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataprocMetastoreFederationClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataprocMetastoreFederationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient)` | The task representing the created [DataprocMetastoreFederationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient).  
  
### CreateFederation(LocationName, Federation, string, CallSettings)
    
    
    public virtual Operation<Federation, OperationMetadata> CreateFederation(LocationName parent, Federation federation, string federationId, CallSettings callSettings = null)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location in which to create a federation service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Federation federation = new Federation();
    string federationId = "";
    // Make the request
    Operation<Federation, OperationMetadata> response = dataprocMetastoreFederationClient.CreateFederation(parent, federation, federationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = dataprocMetastoreFederationClient.PollOnceCreateFederation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFederation(CreateFederationRequest, CallSettings)
    
    
    public virtual Operation<Federation, OperationMetadata> CreateFederation(CreateFederationRequest request, CallSettings callSettings = null)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateFederationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    CreateFederationRequest request = new CreateFederationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FederationId = "",
        Federation = new Federation(),
        RequestId = "",
    };
    // Make the request
    Operation<Federation, OperationMetadata> response = dataprocMetastoreFederationClient.CreateFederation(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = dataprocMetastoreFederationClient.PollOnceCreateFederation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFederation(string, Federation, string, CallSettings)
    
    
    public virtual Operation<Federation, OperationMetadata> CreateFederation(string parent, Federation federation, string federationId, CallSettings callSettings = null)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location in which to create a federation service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Federation federation = new Federation();
    string federationId = "";
    // Make the request
    Operation<Federation, OperationMetadata> response = dataprocMetastoreFederationClient.CreateFederation(parent, federation, federationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = dataprocMetastoreFederationClient.PollOnceCreateFederation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFederationAsync(LocationName, Federation, string, CallSettings)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> CreateFederationAsync(LocationName parent, Federation federation, string federationId, CallSettings callSettings = null)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location in which to create a federation service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Federation federation = new Federation();
    string federationId = "";
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.CreateFederationAsync(parent, federation, federationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceCreateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFederationAsync(LocationName, Federation, string, CancellationToken)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> CreateFederationAsync(LocationName parent, Federation federation, string federationId, CancellationToken cancellationToken)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location in which to create a federation service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Federation federation = new Federation();
    string federationId = "";
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.CreateFederationAsync(parent, federation, federationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceCreateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFederationAsync(CreateFederationRequest, CallSettings)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> CreateFederationAsync(CreateFederationRequest request, CallSettings callSettings = null)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateFederationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    CreateFederationRequest request = new CreateFederationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FederationId = "",
        Federation = new Federation(),
        RequestId = "",
    };
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.CreateFederationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceCreateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFederationAsync(CreateFederationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> CreateFederationAsync(CreateFederationRequest request, CancellationToken cancellationToken)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.CreateFederationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    CreateFederationRequest request = new CreateFederationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FederationId = "",
        Federation = new Federation(),
        RequestId = "",
    };
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.CreateFederationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceCreateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFederationAsync(string, Federation, string, CallSettings)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> CreateFederationAsync(string parent, Federation federation, string federationId, CallSettings callSettings = null)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location in which to create a federation service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Federation federation = new Federation();
    string federationId = "";
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.CreateFederationAsync(parent, federation, federationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceCreateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### CreateFederationAsync(string, Federation, string, CancellationToken)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> CreateFederationAsync(string parent, Federation federation, string federationId, CancellationToken cancellationToken)

Creates a metastore federation in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location in which to create a federation service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Federation federation = new Federation();
    string federationId = "";
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.CreateFederationAsync(parent, federation, federationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceCreateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederation(DeleteFederationRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFederation(DeleteFederationRequest request, CallSettings callSettings = null)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteFederationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    DeleteFederationRequest request = new DeleteFederationRequest
    {
        FederationName = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreFederationClient.DeleteFederation(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreFederationClient.PollOnceDeleteFederation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederation(FederationName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFederation(FederationName name, CallSettings callSettings = null)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.FederationName)`  
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    FederationName name = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreFederationClient.DeleteFederation(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreFederationClient.PollOnceDeleteFederation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederation(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFederation(string name, CallSettings callSettings = null)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/federations/[FEDERATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = dataprocMetastoreFederationClient.DeleteFederation(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataprocMetastoreFederationClient.PollOnceDeleteFederation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederationAsync(DeleteFederationRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFederationAsync(DeleteFederationRequest request, CallSettings callSettings = null)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteFederationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFederationRequest request = new DeleteFederationRequest
    {
        FederationName = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreFederationClient.DeleteFederationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceDeleteFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederationAsync(DeleteFederationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFederationAsync(DeleteFederationRequest request, CancellationToken cancellationToken)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DeleteFederationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFederationRequest request = new DeleteFederationRequest
    {
        FederationName = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreFederationClient.DeleteFederationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceDeleteFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederationAsync(FederationName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFederationAsync(FederationName name, CallSettings callSettings = null)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.FederationName)`  
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    FederationName name = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreFederationClient.DeleteFederationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceDeleteFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederationAsync(FederationName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFederationAsync(FederationName name, CancellationToken cancellationToken)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.FederationName)`  
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    FederationName name = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreFederationClient.DeleteFederationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceDeleteFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFederationAsync(string name, CallSettings callSettings = null)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/federations/[FEDERATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreFederationClient.DeleteFederationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceDeleteFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFederationAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFederationAsync(string name, CancellationToken cancellationToken)

Deletes a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/federations/[FEDERATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataprocMetastoreFederationClient.DeleteFederationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceDeleteFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetFederation(FederationName, CallSettings)
    
    
    public virtual Federation GetFederation(FederationName name, CallSettings callSettings = null)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.FederationName)`  
Required. The relative resource name of the metastore federation to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    FederationName name = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]");
    // Make the request
    Federation response = dataprocMetastoreFederationClient.GetFederation(name);
    

### GetFederation(GetFederationRequest, CallSettings)
    
    
    public virtual Federation GetFederation(GetFederationRequest request, CallSettings callSettings = null)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    GetFederationRequest request = new GetFederationRequest
    {
        FederationName = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]"),
    };
    // Make the request
    Federation response = dataprocMetastoreFederationClient.GetFederation(request);
    

### GetFederation(string, CallSettings)
    
    
    public virtual Federation GetFederation(string name, CallSettings callSettings = null)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore federation to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/federations/[FEDERATION]";
    // Make the request
    Federation response = dataprocMetastoreFederationClient.GetFederation(name);
    

### GetFederationAsync(FederationName, CallSettings)
    
    
    public virtual Task<Federation> GetFederationAsync(FederationName name, CallSettings callSettings = null)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.FederationName)`  
Required. The relative resource name of the metastore federation to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    FederationName name = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]");
    // Make the request
    Federation response = await dataprocMetastoreFederationClient.GetFederationAsync(name);
    

### GetFederationAsync(FederationName, CancellationToken)
    
    
    public virtual Task<Federation> GetFederationAsync(FederationName name, CancellationToken cancellationToken)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.FederationName)`  
Required. The relative resource name of the metastore federation to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    FederationName name = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]");
    // Make the request
    Federation response = await dataprocMetastoreFederationClient.GetFederationAsync(name);
    

### GetFederationAsync(GetFederationRequest, CallSettings)
    
    
    public virtual Task<Federation> GetFederationAsync(GetFederationRequest request, CallSettings callSettings = null)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    GetFederationRequest request = new GetFederationRequest
    {
        FederationName = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]"),
    };
    // Make the request
    Federation response = await dataprocMetastoreFederationClient.GetFederationAsync(request);
    

### GetFederationAsync(GetFederationRequest, CancellationToken)
    
    
    public virtual Task<Federation> GetFederationAsync(GetFederationRequest request, CancellationToken cancellationToken)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.GetFederationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    GetFederationRequest request = new GetFederationRequest
    {
        FederationName = FederationName.FromProjectLocationFederation("[PROJECT]", "[LOCATION]", "[FEDERATION]"),
    };
    // Make the request
    Federation response = await dataprocMetastoreFederationClient.GetFederationAsync(request);
    

### GetFederationAsync(string, CallSettings)
    
    
    public virtual Task<Federation> GetFederationAsync(string name, CallSettings callSettings = null)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore federation to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/federations/[FEDERATION]";
    // Make the request
    Federation response = await dataprocMetastoreFederationClient.GetFederationAsync(name);
    

### GetFederationAsync(string, CancellationToken)
    
    
    public virtual Task<Federation> GetFederationAsync(string name, CancellationToken cancellationToken)

Gets the details of a single federation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the metastore federation to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/federations/[FEDERATION]";
    // Make the request
    Federation response = await dataprocMetastoreFederationClient.GetFederationAsync(name);
    

### ListFederations(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFederationsResponse, Federation> ListFederations(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists federations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location of metastore federations to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFederationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListFederationsResponse)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A pageable sequence of [Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListFederationsResponse, Federation> response = dataprocMetastoreFederationClient.ListFederations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Federation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFederationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Federation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Federation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Federation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFederations(ListFederationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFederationsResponse, Federation> ListFederations(ListFederationsRequest request, CallSettings callSettings = null)

Lists federations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFederationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListFederationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFederationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListFederationsResponse)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A pageable sequence of [Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    ListFederationsRequest request = new ListFederationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFederationsResponse, Federation> response = dataprocMetastoreFederationClient.ListFederations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Federation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFederationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Federation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Federation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Federation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFederations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFederationsResponse, Federation> ListFederations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists federations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location of metastore federations to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFederationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListFederationsResponse)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A pageable sequence of [Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListFederationsResponse, Federation> response = dataprocMetastoreFederationClient.ListFederations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Federation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFederationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Federation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Federation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Federation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFederationsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFederationsResponse, Federation> ListFederationsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists federations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The relative resource name of the location of metastore federations to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFederationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListFederationsResponse)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A pageable asynchronous sequence of [Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListFederationsResponse, Federation> response = dataprocMetastoreFederationClient.ListFederationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Federation item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListFederationsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Federation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Federation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Federation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFederationsAsync(ListFederationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFederationsResponse, Federation> ListFederationsAsync(ListFederationsRequest request, CallSettings callSettings = null)

Lists federations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFederationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListFederationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFederationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListFederationsResponse)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A pageable asynchronous sequence of [Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    ListFederationsRequest request = new ListFederationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFederationsResponse, Federation> response = dataprocMetastoreFederationClient.ListFederationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Federation item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListFederationsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Federation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Federation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Federation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFederationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFederationsResponse, Federation> ListFederationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists federations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The relative resource name of the location of metastore federations to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFederationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.ListFederationsResponse)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)` | A pageable asynchronous sequence of [Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation) resources.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListFederationsResponse, Federation> response = dataprocMetastoreFederationClient.ListFederationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Federation item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListFederationsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Federation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Federation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Federation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateFederation(string, CallSettings)
    
    
    public virtual Operation<Federation, OperationMetadata> PollOnceCreateFederation(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFederation`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFederationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> PollOnceCreateFederationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFederation`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFederation(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteFederation(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFederation`.

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
  
### PollOnceDeleteFederationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteFederationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFederation`.

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
  
### PollOnceUpdateFederation(string, CallSettings)
    
    
    public virtual Operation<Federation, OperationMetadata> PollOnceUpdateFederation(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFederation`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFederationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> PollOnceUpdateFederationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFederation`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient#Google_Cloud_Metastore_V1Beta_DataprocMetastoreFederationClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient#Google_Cloud_Metastore_V1Beta_DataprocMetastoreFederationClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient#Google_Cloud_Metastore_V1Beta_DataprocMetastoreFederationClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.DataprocMetastoreFederationClient#Google_Cloud_Metastore_V1Beta_DataprocMetastoreFederationClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateFederation(Federation, FieldMask, CallSettings)
    
    
    public virtual Operation<Federation, OperationMetadata> UpdateFederation(Federation federation, FieldMask updateMask, CallSettings callSettings = null)

Updates the fields of a federation.

**Parameters**  
---  
**Name** | **Description**  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore federation's `name` field is used to identify the metastore service to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    Federation federation = new Federation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Federation, OperationMetadata> response = dataprocMetastoreFederationClient.UpdateFederation(federation, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = dataprocMetastoreFederationClient.PollOnceUpdateFederation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFederation(UpdateFederationRequest, CallSettings)
    
    
    public virtual Operation<Federation, OperationMetadata> UpdateFederation(UpdateFederationRequest request, CallSettings callSettings = null)

Updates the fields of a federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateFederationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = DataprocMetastoreFederationClient.Create();
    // Initialize request argument(s)
    UpdateFederationRequest request = new UpdateFederationRequest
    {
        UpdateMask = new FieldMask(),
        Federation = new Federation(),
        RequestId = "",
    };
    // Make the request
    Operation<Federation, OperationMetadata> response = dataprocMetastoreFederationClient.UpdateFederation(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = dataprocMetastoreFederationClient.PollOnceUpdateFederation(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFederationAsync(Federation, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> UpdateFederationAsync(Federation federation, FieldMask updateMask, CallSettings callSettings = null)

Updates the fields of a federation.

**Parameters**  
---  
**Name** | **Description**  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore federation's `name` field is used to identify the metastore service to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    Federation federation = new Federation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.UpdateFederationAsync(federation, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceUpdateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFederationAsync(Federation, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> UpdateFederationAsync(Federation federation, FieldMask updateMask, CancellationToken cancellationToken)

Updates the fields of a federation.

**Parameters**  
---  
**Name** | **Description**  
`federation` | `[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)`  
Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore federation's `name` field is used to identify the metastore service to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    Federation federation = new Federation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.UpdateFederationAsync(federation, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceUpdateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFederationAsync(UpdateFederationRequest, CallSettings)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> UpdateFederationAsync(UpdateFederationRequest request, CallSettings callSettings = null)

Updates the fields of a federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateFederationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFederationRequest request = new UpdateFederationRequest
    {
        UpdateMask = new FieldMask(),
        Federation = new Federation(),
        RequestId = "",
    };
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.UpdateFederationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceUpdateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFederationAsync(UpdateFederationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Federation, OperationMetadata>> UpdateFederationAsync(UpdateFederationRequest request, CancellationToken cancellationToken)

Updates the fields of a federation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFederationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.UpdateFederationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Federation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.Federation)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Beta/latest/Google.Cloud.Metastore.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataprocMetastoreFederationClient dataprocMetastoreFederationClient = await DataprocMetastoreFederationClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFederationRequest request = new UpdateFederationRequest
    {
        UpdateMask = new FieldMask(),
        Federation = new Federation(),
        RequestId = "",
    };
    // Make the request
    Operation<Federation, OperationMetadata> response = await dataprocMetastoreFederationClient.UpdateFederationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Federation, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Federation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Federation, OperationMetadata> retrievedResponse = await dataprocMetastoreFederationClient.PollOnceUpdateFederationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Federation retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
