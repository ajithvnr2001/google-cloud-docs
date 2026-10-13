---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient
title: Network Connectivity v1 API - Class DataTransferServiceClient (2.14.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:43.324069+00:00
---

# Network Connectivity v1 API - Class DataTransferServiceClient (2.14.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1 API - Class DataTransferServiceClient (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.14.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.13.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.12.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.11.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.10.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.9.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.8.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.7.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.6.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.5.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.4.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.3.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.2.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.1.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.0.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.2.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.1.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.0.0/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)


    
    
    public abstract class DataTransferServiceClient

Reference documentation and code samples for the Network Connectivity v1 API class DataTransferServiceClient.

DataTransferService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataTransferServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DataTransferServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClientImpl)

## Namespace

[Google.Cloud.NetworkConnectivity.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1)

## Assembly

Google.Cloud.NetworkConnectivity.V1.dll

## Remarks

DataTransferService is the service for the Data Transfer API.

## Properties 

### CreateDestinationOperationsClient
    
    
    public virtual OperationsClient CreateDestinationOperationsClient { get; }

The long-running operations client for `CreateDestination`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateMulticloudDataTransferConfigOperationsClient
    
    
    public virtual OperationsClient CreateMulticloudDataTransferConfigOperationsClient { get; }

The long-running operations client for `CreateMulticloudDataTransferConfig`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the DataTransferService service, which is a host of "networkconnectivity.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default DataTransferService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default DataTransferService scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteDestinationOperationsClient
    
    
    public virtual OperationsClient DeleteDestinationOperationsClient { get; }

The long-running operations client for `DeleteDestination`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteMulticloudDataTransferConfigOperationsClient
    
    
    public virtual OperationsClient DeleteMulticloudDataTransferConfigOperationsClient { get; }

The long-running operations client for `DeleteMulticloudDataTransferConfig`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual DataTransferService.DataTransferServiceClient GrpcClient { get; }

The underlying gRPC DataTransferService client

**Property Value**  
---  
**Type** | **Description**  
`[DataTransferService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferService)[DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferService.DataTransferServiceClient)` |   
  
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
  
### UpdateDestinationOperationsClient
    
    
    public virtual OperationsClient UpdateDestinationOperationsClient { get; }

The long-running operations client for `UpdateDestination`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateMulticloudDataTransferConfigOperationsClient
    
    
    public virtual OperationsClient UpdateMulticloudDataTransferConfigOperationsClient { get; }

The long-running operations client for `UpdateMulticloudDataTransferConfig`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static DataTransferServiceClient Create()

Synchronously creates a [DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataTransferServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)` | The created [DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DataTransferServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DataTransferServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient)` | The task representing the created [DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient).  
  
