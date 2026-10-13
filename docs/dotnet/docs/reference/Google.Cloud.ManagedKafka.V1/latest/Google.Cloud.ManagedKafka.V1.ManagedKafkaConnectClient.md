---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient
title: Managed Service for Apache Kafka API v1 API - Class ManagedKafkaConnectClient (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:52.761036+00:00
---

# Managed Service for Apache Kafka API v1 API - Class ManagedKafkaConnectClient (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class ManagedKafkaConnectClient (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient)


    
    
    public abstract class ManagedKafkaConnectClient

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class ManagedKafkaConnectClient.

ManagedKafkaConnect client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ManagedKafkaConnectClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ManagedKafkaConnectClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClientImpl)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Remarks

The service that a client application uses to manage Apache Kafka Connect clusters and connectors.

## Properties 

### CreateConnectClusterOperationsClient
    
    
    public virtual OperationsClient CreateConnectClusterOperationsClient { get; }

The long-running operations client for `CreateConnectCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ManagedKafkaConnect service, which is a host of "managedkafka.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ManagedKafkaConnect scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ManagedKafkaConnect scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteConnectClusterOperationsClient
    
    
    public virtual OperationsClient DeleteConnectClusterOperationsClient { get; }

The long-running operations client for `DeleteConnectCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ManagedKafkaConnect.ManagedKafkaConnectClient GrpcClient { get; }

The underlying gRPC ManagedKafkaConnect client

**Property Value**  
---  
**Type** | **Description**  
`[ManagedKafkaConnect](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnect)[ManagedKafkaConnectClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnect.ManagedKafkaConnectClient)` |   
  
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
  
### UpdateConnectClusterOperationsClient
    
    
    public virtual OperationsClient UpdateConnectClusterOperationsClient { get; }

The long-running operations client for `UpdateConnectCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static ManagedKafkaConnectClient Create()

Synchronously creates a [ManagedKafkaConnectClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ManagedKafkaConnectClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ManagedKafkaConnectClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient)` | The created [ManagedKafkaConnectClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ManagedKafkaConnectClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ManagedKafkaConnectClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ManagedKafkaConnectClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedKafkaConnectClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient)` | The task representing the created [ManagedKafkaConnectClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient).  
  
### CreateConnectCluster(LocationName, ConnectCluster, string, CallSettings)
    
    
    public virtual Operation<ConnectCluster, OperationMetadata> CreateConnectCluster(LocationName parent, ConnectCluster connectCluster, string connectClusterId, CallSettings callSettings = null)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent project/location in which to create the Kafka Connect cluster. Structured like `projects/{project}/locations/{location}/`.  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. Configuration of the Kafka Connect cluster to create. Its `name` field is ignored.  
`connectClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Connect cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ConnectCluster connectCluster = new ConnectCluster();
    string connectClusterId = "";
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = managedKafkaConnectClient.CreateConnectCluster(parent, connectCluster, connectClusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = managedKafkaConnectClient.PollOnceCreateConnectCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectCluster(CreateConnectClusterRequest, CallSettings)
    
    
    public virtual Operation<ConnectCluster, OperationMetadata> CreateConnectCluster(CreateConnectClusterRequest request, CallSettings callSettings = null)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    CreateConnectClusterRequest request = new CreateConnectClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ConnectClusterId = "",
        ConnectCluster = new ConnectCluster(),
        RequestId = "",
    };
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = managedKafkaConnectClient.CreateConnectCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = managedKafkaConnectClient.PollOnceCreateConnectCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectCluster(string, ConnectCluster, string, CallSettings)
    
    
    public virtual Operation<ConnectCluster, OperationMetadata> CreateConnectCluster(string parent, ConnectCluster connectCluster, string connectClusterId, CallSettings callSettings = null)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent project/location in which to create the Kafka Connect cluster. Structured like `projects/{project}/locations/{location}/`.  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. Configuration of the Kafka Connect cluster to create. Its `name` field is ignored.  
`connectClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Connect cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ConnectCluster connectCluster = new ConnectCluster();
    string connectClusterId = "";
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = managedKafkaConnectClient.CreateConnectCluster(parent, connectCluster, connectClusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = managedKafkaConnectClient.PollOnceCreateConnectCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectClusterAsync(LocationName, ConnectCluster, string, CallSettings)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> CreateConnectClusterAsync(LocationName parent, ConnectCluster connectCluster, string connectClusterId, CallSettings callSettings = null)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent project/location in which to create the Kafka Connect cluster. Structured like `projects/{project}/locations/{location}/`.  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. Configuration of the Kafka Connect cluster to create. Its `name` field is ignored.  
`connectClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Connect cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ConnectCluster connectCluster = new ConnectCluster();
    string connectClusterId = "";
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.CreateConnectClusterAsync(parent, connectCluster, connectClusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceCreateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectClusterAsync(LocationName, ConnectCluster, string, CancellationToken)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> CreateConnectClusterAsync(LocationName parent, ConnectCluster connectCluster, string connectClusterId, CancellationToken cancellationToken)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent project/location in which to create the Kafka Connect cluster. Structured like `projects/{project}/locations/{location}/`.  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. Configuration of the Kafka Connect cluster to create. Its `name` field is ignored.  
`connectClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Connect cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ConnectCluster connectCluster = new ConnectCluster();
    string connectClusterId = "";
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.CreateConnectClusterAsync(parent, connectCluster, connectClusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceCreateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectClusterAsync(CreateConnectClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> CreateConnectClusterAsync(CreateConnectClusterRequest request, CallSettings callSettings = null)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    CreateConnectClusterRequest request = new CreateConnectClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ConnectClusterId = "",
        ConnectCluster = new ConnectCluster(),
        RequestId = "",
    };
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.CreateConnectClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceCreateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectClusterAsync(CreateConnectClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> CreateConnectClusterAsync(CreateConnectClusterRequest request, CancellationToken cancellationToken)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    CreateConnectClusterRequest request = new CreateConnectClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ConnectClusterId = "",
        ConnectCluster = new ConnectCluster(),
        RequestId = "",
    };
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.CreateConnectClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceCreateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectClusterAsync(string, ConnectCluster, string, CallSettings)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> CreateConnectClusterAsync(string parent, ConnectCluster connectCluster, string connectClusterId, CallSettings callSettings = null)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent project/location in which to create the Kafka Connect cluster. Structured like `projects/{project}/locations/{location}/`.  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. Configuration of the Kafka Connect cluster to create. Its `name` field is ignored.  
`connectClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Connect cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ConnectCluster connectCluster = new ConnectCluster();
    string connectClusterId = "";
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.CreateConnectClusterAsync(parent, connectCluster, connectClusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceCreateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectClusterAsync(string, ConnectCluster, string, CancellationToken)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> CreateConnectClusterAsync(string parent, ConnectCluster connectCluster, string connectClusterId, CancellationToken cancellationToken)

Creates a new Kafka Connect cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent project/location in which to create the Kafka Connect cluster. Structured like `projects/{project}/locations/{location}/`.  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. Configuration of the Kafka Connect cluster to create. Its `name` field is ignored.  
`connectClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Connect cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ConnectCluster connectCluster = new ConnectCluster();
    string connectClusterId = "";
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.CreateConnectClusterAsync(parent, connectCluster, connectClusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceCreateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnector(ConnectClusterName, Connector, string, CallSettings)
    
    
    public virtual Connector CreateConnector(ConnectClusterName parent, Connector connector, string connectorId, CallSettings callSettings = null)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The parent Connect cluster in which to create the connector. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to create.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the connector, which will become the final component of the connector's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-connector-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectClusterName parent = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    Connector connector = new Connector();
    string connectorId = "";
    // Make the request
    Connector response = managedKafkaConnectClient.CreateConnector(parent, connector, connectorId);
    

### CreateConnector(CreateConnectorRequest, CallSettings)
    
    
    public virtual Connector CreateConnector(CreateConnectorRequest request, CallSettings callSettings = null)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    CreateConnectorRequest request = new CreateConnectorRequest
    {
        ParentAsConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
        ConnectorId = "",
        Connector = new Connector(),
    };
    // Make the request
    Connector response = managedKafkaConnectClient.CreateConnector(request);
    

### CreateConnector(string, Connector, string, CallSettings)
    
    
    public virtual Connector CreateConnector(string parent, Connector connector, string connectorId, CallSettings callSettings = null)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Connect cluster in which to create the connector. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to create.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the connector, which will become the final component of the connector's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-connector-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    Connector connector = new Connector();
    string connectorId = "";
    // Make the request
    Connector response = managedKafkaConnectClient.CreateConnector(parent, connector, connectorId);
    

### CreateConnectorAsync(ConnectClusterName, Connector, string, CallSettings)
    
    
    public virtual Task<Connector> CreateConnectorAsync(ConnectClusterName parent, Connector connector, string connectorId, CallSettings callSettings = null)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The parent Connect cluster in which to create the connector. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to create.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the connector, which will become the final component of the connector's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-connector-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectClusterName parent = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    Connector connector = new Connector();
    string connectorId = "";
    // Make the request
    Connector response = await managedKafkaConnectClient.CreateConnectorAsync(parent, connector, connectorId);
    

### CreateConnectorAsync(ConnectClusterName, Connector, string, CancellationToken)
    
    
    public virtual Task<Connector> CreateConnectorAsync(ConnectClusterName parent, Connector connector, string connectorId, CancellationToken cancellationToken)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The parent Connect cluster in which to create the connector. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to create.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the connector, which will become the final component of the connector's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-connector-id`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectClusterName parent = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    Connector connector = new Connector();
    string connectorId = "";
    // Make the request
    Connector response = await managedKafkaConnectClient.CreateConnectorAsync(parent, connector, connectorId);
    

### CreateConnectorAsync(CreateConnectorRequest, CallSettings)
    
    
    public virtual Task<Connector> CreateConnectorAsync(CreateConnectorRequest request, CallSettings callSettings = null)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    CreateConnectorRequest request = new CreateConnectorRequest
    {
        ParentAsConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
        ConnectorId = "",
        Connector = new Connector(),
    };
    // Make the request
    Connector response = await managedKafkaConnectClient.CreateConnectorAsync(request);
    

### CreateConnectorAsync(CreateConnectorRequest, CancellationToken)
    
    
    public virtual Task<Connector> CreateConnectorAsync(CreateConnectorRequest request, CancellationToken cancellationToken)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    CreateConnectorRequest request = new CreateConnectorRequest
    {
        ParentAsConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
        ConnectorId = "",
        Connector = new Connector(),
    };
    // Make the request
    Connector response = await managedKafkaConnectClient.CreateConnectorAsync(request);
    

### CreateConnectorAsync(string, Connector, string, CallSettings)
    
    
    public virtual Task<Connector> CreateConnectorAsync(string parent, Connector connector, string connectorId, CallSettings callSettings = null)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Connect cluster in which to create the connector. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to create.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the connector, which will become the final component of the connector's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-connector-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    Connector connector = new Connector();
    string connectorId = "";
    // Make the request
    Connector response = await managedKafkaConnectClient.CreateConnectorAsync(parent, connector, connectorId);
    

### CreateConnectorAsync(string, Connector, string, CancellationToken)
    
    
    public virtual Task<Connector> CreateConnectorAsync(string parent, Connector connector, string connectorId, CancellationToken cancellationToken)

Creates a new connector in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Connect cluster in which to create the connector. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to create.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the connector, which will become the final component of the connector's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-connector-id`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    Connector connector = new Connector();
    string connectorId = "";
    // Make the request
    Connector response = await managedKafkaConnectClient.CreateConnectorAsync(parent, connector, connectorId);
    

### DeleteConnectCluster(ConnectClusterName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteConnectCluster(ConnectClusterName name, CallSettings callSettings = null)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The name of the Kafka Connect cluster to delete. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectClusterName name = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = managedKafkaConnectClient.DeleteConnectCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = managedKafkaConnectClient.PollOnceDeleteConnectCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectCluster(DeleteConnectClusterRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteConnectCluster(DeleteConnectClusterRequest request, CallSettings callSettings = null)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    DeleteConnectClusterRequest request = new DeleteConnectClusterRequest
    {
        ConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = managedKafkaConnectClient.DeleteConnectCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = managedKafkaConnectClient.PollOnceDeleteConnectCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectCluster(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteConnectCluster(string name, CallSettings callSettings = null)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Kafka Connect cluster to delete. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = managedKafkaConnectClient.DeleteConnectCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = managedKafkaConnectClient.PollOnceDeleteConnectCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectClusterAsync(ConnectClusterName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectClusterAsync(ConnectClusterName name, CallSettings callSettings = null)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The name of the Kafka Connect cluster to delete. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectClusterName name = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaConnectClient.DeleteConnectClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceDeleteConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectClusterAsync(ConnectClusterName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectClusterAsync(ConnectClusterName name, CancellationToken cancellationToken)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The name of the Kafka Connect cluster to delete. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectClusterName name = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaConnectClient.DeleteConnectClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceDeleteConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectClusterAsync(DeleteConnectClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectClusterAsync(DeleteConnectClusterRequest request, CallSettings callSettings = null)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConnectClusterRequest request = new DeleteConnectClusterRequest
    {
        ConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaConnectClient.DeleteConnectClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceDeleteConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectClusterAsync(DeleteConnectClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectClusterAsync(DeleteConnectClusterRequest request, CancellationToken cancellationToken)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConnectClusterRequest request = new DeleteConnectClusterRequest
    {
        ConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaConnectClient.DeleteConnectClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceDeleteConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectClusterAsync(string name, CallSettings callSettings = null)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Kafka Connect cluster to delete. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaConnectClient.DeleteConnectClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceDeleteConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectClusterAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectClusterAsync(string name, CancellationToken cancellationToken)

Deletes a single Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Kafka Connect cluster to delete. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaConnectClient.DeleteConnectClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceDeleteConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnector(ConnectorName, CallSettings)
    
    
    public virtual void DeleteConnector(ConnectorName name, CallSettings callSettings = null)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to delete. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    managedKafkaConnectClient.DeleteConnector(name);
    

### DeleteConnector(DeleteConnectorRequest, CallSettings)
    
    
    public virtual void DeleteConnector(DeleteConnectorRequest request, CallSettings callSettings = null)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    DeleteConnectorRequest request = new DeleteConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    managedKafkaConnectClient.DeleteConnector(request);
    

### DeleteConnector(string, CallSettings)
    
    
    public virtual void DeleteConnector(string name, CallSettings callSettings = null)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to delete. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    managedKafkaConnectClient.DeleteConnector(name);
    

### DeleteConnectorAsync(ConnectorName, CallSettings)
    
    
    public virtual Task DeleteConnectorAsync(ConnectorName name, CallSettings callSettings = null)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to delete. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    await managedKafkaConnectClient.DeleteConnectorAsync(name);
    

### DeleteConnectorAsync(ConnectorName, CancellationToken)
    
    
    public virtual Task DeleteConnectorAsync(ConnectorName name, CancellationToken cancellationToken)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to delete. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    await managedKafkaConnectClient.DeleteConnectorAsync(name);
    

### DeleteConnectorAsync(DeleteConnectorRequest, CallSettings)
    
    
    public virtual Task DeleteConnectorAsync(DeleteConnectorRequest request, CallSettings callSettings = null)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConnectorRequest request = new DeleteConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    await managedKafkaConnectClient.DeleteConnectorAsync(request);
    

### DeleteConnectorAsync(DeleteConnectorRequest, CancellationToken)
    
    
    public virtual Task DeleteConnectorAsync(DeleteConnectorRequest request, CancellationToken cancellationToken)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConnectorRequest request = new DeleteConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    await managedKafkaConnectClient.DeleteConnectorAsync(request);
    

### DeleteConnectorAsync(string, CallSettings)
    
    
    public virtual Task DeleteConnectorAsync(string name, CallSettings callSettings = null)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to delete. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    await managedKafkaConnectClient.DeleteConnectorAsync(name);
    

### DeleteConnectorAsync(string, CancellationToken)
    
    
    public virtual Task DeleteConnectorAsync(string name, CancellationToken cancellationToken)

Deletes a connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to delete. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    await managedKafkaConnectClient.DeleteConnectorAsync(name);
    

### GetConnectCluster(ConnectClusterName, CallSettings)
    
    
    public virtual ConnectCluster GetConnectCluster(ConnectClusterName name, CallSettings callSettings = null)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The name of the Kafka Connect cluster whose configuration to return. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectClusterName name = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    // Make the request
    ConnectCluster response = managedKafkaConnectClient.GetConnectCluster(name);
    

### GetConnectCluster(GetConnectClusterRequest, CallSettings)
    
    
    public virtual ConnectCluster GetConnectCluster(GetConnectClusterRequest request, CallSettings callSettings = null)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    GetConnectClusterRequest request = new GetConnectClusterRequest
    {
        ConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
    };
    // Make the request
    ConnectCluster response = managedKafkaConnectClient.GetConnectCluster(request);
    

### GetConnectCluster(string, CallSettings)
    
    
    public virtual ConnectCluster GetConnectCluster(string name, CallSettings callSettings = null)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Kafka Connect cluster whose configuration to return. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    // Make the request
    ConnectCluster response = managedKafkaConnectClient.GetConnectCluster(name);
    

### GetConnectClusterAsync(ConnectClusterName, CallSettings)
    
    
    public virtual Task<ConnectCluster> GetConnectClusterAsync(ConnectClusterName name, CallSettings callSettings = null)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The name of the Kafka Connect cluster whose configuration to return. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectClusterName name = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    // Make the request
    ConnectCluster response = await managedKafkaConnectClient.GetConnectClusterAsync(name);
    

### GetConnectClusterAsync(ConnectClusterName, CancellationToken)
    
    
    public virtual Task<ConnectCluster> GetConnectClusterAsync(ConnectClusterName name, CancellationToken cancellationToken)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The name of the Kafka Connect cluster whose configuration to return. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectClusterName name = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    // Make the request
    ConnectCluster response = await managedKafkaConnectClient.GetConnectClusterAsync(name);
    

### GetConnectClusterAsync(GetConnectClusterRequest, CallSettings)
    
    
    public virtual Task<ConnectCluster> GetConnectClusterAsync(GetConnectClusterRequest request, CallSettings callSettings = null)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    GetConnectClusterRequest request = new GetConnectClusterRequest
    {
        ConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
    };
    // Make the request
    ConnectCluster response = await managedKafkaConnectClient.GetConnectClusterAsync(request);
    

### GetConnectClusterAsync(GetConnectClusterRequest, CancellationToken)
    
    
    public virtual Task<ConnectCluster> GetConnectClusterAsync(GetConnectClusterRequest request, CancellationToken cancellationToken)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    GetConnectClusterRequest request = new GetConnectClusterRequest
    {
        ConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
    };
    // Make the request
    ConnectCluster response = await managedKafkaConnectClient.GetConnectClusterAsync(request);
    

### GetConnectClusterAsync(string, CallSettings)
    
    
    public virtual Task<ConnectCluster> GetConnectClusterAsync(string name, CallSettings callSettings = null)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Kafka Connect cluster whose configuration to return. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    // Make the request
    ConnectCluster response = await managedKafkaConnectClient.GetConnectClusterAsync(name);
    

### GetConnectClusterAsync(string, CancellationToken)
    
    
    public virtual Task<ConnectCluster> GetConnectClusterAsync(string name, CancellationToken cancellationToken)

Returns the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Kafka Connect cluster whose configuration to return. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    // Make the request
    ConnectCluster response = await managedKafkaConnectClient.GetConnectClusterAsync(name);
    

### GetConnector(ConnectorName, CallSettings)
    
    
    public virtual Connector GetConnector(ConnectorName name, CallSettings callSettings = null)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector whose configuration to return. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    Connector response = managedKafkaConnectClient.GetConnector(name);
    

### GetConnector(GetConnectorRequest, CallSettings)
    
    
    public virtual Connector GetConnector(GetConnectorRequest request, CallSettings callSettings = null)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    GetConnectorRequest request = new GetConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    Connector response = managedKafkaConnectClient.GetConnector(request);
    

### GetConnector(string, CallSettings)
    
    
    public virtual Connector GetConnector(string name, CallSettings callSettings = null)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector whose configuration to return. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    Connector response = managedKafkaConnectClient.GetConnector(name);
    

### GetConnectorAsync(ConnectorName, CallSettings)
    
    
    public virtual Task<Connector> GetConnectorAsync(ConnectorName name, CallSettings callSettings = null)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector whose configuration to return. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    Connector response = await managedKafkaConnectClient.GetConnectorAsync(name);
    

### GetConnectorAsync(ConnectorName, CancellationToken)
    
    
    public virtual Task<Connector> GetConnectorAsync(ConnectorName name, CancellationToken cancellationToken)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector whose configuration to return. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    Connector response = await managedKafkaConnectClient.GetConnectorAsync(name);
    

### GetConnectorAsync(GetConnectorRequest, CallSettings)
    
    
    public virtual Task<Connector> GetConnectorAsync(GetConnectorRequest request, CallSettings callSettings = null)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    GetConnectorRequest request = new GetConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    Connector response = await managedKafkaConnectClient.GetConnectorAsync(request);
    

### GetConnectorAsync(GetConnectorRequest, CancellationToken)
    
    
    public virtual Task<Connector> GetConnectorAsync(GetConnectorRequest request, CancellationToken cancellationToken)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    GetConnectorRequest request = new GetConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    Connector response = await managedKafkaConnectClient.GetConnectorAsync(request);
    

### GetConnectorAsync(string, CallSettings)
    
    
    public virtual Task<Connector> GetConnectorAsync(string name, CallSettings callSettings = null)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector whose configuration to return. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    Connector response = await managedKafkaConnectClient.GetConnectorAsync(name);
    

### GetConnectorAsync(string, CancellationToken)
    
    
    public virtual Task<Connector> GetConnectorAsync(string name, CancellationToken cancellationToken)

Returns the properties of a single connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector whose configuration to return. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    Connector response = await managedKafkaConnectClient.GetConnectorAsync(name);
    

### ListConnectClusters(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectClustersResponse, ConnectCluster> ListConnectClusters(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Kafka Connect clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent project/location whose Connect clusters are to be listed. Structured like `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersResponse)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A pageable sequence of [ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListConnectClustersResponse, ConnectCluster> response = managedKafkaConnectClient.ListConnectClusters(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConnectCluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectCluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectCluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectCluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectClusters(ListConnectClustersRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectClustersResponse, ConnectCluster> ListConnectClusters(ListConnectClustersRequest request, CallSettings callSettings = null)

Lists the Kafka Connect clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersResponse)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A pageable sequence of [ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ListConnectClustersRequest request = new ListConnectClustersRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListConnectClustersResponse, ConnectCluster> response = managedKafkaConnectClient.ListConnectClusters(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConnectCluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectCluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectCluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectCluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectClusters(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectClustersResponse, ConnectCluster> ListConnectClusters(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Kafka Connect clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent project/location whose Connect clusters are to be listed. Structured like `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersResponse)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A pageable sequence of [ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListConnectClustersResponse, ConnectCluster> response = managedKafkaConnectClient.ListConnectClusters(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConnectCluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectCluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectCluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectCluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectClustersAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectClustersResponse, ConnectCluster> ListConnectClustersAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Kafka Connect clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent project/location whose Connect clusters are to be listed. Structured like `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersResponse)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A pageable asynchronous sequence of [ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListConnectClustersResponse, ConnectCluster> response = managedKafkaConnectClient.ListConnectClustersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConnectCluster item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectClustersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectCluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectCluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectCluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectClustersAsync(ListConnectClustersRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectClustersResponse, ConnectCluster> ListConnectClustersAsync(ListConnectClustersRequest request, CallSettings callSettings = null)

Lists the Kafka Connect clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersResponse)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A pageable asynchronous sequence of [ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ListConnectClustersRequest request = new ListConnectClustersRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListConnectClustersResponse, ConnectCluster> response = managedKafkaConnectClient.ListConnectClustersAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConnectCluster item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectClustersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectCluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectCluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectCluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectClustersAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectClustersResponse, ConnectCluster> ListConnectClustersAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the Kafka Connect clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent project/location whose Connect clusters are to be listed. Structured like `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectClustersResponse)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)` | A pageable asynchronous sequence of [ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListConnectClustersResponse, ConnectCluster> response = managedKafkaConnectClient.ListConnectClustersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConnectCluster item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectClustersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectCluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectCluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectCluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectors(ConnectClusterName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectorsResponse, Connector> ListConnectors(ConnectClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the connectors in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The parent Connect cluster whose connectors are to be listed. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsResponse)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A pageable sequence of [Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectClusterName parent = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    // Make the request
    PagedEnumerable<ListConnectorsResponse, Connector> response = managedKafkaConnectClient.ListConnectors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Connector item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connector item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connector> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connector item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectors(ListConnectorsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectorsResponse, Connector> ListConnectors(ListConnectorsRequest request, CallSettings callSettings = null)

Lists the connectors in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsResponse)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A pageable sequence of [Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ListConnectorsRequest request = new ListConnectorsRequest
    {
        ParentAsConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
    };
    // Make the request
    PagedEnumerable<ListConnectorsResponse, Connector> response = managedKafkaConnectClient.ListConnectors(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Connector item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connector item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connector> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connector item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectors(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectorsResponse, Connector> ListConnectors(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the connectors in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Connect cluster whose connectors are to be listed. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsResponse)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A pageable sequence of [Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    // Make the request
    PagedEnumerable<ListConnectorsResponse, Connector> response = managedKafkaConnectClient.ListConnectors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Connector item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connector item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connector> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connector item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectorsAsync(ConnectClusterName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectorsResponse, Connector> ListConnectorsAsync(ConnectClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the connectors in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)`  
Required. The parent Connect cluster whose connectors are to be listed. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsResponse)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A pageable asynchronous sequence of [Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectClusterName parent = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]");
    // Make the request
    PagedAsyncEnumerable<ListConnectorsResponse, Connector> response = managedKafkaConnectClient.ListConnectorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Connector item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectorsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connector item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connector> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connector item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectorsAsync(ListConnectorsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectorsResponse, Connector> ListConnectorsAsync(ListConnectorsRequest request, CallSettings callSettings = null)

Lists the connectors in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsResponse)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A pageable asynchronous sequence of [Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ListConnectorsRequest request = new ListConnectorsRequest
    {
        ParentAsConnectClusterName = ConnectClusterName.FromProjectLocationConnectCluster("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListConnectorsResponse, Connector> response = managedKafkaConnectClient.ListConnectorsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Connector item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectorsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connector item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connector> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connector item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectorsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectorsResponse, Connector> ListConnectorsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the connectors in a given Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Connect cluster whose connectors are to be listed. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConnectorsResponse)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A pageable asynchronous sequence of [Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]";
    // Make the request
    PagedAsyncEnumerable<ListConnectorsResponse, Connector> response = managedKafkaConnectClient.ListConnectorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Connector item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectorsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connector item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connector> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connector item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PauseConnector(ConnectorName, CallSettings)
    
    
    public virtual PauseConnectorResponse PauseConnector(ConnectorName name, CallSettings callSettings = null)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    PauseConnectorResponse response = managedKafkaConnectClient.PauseConnector(name);
    

### PauseConnector(PauseConnectorRequest, CallSettings)
    
    
    public virtual PauseConnectorResponse PauseConnector(PauseConnectorRequest request, CallSettings callSettings = null)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    PauseConnectorRequest request = new PauseConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    PauseConnectorResponse response = managedKafkaConnectClient.PauseConnector(request);
    

### PauseConnector(string, CallSettings)
    
    
    public virtual PauseConnectorResponse PauseConnector(string name, CallSettings callSettings = null)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    PauseConnectorResponse response = managedKafkaConnectClient.PauseConnector(name);
    

### PauseConnectorAsync(ConnectorName, CallSettings)
    
    
    public virtual Task<PauseConnectorResponse> PauseConnectorAsync(ConnectorName name, CallSettings callSettings = null)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    PauseConnectorResponse response = await managedKafkaConnectClient.PauseConnectorAsync(name);
    

### PauseConnectorAsync(ConnectorName, CancellationToken)
    
    
    public virtual Task<PauseConnectorResponse> PauseConnectorAsync(ConnectorName name, CancellationToken cancellationToken)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    PauseConnectorResponse response = await managedKafkaConnectClient.PauseConnectorAsync(name);
    

### PauseConnectorAsync(PauseConnectorRequest, CallSettings)
    
    
    public virtual Task<PauseConnectorResponse> PauseConnectorAsync(PauseConnectorRequest request, CallSettings callSettings = null)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    PauseConnectorRequest request = new PauseConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    PauseConnectorResponse response = await managedKafkaConnectClient.PauseConnectorAsync(request);
    

### PauseConnectorAsync(PauseConnectorRequest, CancellationToken)
    
    
    public virtual Task<PauseConnectorResponse> PauseConnectorAsync(PauseConnectorRequest request, CancellationToken cancellationToken)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    PauseConnectorRequest request = new PauseConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    PauseConnectorResponse response = await managedKafkaConnectClient.PauseConnectorAsync(request);
    

### PauseConnectorAsync(string, CallSettings)
    
    
    public virtual Task<PauseConnectorResponse> PauseConnectorAsync(string name, CallSettings callSettings = null)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    PauseConnectorResponse response = await managedKafkaConnectClient.PauseConnectorAsync(name);
    

### PauseConnectorAsync(string, CancellationToken)
    
    
    public virtual Task<PauseConnectorResponse> PauseConnectorAsync(string name, CancellationToken cancellationToken)

Pauses the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PauseConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.PauseConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    PauseConnectorResponse response = await managedKafkaConnectClient.PauseConnectorAsync(name);
    

### PollOnceCreateConnectCluster(string, CallSettings)
    
    
    public virtual Operation<ConnectCluster, OperationMetadata> PollOnceCreateConnectCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateConnectCluster` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateConnectClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> PollOnceCreateConnectClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateConnectCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteConnectCluster(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteConnectCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteConnectCluster` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteConnectClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteConnectClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteConnectCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateConnectCluster(string, CallSettings)
    
    
    public virtual Operation<ConnectCluster, OperationMetadata> PollOnceUpdateConnectCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateConnectCluster` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateConnectClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> PollOnceUpdateConnectClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateConnectCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### RestartConnector(ConnectorName, CallSettings)
    
    
    public virtual RestartConnectorResponse RestartConnector(ConnectorName name, CallSettings callSettings = null)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to restart. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    RestartConnectorResponse response = managedKafkaConnectClient.RestartConnector(name);
    

### RestartConnector(RestartConnectorRequest, CallSettings)
    
    
    public virtual RestartConnectorResponse RestartConnector(RestartConnectorRequest request, CallSettings callSettings = null)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    RestartConnectorRequest request = new RestartConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    RestartConnectorResponse response = managedKafkaConnectClient.RestartConnector(request);
    

### RestartConnector(string, CallSettings)
    
    
    public virtual RestartConnectorResponse RestartConnector(string name, CallSettings callSettings = null)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to restart. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    RestartConnectorResponse response = managedKafkaConnectClient.RestartConnector(name);
    

### RestartConnectorAsync(ConnectorName, CallSettings)
    
    
    public virtual Task<RestartConnectorResponse> RestartConnectorAsync(ConnectorName name, CallSettings callSettings = null)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to restart. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    RestartConnectorResponse response = await managedKafkaConnectClient.RestartConnectorAsync(name);
    

### RestartConnectorAsync(ConnectorName, CancellationToken)
    
    
    public virtual Task<RestartConnectorResponse> RestartConnectorAsync(ConnectorName name, CancellationToken cancellationToken)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to restart. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    RestartConnectorResponse response = await managedKafkaConnectClient.RestartConnectorAsync(name);
    

### RestartConnectorAsync(RestartConnectorRequest, CallSettings)
    
    
    public virtual Task<RestartConnectorResponse> RestartConnectorAsync(RestartConnectorRequest request, CallSettings callSettings = null)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    RestartConnectorRequest request = new RestartConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    RestartConnectorResponse response = await managedKafkaConnectClient.RestartConnectorAsync(request);
    

### RestartConnectorAsync(RestartConnectorRequest, CancellationToken)
    
    
    public virtual Task<RestartConnectorResponse> RestartConnectorAsync(RestartConnectorRequest request, CancellationToken cancellationToken)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    RestartConnectorRequest request = new RestartConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    RestartConnectorResponse response = await managedKafkaConnectClient.RestartConnectorAsync(request);
    

### RestartConnectorAsync(string, CallSettings)
    
    
    public virtual Task<RestartConnectorResponse> RestartConnectorAsync(string name, CallSettings callSettings = null)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to restart. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    RestartConnectorResponse response = await managedKafkaConnectClient.RestartConnectorAsync(name);
    

### RestartConnectorAsync(string, CancellationToken)
    
    
    public virtual Task<RestartConnectorResponse> RestartConnectorAsync(string name, CancellationToken cancellationToken)

Restarts the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to restart. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RestartConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RestartConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    RestartConnectorResponse response = await managedKafkaConnectClient.RestartConnectorAsync(name);
    

### ResumeConnector(ConnectorName, CallSettings)
    
    
    public virtual ResumeConnectorResponse ResumeConnector(ConnectorName name, CallSettings callSettings = null)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    ResumeConnectorResponse response = managedKafkaConnectClient.ResumeConnector(name);
    

### ResumeConnector(ResumeConnectorRequest, CallSettings)
    
    
    public virtual ResumeConnectorResponse ResumeConnector(ResumeConnectorRequest request, CallSettings callSettings = null)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ResumeConnectorRequest request = new ResumeConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    ResumeConnectorResponse response = managedKafkaConnectClient.ResumeConnector(request);
    

### ResumeConnector(string, CallSettings)
    
    
    public virtual ResumeConnectorResponse ResumeConnector(string name, CallSettings callSettings = null)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    ResumeConnectorResponse response = managedKafkaConnectClient.ResumeConnector(name);
    

### ResumeConnectorAsync(ConnectorName, CallSettings)
    
    
    public virtual Task<ResumeConnectorResponse> ResumeConnectorAsync(ConnectorName name, CallSettings callSettings = null)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    ResumeConnectorResponse response = await managedKafkaConnectClient.ResumeConnectorAsync(name);
    

### ResumeConnectorAsync(ConnectorName, CancellationToken)
    
    
    public virtual Task<ResumeConnectorResponse> ResumeConnectorAsync(ConnectorName name, CancellationToken cancellationToken)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    ResumeConnectorResponse response = await managedKafkaConnectClient.ResumeConnectorAsync(name);
    

### ResumeConnectorAsync(ResumeConnectorRequest, CallSettings)
    
    
    public virtual Task<ResumeConnectorResponse> ResumeConnectorAsync(ResumeConnectorRequest request, CallSettings callSettings = null)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ResumeConnectorRequest request = new ResumeConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    ResumeConnectorResponse response = await managedKafkaConnectClient.ResumeConnectorAsync(request);
    

### ResumeConnectorAsync(ResumeConnectorRequest, CancellationToken)
    
    
    public virtual Task<ResumeConnectorResponse> ResumeConnectorAsync(ResumeConnectorRequest request, CancellationToken cancellationToken)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ResumeConnectorRequest request = new ResumeConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    ResumeConnectorResponse response = await managedKafkaConnectClient.ResumeConnectorAsync(request);
    

### ResumeConnectorAsync(string, CallSettings)
    
    
    public virtual Task<ResumeConnectorResponse> ResumeConnectorAsync(string name, CallSettings callSettings = null)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    ResumeConnectorResponse response = await managedKafkaConnectClient.ResumeConnectorAsync(name);
    

### ResumeConnectorAsync(string, CancellationToken)
    
    
    public virtual Task<ResumeConnectorResponse> ResumeConnectorAsync(string name, CancellationToken cancellationToken)

Resumes the connector and its tasks.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to pause. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResumeConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ResumeConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    ResumeConnectorResponse response = await managedKafkaConnectClient.ResumeConnectorAsync(name);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient#Google_Cloud_ManagedKafka_V1_ManagedKafkaConnectClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient#Google_Cloud_ManagedKafka_V1_ManagedKafkaConnectClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient#Google_Cloud_ManagedKafka_V1_ManagedKafkaConnectClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaConnectClient#Google_Cloud_ManagedKafka_V1_ManagedKafkaConnectClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### StopConnector(ConnectorName, CallSettings)
    
    
    public virtual StopConnectorResponse StopConnector(ConnectorName name, CallSettings callSettings = null)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to stop. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    StopConnectorResponse response = managedKafkaConnectClient.StopConnector(name);
    

### StopConnector(StopConnectorRequest, CallSettings)
    
    
    public virtual StopConnectorResponse StopConnector(StopConnectorRequest request, CallSettings callSettings = null)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    StopConnectorRequest request = new StopConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    StopConnectorResponse response = managedKafkaConnectClient.StopConnector(request);
    

### StopConnector(string, CallSettings)
    
    
    public virtual StopConnectorResponse StopConnector(string name, CallSettings callSettings = null)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to stop. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    StopConnectorResponse response = managedKafkaConnectClient.StopConnector(name);
    

### StopConnectorAsync(ConnectorName, CallSettings)
    
    
    public virtual Task<StopConnectorResponse> StopConnectorAsync(ConnectorName name, CallSettings callSettings = null)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to stop. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    StopConnectorResponse response = await managedKafkaConnectClient.StopConnectorAsync(name);
    

### StopConnectorAsync(ConnectorName, CancellationToken)
    
    
    public virtual Task<StopConnectorResponse> StopConnectorAsync(ConnectorName name, CancellationToken cancellationToken)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)`  
Required. The name of the connector to stop. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectorName name = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]");
    // Make the request
    StopConnectorResponse response = await managedKafkaConnectClient.StopConnectorAsync(name);
    

### StopConnectorAsync(StopConnectorRequest, CallSettings)
    
    
    public virtual Task<StopConnectorResponse> StopConnectorAsync(StopConnectorRequest request, CallSettings callSettings = null)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    StopConnectorRequest request = new StopConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    StopConnectorResponse response = await managedKafkaConnectClient.StopConnectorAsync(request);
    

### StopConnectorAsync(StopConnectorRequest, CancellationToken)
    
    
    public virtual Task<StopConnectorResponse> StopConnectorAsync(StopConnectorRequest request, CancellationToken cancellationToken)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    StopConnectorRequest request = new StopConnectorRequest
    {
        ConnectorName = ConnectorName.FromProjectLocationConnectClusterConnector("[PROJECT]", "[LOCATION]", "[CONNECT_CLUSTER]", "[CONNECTOR]"),
    };
    // Make the request
    StopConnectorResponse response = await managedKafkaConnectClient.StopConnectorAsync(request);
    

### StopConnectorAsync(string, CallSettings)
    
    
    public virtual Task<StopConnectorResponse> StopConnectorAsync(string name, CallSettings callSettings = null)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to stop. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    StopConnectorResponse response = await managedKafkaConnectClient.StopConnectorAsync(name);
    

### StopConnectorAsync(string, CancellationToken)
    
    
    public virtual Task<StopConnectorResponse> StopConnectorAsync(string name, CancellationToken cancellationToken)

Stops the connector.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connector to stop. Structured like: projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopConnectorResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.StopConnectorResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectClusters/[CONNECT_CLUSTER]/connectors/[CONNECTOR]";
    // Make the request
    StopConnectorResponse response = await managedKafkaConnectClient.StopConnectorAsync(name);
    

### UpdateConnectCluster(ConnectCluster, FieldMask, CallSettings)
    
    
    public virtual Operation<ConnectCluster, OperationMetadata> UpdateConnectCluster(ConnectCluster connectCluster, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. The Kafka Connect cluster to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    ConnectCluster connectCluster = new ConnectCluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = managedKafkaConnectClient.UpdateConnectCluster(connectCluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = managedKafkaConnectClient.PollOnceUpdateConnectCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectCluster(UpdateConnectClusterRequest, CallSettings)
    
    
    public virtual Operation<ConnectCluster, OperationMetadata> UpdateConnectCluster(UpdateConnectClusterRequest request, CallSettings callSettings = null)

Updates the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    UpdateConnectClusterRequest request = new UpdateConnectClusterRequest
    {
        UpdateMask = new FieldMask(),
        ConnectCluster = new ConnectCluster(),
        RequestId = "",
    };
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = managedKafkaConnectClient.UpdateConnectCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = managedKafkaConnectClient.PollOnceUpdateConnectCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectClusterAsync(ConnectCluster, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> UpdateConnectClusterAsync(ConnectCluster connectCluster, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. The Kafka Connect cluster to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectCluster connectCluster = new ConnectCluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.UpdateConnectClusterAsync(connectCluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceUpdateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectClusterAsync(ConnectCluster, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> UpdateConnectClusterAsync(ConnectCluster connectCluster, FieldMask updateMask, CancellationToken cancellationToken)

Updates the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`connectCluster` | `[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)`  
Required. The Kafka Connect cluster to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    ConnectCluster connectCluster = new ConnectCluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.UpdateConnectClusterAsync(connectCluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceUpdateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectClusterAsync(UpdateConnectClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> UpdateConnectClusterAsync(UpdateConnectClusterRequest request, CallSettings callSettings = null)

Updates the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    UpdateConnectClusterRequest request = new UpdateConnectClusterRequest
    {
        UpdateMask = new FieldMask(),
        ConnectCluster = new ConnectCluster(),
        RequestId = "",
    };
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.UpdateConnectClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceUpdateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectClusterAsync(UpdateConnectClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<ConnectCluster, OperationMetadata>> UpdateConnectClusterAsync(UpdateConnectClusterRequest request, CancellationToken cancellationToken)

Updates the properties of a single Kafka Connect cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConnectClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectCluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    UpdateConnectClusterRequest request = new UpdateConnectClusterRequest
    {
        UpdateMask = new FieldMask(),
        ConnectCluster = new ConnectCluster(),
        RequestId = "",
    };
    // Make the request
    Operation<ConnectCluster, OperationMetadata> response = await managedKafkaConnectClient.UpdateConnectClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectCluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectCluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectCluster, OperationMetadata> retrievedResponse = await managedKafkaConnectClient.PollOnceUpdateConnectClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectCluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnector(Connector, FieldMask, CallSettings)
    
    
    public virtual Connector UpdateConnector(Connector connector, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a connector.

**Parameters**  
---  
**Name** | **Description**  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    Connector connector = new Connector();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Connector response = managedKafkaConnectClient.UpdateConnector(connector, updateMask);
    

### UpdateConnector(UpdateConnectorRequest, CallSettings)
    
    
    public virtual Connector UpdateConnector(UpdateConnectorRequest request, CallSettings callSettings = null)

Updates the properties of a connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = ManagedKafkaConnectClient.Create();
    // Initialize request argument(s)
    UpdateConnectorRequest request = new UpdateConnectorRequest
    {
        UpdateMask = new FieldMask(),
        Connector = new Connector(),
    };
    // Make the request
    Connector response = managedKafkaConnectClient.UpdateConnector(request);
    

### UpdateConnectorAsync(Connector, FieldMask, CallSettings)
    
    
    public virtual Task<Connector> UpdateConnectorAsync(Connector connector, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a connector.

**Parameters**  
---  
**Name** | **Description**  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    Connector connector = new Connector();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Connector response = await managedKafkaConnectClient.UpdateConnectorAsync(connector, updateMask);
    

### UpdateConnectorAsync(Connector, FieldMask, CancellationToken)
    
    
    public virtual Task<Connector> UpdateConnectorAsync(Connector connector, FieldMask updateMask, CancellationToken cancellationToken)

Updates the properties of a connector.

**Parameters**  
---  
**Name** | **Description**  
`connector` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
Required. The connector to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    Connector connector = new Connector();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Connector response = await managedKafkaConnectClient.UpdateConnectorAsync(connector, updateMask);
    

### UpdateConnectorAsync(UpdateConnectorRequest, CallSettings)
    
    
    public virtual Task<Connector> UpdateConnectorAsync(UpdateConnectorRequest request, CallSettings callSettings = null)

Updates the properties of a connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    UpdateConnectorRequest request = new UpdateConnectorRequest
    {
        UpdateMask = new FieldMask(),
        Connector = new Connector(),
    };
    // Make the request
    Connector response = await managedKafkaConnectClient.UpdateConnectorAsync(request);
    

### UpdateConnectorAsync(UpdateConnectorRequest, CancellationToken)
    
    
    public virtual Task<Connector> UpdateConnectorAsync(UpdateConnectorRequest request, CancellationToken cancellationToken)

Updates the properties of a connector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConnectorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaConnectClient managedKafkaConnectClient = await ManagedKafkaConnectClient.CreateAsync();
    // Initialize request argument(s)
    UpdateConnectorRequest request = new UpdateConnectorRequest
    {
        UpdateMask = new FieldMask(),
        Connector = new Connector(),
    };
    // Make the request
    Connector response = await managedKafkaConnectClient.UpdateConnectorAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