### CreateDestination(CreateDestinationRequest, CallSettings)
    
    
    public virtual Operation<Destination, OperationMetadata> CreateDestination(CreateDestinationRequest request, CallSettings callSettings = null)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CreateDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    CreateDestinationRequest request = new CreateDestinationRequest
    {
        ParentAsMulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
        DestinationId = "",
        Destination = new Destination(),
        RequestId = "",
    };
    // Make the request
    Operation<Destination, OperationMetadata> response = dataTransferServiceClient.CreateDestination(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceCreateDestination(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateDestination(MulticloudDataTransferConfigName, Destination, string, CallSettings)
    
    
    public virtual Operation<Destination, OperationMetadata> CreateDestination(MulticloudDataTransferConfigName parent, Destination destination, string destinationId, CallSettings callSettings = null)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the parent resource.  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to create.  
`destinationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `Destination` resource, which becomes the final component of the `Destination` resource name.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName parent = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    Destination destination = new Destination();
    string destinationId = "";
    // Make the request
    Operation<Destination, OperationMetadata> response = dataTransferServiceClient.CreateDestination(parent, destination, destinationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceCreateDestination(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateDestination(string, Destination, string, CallSettings)
    
    
    public virtual Operation<Destination, OperationMetadata> CreateDestination(string parent, Destination destination, string destinationId, CallSettings callSettings = null)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to create.  
`destinationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `Destination` resource, which becomes the final component of the `Destination` resource name.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    Destination destination = new Destination();
    string destinationId = "";
    // Make the request
    Operation<Destination, OperationMetadata> response = dataTransferServiceClient.CreateDestination(parent, destination, destinationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceCreateDestination(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateDestinationAsync(CreateDestinationRequest, CallSettings)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> CreateDestinationAsync(CreateDestinationRequest request, CallSettings callSettings = null)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CreateDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateDestinationRequest request = new CreateDestinationRequest
    {
        ParentAsMulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
        DestinationId = "",
        Destination = new Destination(),
        RequestId = "",
    };
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.CreateDestinationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateDestinationAsync(CreateDestinationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> CreateDestinationAsync(CreateDestinationRequest request, CancellationToken cancellationToken)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CreateDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateDestinationRequest request = new CreateDestinationRequest
    {
        ParentAsMulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
        DestinationId = "",
        Destination = new Destination(),
        RequestId = "",
    };
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.CreateDestinationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateDestinationAsync(MulticloudDataTransferConfigName, Destination, string, CallSettings)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> CreateDestinationAsync(MulticloudDataTransferConfigName parent, Destination destination, string destinationId, CallSettings callSettings = null)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the parent resource.  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to create.  
`destinationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `Destination` resource, which becomes the final component of the `Destination` resource name.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName parent = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    Destination destination = new Destination();
    string destinationId = "";
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.CreateDestinationAsync(parent, destination, destinationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateDestinationAsync(MulticloudDataTransferConfigName, Destination, string, CancellationToken)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> CreateDestinationAsync(MulticloudDataTransferConfigName parent, Destination destination, string destinationId, CancellationToken cancellationToken)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the parent resource.  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to create.  
`destinationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `Destination` resource, which becomes the final component of the `Destination` resource name.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName parent = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    Destination destination = new Destination();
    string destinationId = "";
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.CreateDestinationAsync(parent, destination, destinationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateDestinationAsync(string, Destination, string, CallSettings)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> CreateDestinationAsync(string parent, Destination destination, string destinationId, CallSettings callSettings = null)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to create.  
`destinationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `Destination` resource, which becomes the final component of the `Destination` resource name.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    Destination destination = new Destination();
    string destinationId = "";
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.CreateDestinationAsync(parent, destination, destinationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateDestinationAsync(string, Destination, string, CancellationToken)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> CreateDestinationAsync(string parent, Destination destination, string destinationId, CancellationToken cancellationToken)

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to create.  
`destinationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `Destination` resource, which becomes the final component of the `Destination` resource name.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    Destination destination = new Destination();
    string destinationId = "";
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.CreateDestinationAsync(parent, destination, destinationId);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfig(LocationName, MulticloudDataTransferConfig, string, CallSettings)
    
    
    public virtual Operation<MulticloudDataTransferConfig, OperationMetadata> CreateMulticloudDataTransferConfig(LocationName parent, MulticloudDataTransferConfig multicloudDataTransferConfig, string multicloudDataTransferConfigId, CallSettings callSettings = null)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource.  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to create.  
`multicloudDataTransferConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `MulticloudDataTransferConfig` resource, which becomes the final component of the `MulticloudDataTransferConfig` resource name.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    string multicloudDataTransferConfigId = "";
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = dataTransferServiceClient.CreateMulticloudDataTransferConfig(parent, multicloudDataTransferConfig, multicloudDataTransferConfigId);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfig(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfig(CreateMulticloudDataTransferConfigRequest, CallSettings)
    
    
    public virtual Operation<MulticloudDataTransferConfig, OperationMetadata> CreateMulticloudDataTransferConfig(CreateMulticloudDataTransferConfigRequest request, CallSettings callSettings = null)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CreateMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    CreateMulticloudDataTransferConfigRequest request = new CreateMulticloudDataTransferConfigRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        MulticloudDataTransferConfigId = "",
        MulticloudDataTransferConfig = new MulticloudDataTransferConfig(),
        RequestId = "",
    };
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = dataTransferServiceClient.CreateMulticloudDataTransferConfig(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfig(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfig(string, MulticloudDataTransferConfig, string, CallSettings)
    
    
    public virtual Operation<MulticloudDataTransferConfig, OperationMetadata> CreateMulticloudDataTransferConfig(string parent, MulticloudDataTransferConfig multicloudDataTransferConfig, string multicloudDataTransferConfigId, CallSettings callSettings = null)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to create.  
`multicloudDataTransferConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `MulticloudDataTransferConfig` resource, which becomes the final component of the `MulticloudDataTransferConfig` resource name.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    string multicloudDataTransferConfigId = "";
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = dataTransferServiceClient.CreateMulticloudDataTransferConfig(parent, multicloudDataTransferConfig, multicloudDataTransferConfigId);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfig(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfigAsync(LocationName, MulticloudDataTransferConfig, string, CallSettings)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> CreateMulticloudDataTransferConfigAsync(LocationName parent, MulticloudDataTransferConfig multicloudDataTransferConfig, string multicloudDataTransferConfigId, CallSettings callSettings = null)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource.  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to create.  
`multicloudDataTransferConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `MulticloudDataTransferConfig` resource, which becomes the final component of the `MulticloudDataTransferConfig` resource name.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    string multicloudDataTransferConfigId = "";
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.CreateMulticloudDataTransferConfigAsync(parent, multicloudDataTransferConfig, multicloudDataTransferConfigId);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfigAsync(LocationName, MulticloudDataTransferConfig, string, CancellationToken)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> CreateMulticloudDataTransferConfigAsync(LocationName parent, MulticloudDataTransferConfig multicloudDataTransferConfig, string multicloudDataTransferConfigId, CancellationToken cancellationToken)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource.  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to create.  
`multicloudDataTransferConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `MulticloudDataTransferConfig` resource, which becomes the final component of the `MulticloudDataTransferConfig` resource name.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    string multicloudDataTransferConfigId = "";
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.CreateMulticloudDataTransferConfigAsync(parent, multicloudDataTransferConfig, multicloudDataTransferConfigId);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfigAsync(CreateMulticloudDataTransferConfigRequest, CallSettings)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> CreateMulticloudDataTransferConfigAsync(CreateMulticloudDataTransferConfigRequest request, CallSettings callSettings = null)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CreateMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateMulticloudDataTransferConfigRequest request = new CreateMulticloudDataTransferConfigRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        MulticloudDataTransferConfigId = "",
        MulticloudDataTransferConfig = new MulticloudDataTransferConfig(),
        RequestId = "",
    };
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.CreateMulticloudDataTransferConfigAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfigAsync(CreateMulticloudDataTransferConfigRequest, CancellationToken)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> CreateMulticloudDataTransferConfigAsync(CreateMulticloudDataTransferConfigRequest request, CancellationToken cancellationToken)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CreateMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateMulticloudDataTransferConfigRequest request = new CreateMulticloudDataTransferConfigRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        MulticloudDataTransferConfigId = "",
        MulticloudDataTransferConfig = new MulticloudDataTransferConfig(),
        RequestId = "",
    };
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.CreateMulticloudDataTransferConfigAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfigAsync(string, MulticloudDataTransferConfig, string, CallSettings)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> CreateMulticloudDataTransferConfigAsync(string parent, MulticloudDataTransferConfig multicloudDataTransferConfig, string multicloudDataTransferConfigId, CallSettings callSettings = null)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to create.  
`multicloudDataTransferConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `MulticloudDataTransferConfig` resource, which becomes the final component of the `MulticloudDataTransferConfig` resource name.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    string multicloudDataTransferConfigId = "";
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.CreateMulticloudDataTransferConfigAsync(parent, multicloudDataTransferConfig, multicloudDataTransferConfigId);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### CreateMulticloudDataTransferConfigAsync(string, MulticloudDataTransferConfig, string, CancellationToken)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> CreateMulticloudDataTransferConfigAsync(string parent, MulticloudDataTransferConfig multicloudDataTransferConfig, string multicloudDataTransferConfigId, CancellationToken cancellationToken)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to create.  
`multicloudDataTransferConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the `MulticloudDataTransferConfig` resource, which becomes the final component of the `MulticloudDataTransferConfig` resource name.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    string multicloudDataTransferConfigId = "";
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.CreateMulticloudDataTransferConfigAsync(parent, multicloudDataTransferConfig, multicloudDataTransferConfigId);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceCreateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestination(DeleteDestinationRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDestination(DeleteDestinationRequest request, CallSettings callSettings = null)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DeleteDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    DeleteDestinationRequest request = new DeleteDestinationRequest
    {
        DestinationName = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]"),
        RequestId = "",
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = dataTransferServiceClient.DeleteDestination(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceDeleteDestination(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestination(DestinationName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDestination(DestinationName name, CallSettings callSettings = null)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DestinationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DestinationName)`  
Required. The name of the `Destination` resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    DestinationName name = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = dataTransferServiceClient.DeleteDestination(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceDeleteDestination(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestination(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDestination(string name, CallSettings callSettings = null)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `Destination` resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]/destinations/[DESTINATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = dataTransferServiceClient.DeleteDestination(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceDeleteDestination(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestinationAsync(DeleteDestinationRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDestinationAsync(DeleteDestinationRequest request, CallSettings callSettings = null)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DeleteDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDestinationRequest request = new DeleteDestinationRequest
    {
        DestinationName = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]"),
        RequestId = "",
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteDestinationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestinationAsync(DeleteDestinationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDestinationAsync(DeleteDestinationRequest request, CancellationToken cancellationToken)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DeleteDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDestinationRequest request = new DeleteDestinationRequest
    {
        DestinationName = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]"),
        RequestId = "",
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteDestinationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestinationAsync(DestinationName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDestinationAsync(DestinationName name, CallSettings callSettings = null)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DestinationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DestinationName)`  
Required. The name of the `Destination` resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    DestinationName name = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteDestinationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestinationAsync(DestinationName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDestinationAsync(DestinationName name, CancellationToken cancellationToken)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DestinationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DestinationName)`  
Required. The name of the `Destination` resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    DestinationName name = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteDestinationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestinationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDestinationAsync(string name, CallSettings callSettings = null)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `Destination` resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]/destinations/[DESTINATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteDestinationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDestinationAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDestinationAsync(string name, CancellationToken cancellationToken)

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `Destination` resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]/destinations/[DESTINATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteDestinationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfig(DeleteMulticloudDataTransferConfigRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteMulticloudDataTransferConfig(DeleteMulticloudDataTransferConfigRequest request, CallSettings callSettings = null)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DeleteMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    DeleteMulticloudDataTransferConfigRequest request = new DeleteMulticloudDataTransferConfigRequest
    {
        MulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
        RequestId = "",
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = dataTransferServiceClient.DeleteMulticloudDataTransferConfig(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfig(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfig(MulticloudDataTransferConfigName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteMulticloudDataTransferConfig(MulticloudDataTransferConfigName name, CallSettings callSettings = null)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the `MulticloudDataTransferConfig` resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName name = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    // Make the request
    Operation<Empty, OperationMetadata> response = dataTransferServiceClient.DeleteMulticloudDataTransferConfig(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfig(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfig(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteMulticloudDataTransferConfig(string name, CallSettings callSettings = null)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `MulticloudDataTransferConfig` resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    // Make the request
    Operation<Empty, OperationMetadata> response = dataTransferServiceClient.DeleteMulticloudDataTransferConfig(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfig(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfigAsync(DeleteMulticloudDataTransferConfigRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMulticloudDataTransferConfigAsync(DeleteMulticloudDataTransferConfigRequest request, CallSettings callSettings = null)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DeleteMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteMulticloudDataTransferConfigRequest request = new DeleteMulticloudDataTransferConfigRequest
    {
        MulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
        RequestId = "",
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteMulticloudDataTransferConfigAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfigAsync(DeleteMulticloudDataTransferConfigRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMulticloudDataTransferConfigAsync(DeleteMulticloudDataTransferConfigRequest request, CancellationToken cancellationToken)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DeleteMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteMulticloudDataTransferConfigRequest request = new DeleteMulticloudDataTransferConfigRequest
    {
        MulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
        RequestId = "",
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteMulticloudDataTransferConfigAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName name, CallSettings callSettings = null)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the `MulticloudDataTransferConfig` resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName name = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteMulticloudDataTransferConfigAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName name, CancellationToken cancellationToken)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the `MulticloudDataTransferConfig` resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName name = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteMulticloudDataTransferConfigAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfigAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMulticloudDataTransferConfigAsync(string name, CallSettings callSettings = null)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `MulticloudDataTransferConfig` resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteMulticloudDataTransferConfigAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMulticloudDataTransferConfigAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMulticloudDataTransferConfigAsync(string name, CancellationToken cancellationToken)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `MulticloudDataTransferConfig` resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await dataTransferServiceClient.DeleteMulticloudDataTransferConfigAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceDeleteMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetDestination(DestinationName, CallSettings)
    
    
    public virtual Destination GetDestination(DestinationName name, CallSettings callSettings = null)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DestinationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DestinationName)`  
Required. The name of the `Destination` resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    DestinationName name = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]");
    // Make the request
    Destination response = dataTransferServiceClient.GetDestination(name);
    

### GetDestination(GetDestinationRequest, CallSettings)
    
    
    public virtual Destination GetDestination(GetDestinationRequest request, CallSettings callSettings = null)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    GetDestinationRequest request = new GetDestinationRequest
    {
        DestinationName = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]"),
    };
    // Make the request
    Destination response = dataTransferServiceClient.GetDestination(request);
    

### GetDestination(string, CallSettings)
    
    
    public virtual Destination GetDestination(string name, CallSettings callSettings = null)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `Destination` resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]/destinations/[DESTINATION]";
    // Make the request
    Destination response = dataTransferServiceClient.GetDestination(name);
    

### GetDestinationAsync(DestinationName, CallSettings)
    
    
    public virtual Task<Destination> GetDestinationAsync(DestinationName name, CallSettings callSettings = null)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DestinationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DestinationName)`  
Required. The name of the `Destination` resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    DestinationName name = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]");
    // Make the request
    Destination response = await dataTransferServiceClient.GetDestinationAsync(name);
    

### GetDestinationAsync(DestinationName, CancellationToken)
    
    
    public virtual Task<Destination> GetDestinationAsync(DestinationName name, CancellationToken cancellationToken)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DestinationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DestinationName)`  
Required. The name of the `Destination` resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    DestinationName name = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]");
    // Make the request
    Destination response = await dataTransferServiceClient.GetDestinationAsync(name);
    

### GetDestinationAsync(GetDestinationRequest, CallSettings)
    
    
    public virtual Task<Destination> GetDestinationAsync(GetDestinationRequest request, CallSettings callSettings = null)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDestinationRequest request = new GetDestinationRequest
    {
        DestinationName = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]"),
    };
    // Make the request
    Destination response = await dataTransferServiceClient.GetDestinationAsync(request);
    

### GetDestinationAsync(GetDestinationRequest, CancellationToken)
    
    
    public virtual Task<Destination> GetDestinationAsync(GetDestinationRequest request, CancellationToken cancellationToken)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDestinationRequest request = new GetDestinationRequest
    {
        DestinationName = DestinationName.FromProjectLocationMulticloudDataTransferConfigDestination("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]"),
    };
    // Make the request
    Destination response = await dataTransferServiceClient.GetDestinationAsync(request);
    

### GetDestinationAsync(string, CallSettings)
    
    
    public virtual Task<Destination> GetDestinationAsync(string name, CallSettings callSettings = null)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `Destination` resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]/destinations/[DESTINATION]";
    // Make the request
    Destination response = await dataTransferServiceClient.GetDestinationAsync(name);
    

### GetDestinationAsync(string, CancellationToken)
    
    
    public virtual Task<Destination> GetDestinationAsync(string name, CancellationToken cancellationToken)

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `Destination` resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]/destinations/[DESTINATION]";
    // Make the request
    Destination response = await dataTransferServiceClient.GetDestinationAsync(name);
    

### GetMulticloudDataTransferConfig(GetMulticloudDataTransferConfigRequest, CallSettings)
    
    
    public virtual MulticloudDataTransferConfig GetMulticloudDataTransferConfig(GetMulticloudDataTransferConfigRequest request, CallSettings callSettings = null)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    GetMulticloudDataTransferConfigRequest request = new GetMulticloudDataTransferConfigRequest
    {
        MulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
    };
    // Make the request
    MulticloudDataTransferConfig response = dataTransferServiceClient.GetMulticloudDataTransferConfig(request);
    

### GetMulticloudDataTransferConfig(MulticloudDataTransferConfigName, CallSettings)
    
    
    public virtual MulticloudDataTransferConfig GetMulticloudDataTransferConfig(MulticloudDataTransferConfigName name, CallSettings callSettings = null)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the `MulticloudDataTransferConfig` resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName name = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    // Make the request
    MulticloudDataTransferConfig response = dataTransferServiceClient.GetMulticloudDataTransferConfig(name);
    

### GetMulticloudDataTransferConfig(string, CallSettings)
    
    
    public virtual MulticloudDataTransferConfig GetMulticloudDataTransferConfig(string name, CallSettings callSettings = null)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `MulticloudDataTransferConfig` resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    // Make the request
    MulticloudDataTransferConfig response = dataTransferServiceClient.GetMulticloudDataTransferConfig(name);
    

### GetMulticloudDataTransferConfigAsync(GetMulticloudDataTransferConfigRequest, CallSettings)
    
    
    public virtual Task<MulticloudDataTransferConfig> GetMulticloudDataTransferConfigAsync(GetMulticloudDataTransferConfigRequest request, CallSettings callSettings = null)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetMulticloudDataTransferConfigRequest request = new GetMulticloudDataTransferConfigRequest
    {
        MulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
    };
    // Make the request
    MulticloudDataTransferConfig response = await dataTransferServiceClient.GetMulticloudDataTransferConfigAsync(request);
    

### GetMulticloudDataTransferConfigAsync(GetMulticloudDataTransferConfigRequest, CancellationToken)
    
    
    public virtual Task<MulticloudDataTransferConfig> GetMulticloudDataTransferConfigAsync(GetMulticloudDataTransferConfigRequest request, CancellationToken cancellationToken)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetMulticloudDataTransferConfigRequest request = new GetMulticloudDataTransferConfigRequest
    {
        MulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
    };
    // Make the request
    MulticloudDataTransferConfig response = await dataTransferServiceClient.GetMulticloudDataTransferConfigAsync(request);
    

### GetMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName, CallSettings)
    
    
    public virtual Task<MulticloudDataTransferConfig> GetMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName name, CallSettings callSettings = null)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the `MulticloudDataTransferConfig` resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName name = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    // Make the request
    MulticloudDataTransferConfig response = await dataTransferServiceClient.GetMulticloudDataTransferConfigAsync(name);
    

### GetMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName, CancellationToken)
    
    
    public virtual Task<MulticloudDataTransferConfig> GetMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName name, CancellationToken cancellationToken)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the `MulticloudDataTransferConfig` resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName name = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    // Make the request
    MulticloudDataTransferConfig response = await dataTransferServiceClient.GetMulticloudDataTransferConfigAsync(name);
    

### GetMulticloudDataTransferConfigAsync(string, CallSettings)
    
    
    public virtual Task<MulticloudDataTransferConfig> GetMulticloudDataTransferConfigAsync(string name, CallSettings callSettings = null)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `MulticloudDataTransferConfig` resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    // Make the request
    MulticloudDataTransferConfig response = await dataTransferServiceClient.GetMulticloudDataTransferConfigAsync(name);
    

### GetMulticloudDataTransferConfigAsync(string, CancellationToken)
    
    
    public virtual Task<MulticloudDataTransferConfig> GetMulticloudDataTransferConfigAsync(string name, CancellationToken cancellationToken)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the `MulticloudDataTransferConfig` resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    // Make the request
    MulticloudDataTransferConfig response = await dataTransferServiceClient.GetMulticloudDataTransferConfigAsync(name);
    

### GetMulticloudDataTransferSupportedService(GetMulticloudDataTransferSupportedServiceRequest, CallSettings)
    
    
    public virtual MulticloudDataTransferSupportedService GetMulticloudDataTransferSupportedService(GetMulticloudDataTransferSupportedServiceRequest request, CallSettings callSettings = null)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetMulticloudDataTransferSupportedServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    GetMulticloudDataTransferSupportedServiceRequest request = new GetMulticloudDataTransferSupportedServiceRequest
    {
        MulticloudDataTransferSupportedServiceName = MulticloudDataTransferSupportedServiceName.FromProjectLocationMulticloudDataTransferSupportedService("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]"),
    };
    // Make the request
    MulticloudDataTransferSupportedService response = dataTransferServiceClient.GetMulticloudDataTransferSupportedService(request);
    

### GetMulticloudDataTransferSupportedService(MulticloudDataTransferSupportedServiceName, CallSettings)
    
    
    public virtual MulticloudDataTransferSupportedService GetMulticloudDataTransferSupportedService(MulticloudDataTransferSupportedServiceName name, CallSettings callSettings = null)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferSupportedServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedServiceName)`  
Required. The name of the service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    MulticloudDataTransferSupportedServiceName name = MulticloudDataTransferSupportedServiceName.FromProjectLocationMulticloudDataTransferSupportedService("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]");
    // Make the request
    MulticloudDataTransferSupportedService response = dataTransferServiceClient.GetMulticloudDataTransferSupportedService(name);
    

### GetMulticloudDataTransferSupportedService(string, CallSettings)
    
    
    public virtual MulticloudDataTransferSupportedService GetMulticloudDataTransferSupportedService(string name, CallSettings callSettings = null)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferSupportedServices/[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]";
    // Make the request
    MulticloudDataTransferSupportedService response = dataTransferServiceClient.GetMulticloudDataTransferSupportedService(name);
    

### GetMulticloudDataTransferSupportedServiceAsync(GetMulticloudDataTransferSupportedServiceRequest, CallSettings)
    
    
    public virtual Task<MulticloudDataTransferSupportedService> GetMulticloudDataTransferSupportedServiceAsync(GetMulticloudDataTransferSupportedServiceRequest request, CallSettings callSettings = null)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetMulticloudDataTransferSupportedServiceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetMulticloudDataTransferSupportedServiceRequest request = new GetMulticloudDataTransferSupportedServiceRequest
    {
        MulticloudDataTransferSupportedServiceName = MulticloudDataTransferSupportedServiceName.FromProjectLocationMulticloudDataTransferSupportedService("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]"),
    };
    // Make the request
    MulticloudDataTransferSupportedService response = await dataTransferServiceClient.GetMulticloudDataTransferSupportedServiceAsync(request);
    

### GetMulticloudDataTransferSupportedServiceAsync(GetMulticloudDataTransferSupportedServiceRequest, CancellationToken)
    
    
    public virtual Task<MulticloudDataTransferSupportedService> GetMulticloudDataTransferSupportedServiceAsync(GetMulticloudDataTransferSupportedServiceRequest request, CancellationToken cancellationToken)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.GetMulticloudDataTransferSupportedServiceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetMulticloudDataTransferSupportedServiceRequest request = new GetMulticloudDataTransferSupportedServiceRequest
    {
        MulticloudDataTransferSupportedServiceName = MulticloudDataTransferSupportedServiceName.FromProjectLocationMulticloudDataTransferSupportedService("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]"),
    };
    // Make the request
    MulticloudDataTransferSupportedService response = await dataTransferServiceClient.GetMulticloudDataTransferSupportedServiceAsync(request);
    

### GetMulticloudDataTransferSupportedServiceAsync(MulticloudDataTransferSupportedServiceName, CallSettings)
    
    
    public virtual Task<MulticloudDataTransferSupportedService> GetMulticloudDataTransferSupportedServiceAsync(MulticloudDataTransferSupportedServiceName name, CallSettings callSettings = null)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferSupportedServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedServiceName)`  
Required. The name of the service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferSupportedServiceName name = MulticloudDataTransferSupportedServiceName.FromProjectLocationMulticloudDataTransferSupportedService("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]");
    // Make the request
    MulticloudDataTransferSupportedService response = await dataTransferServiceClient.GetMulticloudDataTransferSupportedServiceAsync(name);
    

### GetMulticloudDataTransferSupportedServiceAsync(MulticloudDataTransferSupportedServiceName, CancellationToken)
    
    
    public virtual Task<MulticloudDataTransferSupportedService> GetMulticloudDataTransferSupportedServiceAsync(MulticloudDataTransferSupportedServiceName name, CancellationToken cancellationToken)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MulticloudDataTransferSupportedServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedServiceName)`  
Required. The name of the service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferSupportedServiceName name = MulticloudDataTransferSupportedServiceName.FromProjectLocationMulticloudDataTransferSupportedService("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]");
    // Make the request
    MulticloudDataTransferSupportedService response = await dataTransferServiceClient.GetMulticloudDataTransferSupportedServiceAsync(name);
    

### GetMulticloudDataTransferSupportedServiceAsync(string, CallSettings)
    
    
    public virtual Task<MulticloudDataTransferSupportedService> GetMulticloudDataTransferSupportedServiceAsync(string name, CallSettings callSettings = null)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferSupportedServices/[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]";
    // Make the request
    MulticloudDataTransferSupportedService response = await dataTransferServiceClient.GetMulticloudDataTransferSupportedServiceAsync(name);
    

### GetMulticloudDataTransferSupportedServiceAsync(string, CancellationToken)
    
    
    public virtual Task<MulticloudDataTransferSupportedService> GetMulticloudDataTransferSupportedServiceAsync(string name, CancellationToken cancellationToken)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferSupportedServices/[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]";
    // Make the request
    MulticloudDataTransferSupportedService response = await dataTransferServiceClient.GetMulticloudDataTransferSupportedServiceAsync(name);
    

### ListDestinations(ListDestinationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDestinationsResponse, Destination> ListDestinations(ListDestinationsRequest request, CallSettings callSettings = null)

Lists the `Destination` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDestinationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListDestinationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDestinationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListDestinationsResponse)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A pageable sequence of [Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    ListDestinationsRequest request = new ListDestinationsRequest
    {
        ParentAsMulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
        Filter = "",
        OrderBy = "",
        ReturnPartialSuccess = false,
    };
    // Make the request
    PagedEnumerable<ListDestinationsResponse, Destination> response = dataTransferServiceClient.ListDestinations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Destination item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDestinationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Destination item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Destination> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Destination item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDestinations(MulticloudDataTransferConfigName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDestinationsResponse, Destination> ListDestinations(MulticloudDataTransferConfigName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `Destination` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDestinationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListDestinationsResponse)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A pageable sequence of [Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName parent = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    // Make the request
    PagedEnumerable<ListDestinationsResponse, Destination> response = dataTransferServiceClient.ListDestinations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Destination item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDestinationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Destination item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Destination> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Destination item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDestinations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDestinationsResponse, Destination> ListDestinations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `Destination` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDestinationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListDestinationsResponse)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A pageable sequence of [Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    // Make the request
    PagedEnumerable<ListDestinationsResponse, Destination> response = dataTransferServiceClient.ListDestinations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Destination item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDestinationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Destination item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Destination> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Destination item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDestinationsAsync(ListDestinationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDestinationsResponse, Destination> ListDestinationsAsync(ListDestinationsRequest request, CallSettings callSettings = null)

Lists the `Destination` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDestinationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListDestinationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDestinationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListDestinationsResponse)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A pageable asynchronous sequence of [Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListDestinationsRequest request = new ListDestinationsRequest
    {
        ParentAsMulticloudDataTransferConfigName = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]"),
        Filter = "",
        OrderBy = "",
        ReturnPartialSuccess = false,
    };
    // Make the request
    PagedAsyncEnumerable<ListDestinationsResponse, Destination> response = dataTransferServiceClient.ListDestinationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Destination item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDestinationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Destination item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Destination> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Destination item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDestinationsAsync(MulticloudDataTransferConfigName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDestinationsResponse, Destination> ListDestinationsAsync(MulticloudDataTransferConfigName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `Destination` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[MulticloudDataTransferConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfigName)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDestinationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListDestinationsResponse)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A pageable asynchronous sequence of [Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfigName parent = MulticloudDataTransferConfigName.FromProjectLocationMulticloudDataTransferConfig("[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
    // Make the request
    PagedAsyncEnumerable<ListDestinationsResponse, Destination> response = dataTransferServiceClient.ListDestinationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Destination item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDestinationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Destination item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Destination> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Destination item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDestinationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDestinationsResponse, Destination> ListDestinationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `Destination` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDestinationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListDestinationsResponse)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)` | A pageable asynchronous sequence of [Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/multicloudDataTransferConfigs/[MULTICLOUD_DATA_TRANSFER_CONFIG]";
    // Make the request
    PagedAsyncEnumerable<ListDestinationsResponse, Destination> response = dataTransferServiceClient.ListDestinationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Destination item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDestinationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Destination item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Destination> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Destination item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferConfigs(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> ListMulticloudDataTransferConfigs(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferConfigsResponse)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A pageable sequence of [MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> response = dataTransferServiceClient.ListMulticloudDataTransferConfigs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MulticloudDataTransferConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMulticloudDataTransferConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferConfig> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferConfigs(ListMulticloudDataTransferConfigsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> ListMulticloudDataTransferConfigs(ListMulticloudDataTransferConfigsRequest request, CallSettings callSettings = null)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferConfigsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferConfigsResponse)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A pageable sequence of [MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    ListMulticloudDataTransferConfigsRequest request = new ListMulticloudDataTransferConfigsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
        ReturnPartialSuccess = false,
    };
    // Make the request
    PagedEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> response = dataTransferServiceClient.ListMulticloudDataTransferConfigs(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MulticloudDataTransferConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMulticloudDataTransferConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferConfig> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferConfigs(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> ListMulticloudDataTransferConfigs(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferConfigsResponse)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A pageable sequence of [MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> response = dataTransferServiceClient.ListMulticloudDataTransferConfigs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MulticloudDataTransferConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMulticloudDataTransferConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferConfig> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferConfigsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> ListMulticloudDataTransferConfigsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferConfigsResponse)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A pageable asynchronous sequence of [MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> response = dataTransferServiceClient.ListMulticloudDataTransferConfigsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MulticloudDataTransferConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMulticloudDataTransferConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferConfig> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferConfigsAsync(ListMulticloudDataTransferConfigsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> ListMulticloudDataTransferConfigsAsync(ListMulticloudDataTransferConfigsRequest request, CallSettings callSettings = null)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferConfigsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferConfigsResponse)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A pageable asynchronous sequence of [MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListMulticloudDataTransferConfigsRequest request = new ListMulticloudDataTransferConfigsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
        ReturnPartialSuccess = false,
    };
    // Make the request
    PagedAsyncEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> response = dataTransferServiceClient.ListMulticloudDataTransferConfigsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MulticloudDataTransferConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMulticloudDataTransferConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferConfig> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferConfigsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> ListMulticloudDataTransferConfigsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferConfigsResponse)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)` | A pageable asynchronous sequence of [MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListMulticloudDataTransferConfigsResponse, MulticloudDataTransferConfig> response = dataTransferServiceClient.ListMulticloudDataTransferConfigsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MulticloudDataTransferConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMulticloudDataTransferConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferConfig> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferSupportedServices(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> ListMulticloudDataTransferSupportedServices(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferSupportedServicesResponse)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A pageable sequence of [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> response = dataTransferServiceClient.ListMulticloudDataTransferSupportedServices(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MulticloudDataTransferSupportedService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMulticloudDataTransferSupportedServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferSupportedService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferSupportedService> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferSupportedService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferSupportedServices(ListMulticloudDataTransferSupportedServicesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> ListMulticloudDataTransferSupportedServices(ListMulticloudDataTransferSupportedServicesRequest request, CallSettings callSettings = null)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferSupportedServicesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferSupportedServicesResponse)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A pageable sequence of [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    ListMulticloudDataTransferSupportedServicesRequest request = new ListMulticloudDataTransferSupportedServicesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> response = dataTransferServiceClient.ListMulticloudDataTransferSupportedServices(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MulticloudDataTransferSupportedService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMulticloudDataTransferSupportedServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferSupportedService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferSupportedService> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferSupportedService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferSupportedServices(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> ListMulticloudDataTransferSupportedServices(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferSupportedServicesResponse)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A pageable sequence of [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> response = dataTransferServiceClient.ListMulticloudDataTransferSupportedServices(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MulticloudDataTransferSupportedService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMulticloudDataTransferSupportedServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferSupportedService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferSupportedService> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferSupportedService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferSupportedServicesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> ListMulticloudDataTransferSupportedServicesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferSupportedServicesResponse)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A pageable asynchronous sequence of [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> response = dataTransferServiceClient.ListMulticloudDataTransferSupportedServicesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MulticloudDataTransferSupportedService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMulticloudDataTransferSupportedServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferSupportedService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferSupportedService> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferSupportedService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferSupportedServicesAsync(ListMulticloudDataTransferSupportedServicesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> ListMulticloudDataTransferSupportedServicesAsync(ListMulticloudDataTransferSupportedServicesRequest request, CallSettings callSettings = null)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferSupportedServicesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferSupportedServicesResponse)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A pageable asynchronous sequence of [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListMulticloudDataTransferSupportedServicesRequest request = new ListMulticloudDataTransferSupportedServicesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> response = dataTransferServiceClient.ListMulticloudDataTransferSupportedServicesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MulticloudDataTransferSupportedService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMulticloudDataTransferSupportedServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferSupportedService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferSupportedService> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferSupportedService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMulticloudDataTransferSupportedServicesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> ListMulticloudDataTransferSupportedServicesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.ListMulticloudDataTransferSupportedServicesResponse)[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService)` | A pageable asynchronous sequence of [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferSupportedService) resources.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListMulticloudDataTransferSupportedServicesResponse, MulticloudDataTransferSupportedService> response = dataTransferServiceClient.ListMulticloudDataTransferSupportedServicesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MulticloudDataTransferSupportedService item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMulticloudDataTransferSupportedServicesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MulticloudDataTransferSupportedService item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MulticloudDataTransferSupportedService> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MulticloudDataTransferSupportedService item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateDestination(string, CallSettings)
    
    
    public virtual Operation<Destination, OperationMetadata> PollOnceCreateDestination(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateDestination` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateDestinationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> PollOnceCreateDestinationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateDestination`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateMulticloudDataTransferConfig(string, CallSettings)
    
    
    public virtual Operation<MulticloudDataTransferConfig, OperationMetadata> PollOnceCreateMulticloudDataTransferConfig(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateMulticloudDataTransferConfig`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateMulticloudDataTransferConfigAsync(string, CallSettings)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> PollOnceCreateMulticloudDataTransferConfigAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateMulticloudDataTransferConfig`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteDestination(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteDestination(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteDestination` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteDestinationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteDestinationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteDestination`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteMulticloudDataTransferConfig(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteMulticloudDataTransferConfig(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteMulticloudDataTransferConfig`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteMulticloudDataTransferConfigAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteMulticloudDataTransferConfigAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteMulticloudDataTransferConfig`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateDestination(string, CallSettings)
    
    
    public virtual Operation<Destination, OperationMetadata> PollOnceUpdateDestination(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateDestination` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateDestinationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> PollOnceUpdateDestinationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateDestination`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateMulticloudDataTransferConfig(string, CallSettings)
    
    
    public virtual Operation<MulticloudDataTransferConfig, OperationMetadata> PollOnceUpdateMulticloudDataTransferConfig(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateMulticloudDataTransferConfig`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateMulticloudDataTransferConfigAsync(string, CallSettings)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> PollOnceUpdateMulticloudDataTransferConfigAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateMulticloudDataTransferConfig`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient#Google_Cloud_NetworkConnectivity_V1_DataTransferServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient#Google_Cloud_NetworkConnectivity_V1_DataTransferServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient#Google_Cloud_NetworkConnectivity_V1_DataTransferServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient#Google_Cloud_NetworkConnectivity_V1_DataTransferServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateDestination(Destination, FieldMask, CallSettings)
    
    
    public virtual Operation<Destination, OperationMetadata> UpdateDestination(Destination destination, FieldMask updateMask, CallSettings callSettings = null)

Updates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. `FieldMask is used to specify the fields to be overwritten in the`Destination`resource by the update. The fields specified in`update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't specify a mask, all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    Destination destination = new Destination();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Destination, OperationMetadata> response = dataTransferServiceClient.UpdateDestination(destination, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceUpdateDestination(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDestination(UpdateDestinationRequest, CallSettings)
    
    
    public virtual Operation<Destination, OperationMetadata> UpdateDestination(UpdateDestinationRequest request, CallSettings callSettings = null)

Updates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.UpdateDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    UpdateDestinationRequest request = new UpdateDestinationRequest
    {
        UpdateMask = new FieldMask(),
        Destination = new Destination(),
        RequestId = "",
    };
    // Make the request
    Operation<Destination, OperationMetadata> response = dataTransferServiceClient.UpdateDestination(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceUpdateDestination(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDestinationAsync(Destination, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> UpdateDestinationAsync(Destination destination, FieldMask updateMask, CallSettings callSettings = null)

Updates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. `FieldMask is used to specify the fields to be overwritten in the`Destination`resource by the update. The fields specified in`update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't specify a mask, all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    Destination destination = new Destination();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.UpdateDestinationAsync(destination, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceUpdateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDestinationAsync(Destination, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> UpdateDestinationAsync(Destination destination, FieldMask updateMask, CancellationToken cancellationToken)

Updates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`destination` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)`  
Required. The `Destination` resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. `FieldMask is used to specify the fields to be overwritten in the`Destination`resource by the update. The fields specified in`update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't specify a mask, all fields are overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    Destination destination = new Destination();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.UpdateDestinationAsync(destination, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceUpdateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDestinationAsync(UpdateDestinationRequest, CallSettings)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> UpdateDestinationAsync(UpdateDestinationRequest request, CallSettings callSettings = null)

Updates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.UpdateDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDestinationRequest request = new UpdateDestinationRequest
    {
        UpdateMask = new FieldMask(),
        Destination = new Destination(),
        RequestId = "",
    };
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.UpdateDestinationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceUpdateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDestinationAsync(UpdateDestinationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Destination, OperationMetadata>> UpdateDestinationAsync(UpdateDestinationRequest request, CancellationToken cancellationToken)

Updates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDestinationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.UpdateDestinationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.Destination)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDestinationRequest request = new UpdateDestinationRequest
    {
        UpdateMask = new FieldMask(),
        Destination = new Destination(),
        RequestId = "",
    };
    // Make the request
    Operation<Destination, OperationMetadata> response = await dataTransferServiceClient.UpdateDestinationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Destination, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Destination result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Destination, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceUpdateDestinationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Destination retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMulticloudDataTransferConfig(MulticloudDataTransferConfig, FieldMask, CallSettings)
    
    
    public virtual Operation<MulticloudDataTransferConfig, OperationMetadata> UpdateMulticloudDataTransferConfig(MulticloudDataTransferConfig multicloudDataTransferConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. `FieldMask` is used to specify the fields in the `MulticloudDataTransferConfig` resource to be overwritten by the update. The fields specified in `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't specify a mask, all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = dataTransferServiceClient.UpdateMulticloudDataTransferConfig(multicloudDataTransferConfig, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceUpdateMulticloudDataTransferConfig(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMulticloudDataTransferConfig(UpdateMulticloudDataTransferConfigRequest, CallSettings)
    
    
    public virtual Operation<MulticloudDataTransferConfig, OperationMetadata> UpdateMulticloudDataTransferConfig(UpdateMulticloudDataTransferConfigRequest request, CallSettings callSettings = null)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.UpdateMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.Create();
    // Initialize request argument(s)
    UpdateMulticloudDataTransferConfigRequest request = new UpdateMulticloudDataTransferConfigRequest
    {
        UpdateMask = new FieldMask(),
        MulticloudDataTransferConfig = new MulticloudDataTransferConfig(),
        RequestId = "",
    };
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = dataTransferServiceClient.UpdateMulticloudDataTransferConfig(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = dataTransferServiceClient.PollOnceUpdateMulticloudDataTransferConfig(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMulticloudDataTransferConfigAsync(MulticloudDataTransferConfig, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> UpdateMulticloudDataTransferConfigAsync(MulticloudDataTransferConfig multicloudDataTransferConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. `FieldMask` is used to specify the fields in the `MulticloudDataTransferConfig` resource to be overwritten by the update. The fields specified in `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't specify a mask, all fields are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.UpdateMulticloudDataTransferConfigAsync(multicloudDataTransferConfig, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceUpdateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMulticloudDataTransferConfigAsync(MulticloudDataTransferConfig, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> UpdateMulticloudDataTransferConfigAsync(MulticloudDataTransferConfig multicloudDataTransferConfig, FieldMask updateMask, CancellationToken cancellationToken)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. `FieldMask` is used to specify the fields in the `MulticloudDataTransferConfig` resource to be overwritten by the update. The fields specified in `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't specify a mask, all fields are overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    MulticloudDataTransferConfig multicloudDataTransferConfig = new MulticloudDataTransferConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.UpdateMulticloudDataTransferConfigAsync(multicloudDataTransferConfig, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceUpdateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMulticloudDataTransferConfigAsync(UpdateMulticloudDataTransferConfigRequest, CallSettings)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> UpdateMulticloudDataTransferConfigAsync(UpdateMulticloudDataTransferConfigRequest request, CallSettings callSettings = null)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.UpdateMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateMulticloudDataTransferConfigRequest request = new UpdateMulticloudDataTransferConfigRequest
    {
        UpdateMask = new FieldMask(),
        MulticloudDataTransferConfig = new MulticloudDataTransferConfig(),
        RequestId = "",
    };
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.UpdateMulticloudDataTransferConfigAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceUpdateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMulticloudDataTransferConfigAsync(UpdateMulticloudDataTransferConfigRequest, CancellationToken)
    
    
    public virtual Task<Operation<MulticloudDataTransferConfig, OperationMetadata>> UpdateMulticloudDataTransferConfigAsync(UpdateMulticloudDataTransferConfigRequest request, CancellationToken cancellationToken)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.UpdateMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[MulticloudDataTransferConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.MulticloudDataTransferConfig)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DataTransferServiceClient dataTransferServiceClient = await DataTransferServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateMulticloudDataTransferConfigRequest request = new UpdateMulticloudDataTransferConfigRequest
    {
        UpdateMask = new FieldMask(),
        MulticloudDataTransferConfig = new MulticloudDataTransferConfig(),
        RequestId = "",
    };
    // Make the request
    Operation<MulticloudDataTransferConfig, OperationMetadata> response = await dataTransferServiceClient.UpdateMulticloudDataTransferConfigAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<MulticloudDataTransferConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    MulticloudDataTransferConfig result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<MulticloudDataTransferConfig, OperationMetadata> retrievedResponse = await dataTransferServiceClient.PollOnceUpdateMulticloudDataTransferConfigAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        MulticloudDataTransferConfig retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
