---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient
title: DataStream v1 API - Class DatastreamClient (2.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:25.393008+00:00
---

# DataStream v1 API - Class DatastreamClient (2.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1 API - Class DatastreamClient (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.12.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.11.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.10.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.9.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.8.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.7.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.6.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.5.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.4.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.3.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.2.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.1.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.0.0/Google.Cloud.Datastream.V1.DatastreamClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/1.0.0/Google.Cloud.Datastream.V1.DatastreamClient)


    
    
    public abstract class DatastreamClient

Reference documentation and code samples for the DataStream v1 API class DatastreamClient.

Datastream client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DatastreamClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DatastreamClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClientImpl)

## Namespace

[Google.Cloud.Datastream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1)

## Assembly

Google.Cloud.Datastream.V1.dll

## Remarks

Datastream service

## Properties 

### CreateConnectionProfileOperationsClient
    
    
    public virtual OperationsClient CreateConnectionProfileOperationsClient { get; }

The long-running operations client for `CreateConnectionProfile`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreatePrivateConnectionOperationsClient
    
    
    public virtual OperationsClient CreatePrivateConnectionOperationsClient { get; }

The long-running operations client for `CreatePrivateConnection`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateRouteOperationsClient
    
    
    public virtual OperationsClient CreateRouteOperationsClient { get; }

The long-running operations client for `CreateRoute`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateStreamOperationsClient
    
    
    public virtual OperationsClient CreateStreamOperationsClient { get; }

The long-running operations client for `CreateStream`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Datastream service, which is a host of "datastream.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Datastream scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Datastream scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteConnectionProfileOperationsClient
    
    
    public virtual OperationsClient DeleteConnectionProfileOperationsClient { get; }

The long-running operations client for `DeleteConnectionProfile`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeletePrivateConnectionOperationsClient
    
    
    public virtual OperationsClient DeletePrivateConnectionOperationsClient { get; }

The long-running operations client for `DeletePrivateConnection`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteRouteOperationsClient
    
    
    public virtual OperationsClient DeleteRouteOperationsClient { get; }

The long-running operations client for `DeleteRoute`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteStreamOperationsClient
    
    
    public virtual OperationsClient DeleteStreamOperationsClient { get; }

The long-running operations client for `DeleteStream`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual Datastream.DatastreamClient GrpcClient { get; }

The underlying gRPC Datastream client

**Property Value**  
---  
**Type** | **Description**  
`[Datastream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream)[DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamClient)` |   
  
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
  
### RunStreamOperationsClient
    
    
    public virtual OperationsClient RunStreamOperationsClient { get; }

The long-running operations client for `RunStream`.

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
  
### UpdateConnectionProfileOperationsClient
    
    
    public virtual OperationsClient UpdateConnectionProfileOperationsClient { get; }

The long-running operations client for `UpdateConnectionProfile`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateStreamOperationsClient
    
    
    public virtual OperationsClient UpdateStreamOperationsClient { get; }

The long-running operations client for `UpdateStream`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static DatastreamClient Create()

Synchronously creates a [DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DatastreamClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient)` | The created [DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DatastreamClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DatastreamClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient)` | The task representing the created [DatastreamClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient).  
  
### CreateConnectionProfile(LocationName, ConnectionProfile, string, CallSettings)
    
    
    public virtual Operation<ConnectionProfile, OperationMetadata> CreateConnectionProfile(LocationName parent, ConnectionProfile connectionProfile, string connectionProfileId, CallSettings callSettings = null)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of ConnectionProfiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile resource to create.  
`connectionProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The connection profile identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ConnectionProfile connectionProfile = new ConnectionProfile();
    string connectionProfileId = "";
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = datastreamClient.CreateConnectionProfile(parent, connectionProfile, connectionProfileId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateConnectionProfile(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectionProfile(CreateConnectionProfileRequest, CallSettings)
    
    
    public virtual Operation<ConnectionProfile, OperationMetadata> CreateConnectionProfile(CreateConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    CreateConnectionProfileRequest request = new CreateConnectionProfileRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ConnectionProfileId = "",
        ConnectionProfile = new ConnectionProfile(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = datastreamClient.CreateConnectionProfile(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateConnectionProfile(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectionProfile(string, ConnectionProfile, string, CallSettings)
    
    
    public virtual Operation<ConnectionProfile, OperationMetadata> CreateConnectionProfile(string parent, ConnectionProfile connectionProfile, string connectionProfileId, CallSettings callSettings = null)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of ConnectionProfiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile resource to create.  
`connectionProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The connection profile identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ConnectionProfile connectionProfile = new ConnectionProfile();
    string connectionProfileId = "";
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = datastreamClient.CreateConnectionProfile(parent, connectionProfile, connectionProfileId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateConnectionProfile(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectionProfileAsync(LocationName, ConnectionProfile, string, CallSettings)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> CreateConnectionProfileAsync(LocationName parent, ConnectionProfile connectionProfile, string connectionProfileId, CallSettings callSettings = null)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of ConnectionProfiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile resource to create.  
`connectionProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The connection profile identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ConnectionProfile connectionProfile = new ConnectionProfile();
    string connectionProfileId = "";
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.CreateConnectionProfileAsync(parent, connectionProfile, connectionProfileId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectionProfileAsync(LocationName, ConnectionProfile, string, CancellationToken)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> CreateConnectionProfileAsync(LocationName parent, ConnectionProfile connectionProfile, string connectionProfileId, CancellationToken cancellationToken)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of ConnectionProfiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile resource to create.  
`connectionProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The connection profile identifier.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ConnectionProfile connectionProfile = new ConnectionProfile();
    string connectionProfileId = "";
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.CreateConnectionProfileAsync(parent, connectionProfile, connectionProfileId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectionProfileAsync(CreateConnectionProfileRequest, CallSettings)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> CreateConnectionProfileAsync(CreateConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    CreateConnectionProfileRequest request = new CreateConnectionProfileRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ConnectionProfileId = "",
        ConnectionProfile = new ConnectionProfile(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.CreateConnectionProfileAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectionProfileAsync(CreateConnectionProfileRequest, CancellationToken)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> CreateConnectionProfileAsync(CreateConnectionProfileRequest request, CancellationToken cancellationToken)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    CreateConnectionProfileRequest request = new CreateConnectionProfileRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ConnectionProfileId = "",
        ConnectionProfile = new ConnectionProfile(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.CreateConnectionProfileAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectionProfileAsync(string, ConnectionProfile, string, CallSettings)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> CreateConnectionProfileAsync(string parent, ConnectionProfile connectionProfile, string connectionProfileId, CallSettings callSettings = null)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of ConnectionProfiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile resource to create.  
`connectionProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The connection profile identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ConnectionProfile connectionProfile = new ConnectionProfile();
    string connectionProfileId = "";
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.CreateConnectionProfileAsync(parent, connectionProfile, connectionProfileId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreateConnectionProfileAsync(string, ConnectionProfile, string, CancellationToken)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> CreateConnectionProfileAsync(string parent, ConnectionProfile connectionProfile, string connectionProfileId, CancellationToken cancellationToken)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of ConnectionProfiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile resource to create.  
`connectionProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The connection profile identifier.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ConnectionProfile connectionProfile = new ConnectionProfile();
    string connectionProfileId = "";
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.CreateConnectionProfileAsync(parent, connectionProfile, connectionProfileId);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnection(LocationName, PrivateConnection, string, CallSettings)
    
    
    public virtual Operation<PrivateConnection, OperationMetadata> CreatePrivateConnection(LocationName parent, PrivateConnection privateConnection, string privateConnectionId, CallSettings callSettings = null)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)`  
Required. The Private Connectivity resource to create.  
`privateConnectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The private connectivity identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    PrivateConnection privateConnection = new PrivateConnection();
    string privateConnectionId = "";
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = datastreamClient.CreatePrivateConnection(parent, privateConnection, privateConnectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreatePrivateConnection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnection(CreatePrivateConnectionRequest, CallSettings)
    
    
    public virtual Operation<PrivateConnection, OperationMetadata> CreatePrivateConnection(CreatePrivateConnectionRequest request, CallSettings callSettings = null)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreatePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    CreatePrivateConnectionRequest request = new CreatePrivateConnectionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        PrivateConnectionId = "",
        PrivateConnection = new PrivateConnection(),
        RequestId = "",
        Force = false,
        ValidateOnly = false,
    };
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = datastreamClient.CreatePrivateConnection(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreatePrivateConnection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnection(string, PrivateConnection, string, CallSettings)
    
    
    public virtual Operation<PrivateConnection, OperationMetadata> CreatePrivateConnection(string parent, PrivateConnection privateConnection, string privateConnectionId, CallSettings callSettings = null)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)`  
Required. The Private Connectivity resource to create.  
`privateConnectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The private connectivity identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    PrivateConnection privateConnection = new PrivateConnection();
    string privateConnectionId = "";
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = datastreamClient.CreatePrivateConnection(parent, privateConnection, privateConnectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreatePrivateConnection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnectionAsync(LocationName, PrivateConnection, string, CallSettings)
    
    
    public virtual Task<Operation<PrivateConnection, OperationMetadata>> CreatePrivateConnectionAsync(LocationName parent, PrivateConnection privateConnection, string privateConnectionId, CallSettings callSettings = null)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)`  
Required. The Private Connectivity resource to create.  
`privateConnectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The private connectivity identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    PrivateConnection privateConnection = new PrivateConnection();
    string privateConnectionId = "";
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = await datastreamClient.CreatePrivateConnectionAsync(parent, privateConnection, privateConnectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreatePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnectionAsync(LocationName, PrivateConnection, string, CancellationToken)
    
    
    public virtual Task<Operation<PrivateConnection, OperationMetadata>> CreatePrivateConnectionAsync(LocationName parent, PrivateConnection privateConnection, string privateConnectionId, CancellationToken cancellationToken)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)`  
Required. The Private Connectivity resource to create.  
`privateConnectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The private connectivity identifier.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    PrivateConnection privateConnection = new PrivateConnection();
    string privateConnectionId = "";
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = await datastreamClient.CreatePrivateConnectionAsync(parent, privateConnection, privateConnectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreatePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnectionAsync(CreatePrivateConnectionRequest, CallSettings)
    
    
    public virtual Task<Operation<PrivateConnection, OperationMetadata>> CreatePrivateConnectionAsync(CreatePrivateConnectionRequest request, CallSettings callSettings = null)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreatePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    CreatePrivateConnectionRequest request = new CreatePrivateConnectionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        PrivateConnectionId = "",
        PrivateConnection = new PrivateConnection(),
        RequestId = "",
        Force = false,
        ValidateOnly = false,
    };
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = await datastreamClient.CreatePrivateConnectionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreatePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnectionAsync(CreatePrivateConnectionRequest, CancellationToken)
    
    
    public virtual Task<Operation<PrivateConnection, OperationMetadata>> CreatePrivateConnectionAsync(CreatePrivateConnectionRequest request, CancellationToken cancellationToken)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreatePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    CreatePrivateConnectionRequest request = new CreatePrivateConnectionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        PrivateConnectionId = "",
        PrivateConnection = new PrivateConnection(),
        RequestId = "",
        Force = false,
        ValidateOnly = false,
    };
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = await datastreamClient.CreatePrivateConnectionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreatePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnectionAsync(string, PrivateConnection, string, CallSettings)
    
    
    public virtual Task<Operation<PrivateConnection, OperationMetadata>> CreatePrivateConnectionAsync(string parent, PrivateConnection privateConnection, string privateConnectionId, CallSettings callSettings = null)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)`  
Required. The Private Connectivity resource to create.  
`privateConnectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The private connectivity identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    PrivateConnection privateConnection = new PrivateConnection();
    string privateConnectionId = "";
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = await datastreamClient.CreatePrivateConnectionAsync(parent, privateConnection, privateConnectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreatePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreatePrivateConnectionAsync(string, PrivateConnection, string, CancellationToken)
    
    
    public virtual Task<Operation<PrivateConnection, OperationMetadata>> CreatePrivateConnectionAsync(string parent, PrivateConnection privateConnection, string privateConnectionId, CancellationToken cancellationToken)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)`  
Required. The Private Connectivity resource to create.  
`privateConnectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The private connectivity identifier.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    PrivateConnection privateConnection = new PrivateConnection();
    string privateConnectionId = "";
    // Make the request
    Operation<PrivateConnection, OperationMetadata> response = await datastreamClient.CreatePrivateConnectionAsync(parent, privateConnection, privateConnectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<PrivateConnection, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PrivateConnection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PrivateConnection, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreatePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PrivateConnection retrievedResult = retrievedResponse.Result;
    }
    

### CreateRoute(CreateRouteRequest, CallSettings)
    
    
    public virtual Operation<Route, OperationMetadata> CreateRoute(CreateRouteRequest request, CallSettings callSettings = null)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    CreateRouteRequest request = new CreateRouteRequest
    {
        ParentAsPrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
        RouteId = "",
        Route = new Route(),
        RequestId = "",
    };
    // Make the request
    Operation<Route, OperationMetadata> response = datastreamClient.CreateRoute(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateRoute(PrivateConnectionName, Route, string, CallSettings)
    
    
    public virtual Operation<Route, OperationMetadata> CreateRoute(PrivateConnectionName parent, Route route, string routeId, CallSettings callSettings = null)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The parent that owns the collection of Routes.  
`route` | `[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)`  
Required. The Route resource to create.  
`routeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Route identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    PrivateConnectionName parent = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    Route route = new Route();
    string routeId = "";
    // Make the request
    Operation<Route, OperationMetadata> response = datastreamClient.CreateRoute(parent, route, routeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateRoute(string, Route, string, CallSettings)
    
    
    public virtual Operation<Route, OperationMetadata> CreateRoute(string parent, Route route, string routeId, CallSettings callSettings = null)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of Routes.  
`route` | `[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)`  
Required. The Route resource to create.  
`routeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Route identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    Route route = new Route();
    string routeId = "";
    // Make the request
    Operation<Route, OperationMetadata> response = datastreamClient.CreateRoute(parent, route, routeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateRouteAsync(CreateRouteRequest, CallSettings)
    
    
    public virtual Task<Operation<Route, OperationMetadata>> CreateRouteAsync(CreateRouteRequest request, CallSettings callSettings = null)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    CreateRouteRequest request = new CreateRouteRequest
    {
        ParentAsPrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
        RouteId = "",
        Route = new Route(),
        RequestId = "",
    };
    // Make the request
    Operation<Route, OperationMetadata> response = await datastreamClient.CreateRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateRouteAsync(CreateRouteRequest, CancellationToken)
    
    
    public virtual Task<Operation<Route, OperationMetadata>> CreateRouteAsync(CreateRouteRequest request, CancellationToken cancellationToken)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateRouteRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    CreateRouteRequest request = new CreateRouteRequest
    {
        ParentAsPrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
        RouteId = "",
        Route = new Route(),
        RequestId = "",
    };
    // Make the request
    Operation<Route, OperationMetadata> response = await datastreamClient.CreateRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateRouteAsync(PrivateConnectionName, Route, string, CallSettings)
    
    
    public virtual Task<Operation<Route, OperationMetadata>> CreateRouteAsync(PrivateConnectionName parent, Route route, string routeId, CallSettings callSettings = null)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The parent that owns the collection of Routes.  
`route` | `[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)`  
Required. The Route resource to create.  
`routeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Route identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    PrivateConnectionName parent = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    Route route = new Route();
    string routeId = "";
    // Make the request
    Operation<Route, OperationMetadata> response = await datastreamClient.CreateRouteAsync(parent, route, routeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateRouteAsync(PrivateConnectionName, Route, string, CancellationToken)
    
    
    public virtual Task<Operation<Route, OperationMetadata>> CreateRouteAsync(PrivateConnectionName parent, Route route, string routeId, CancellationToken cancellationToken)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The parent that owns the collection of Routes.  
`route` | `[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)`  
Required. The Route resource to create.  
`routeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Route identifier.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    PrivateConnectionName parent = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    Route route = new Route();
    string routeId = "";
    // Make the request
    Operation<Route, OperationMetadata> response = await datastreamClient.CreateRouteAsync(parent, route, routeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateRouteAsync(string, Route, string, CallSettings)
    
    
    public virtual Task<Operation<Route, OperationMetadata>> CreateRouteAsync(string parent, Route route, string routeId, CallSettings callSettings = null)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of Routes.  
`route` | `[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)`  
Required. The Route resource to create.  
`routeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Route identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    Route route = new Route();
    string routeId = "";
    // Make the request
    Operation<Route, OperationMetadata> response = await datastreamClient.CreateRouteAsync(parent, route, routeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateRouteAsync(string, Route, string, CancellationToken)
    
    
    public virtual Task<Operation<Route, OperationMetadata>> CreateRouteAsync(string parent, Route route, string routeId, CancellationToken cancellationToken)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of Routes.  
`route` | `[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)`  
Required. The Route resource to create.  
`routeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Route identifier.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    Route route = new Route();
    string routeId = "";
    // Make the request
    Operation<Route, OperationMetadata> response = await datastreamClient.CreateRouteAsync(parent, route, routeId);
    
    // Poll until the returned long-running operation is complete
    Operation<Route, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Route result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Route, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Route retrievedResult = retrievedResponse.Result;
    }
    

### CreateStream(LocationName, Stream, string, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> CreateStream(LocationName parent, Stream stream, string streamId, CallSettings callSettings = null)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of streams.  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to create.  
`streamId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The stream identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Stream stream = new Stream();
    string streamId = "";
    // Make the request
    Operation<Stream, OperationMetadata> response = datastreamClient.CreateStream(parent, stream, streamId);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### CreateStream(CreateStreamRequest, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> CreateStream(CreateStreamRequest request, CallSettings callSettings = null)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    CreateStreamRequest request = new CreateStreamRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        StreamId = "",
        Stream = new Stream(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = datastreamClient.CreateStream(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### CreateStream(string, Stream, string, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> CreateStream(string parent, Stream stream, string streamId, CallSettings callSettings = null)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of streams.  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to create.  
`streamId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The stream identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Stream stream = new Stream();
    string streamId = "";
    // Make the request
    Operation<Stream, OperationMetadata> response = datastreamClient.CreateStream(parent, stream, streamId);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = datastreamClient.PollOnceCreateStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### CreateStreamAsync(LocationName, Stream, string, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> CreateStreamAsync(LocationName parent, Stream stream, string streamId, CallSettings callSettings = null)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of streams.  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to create.  
`streamId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The stream identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Stream stream = new Stream();
    string streamId = "";
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.CreateStreamAsync(parent, stream, streamId);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### CreateStreamAsync(LocationName, Stream, string, CancellationToken)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> CreateStreamAsync(LocationName parent, Stream stream, string streamId, CancellationToken cancellationToken)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of streams.  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to create.  
`streamId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The stream identifier.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Stream stream = new Stream();
    string streamId = "";
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.CreateStreamAsync(parent, stream, streamId);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### CreateStreamAsync(CreateStreamRequest, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> CreateStreamAsync(CreateStreamRequest request, CallSettings callSettings = null)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    CreateStreamRequest request = new CreateStreamRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        StreamId = "",
        Stream = new Stream(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.CreateStreamAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### CreateStreamAsync(CreateStreamRequest, CancellationToken)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> CreateStreamAsync(CreateStreamRequest request, CancellationToken cancellationToken)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateStreamRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    CreateStreamRequest request = new CreateStreamRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        StreamId = "",
        Stream = new Stream(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.CreateStreamAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### CreateStreamAsync(string, Stream, string, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> CreateStreamAsync(string parent, Stream stream, string streamId, CallSettings callSettings = null)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of streams.  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to create.  
`streamId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The stream identifier.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Stream stream = new Stream();
    string streamId = "";
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.CreateStreamAsync(parent, stream, streamId);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### CreateStreamAsync(string, Stream, string, CancellationToken)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> CreateStreamAsync(string parent, Stream stream, string streamId, CancellationToken cancellationToken)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of streams.  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to create.  
`streamId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The stream identifier.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Stream stream = new Stream();
    string streamId = "";
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.CreateStreamAsync(parent, stream, streamId);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceCreateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfile(ConnectionProfileName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteConnectionProfile(ConnectionProfileName name, CallSettings callSettings = null)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectionProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfileName)`  
Required. The name of the connection profile resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    ConnectionProfileName name = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteConnectionProfile(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteConnectionProfile(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfile(DeleteConnectionProfileRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteConnectionProfile(DeleteConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    DeleteConnectionProfileRequest request = new DeleteConnectionProfileRequest
    {
        ConnectionProfileName = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteConnectionProfile(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteConnectionProfile(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfile(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteConnectionProfile(string name, CallSettings callSettings = null)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connection profile resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectionProfiles/[CONNECTION_PROFILE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteConnectionProfile(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteConnectionProfile(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfileAsync(ConnectionProfileName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectionProfileAsync(ConnectionProfileName name, CallSettings callSettings = null)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectionProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfileName)`  
Required. The name of the connection profile resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ConnectionProfileName name = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteConnectionProfileAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfileAsync(ConnectionProfileName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectionProfileAsync(ConnectionProfileName name, CancellationToken cancellationToken)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectionProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfileName)`  
Required. The name of the connection profile resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ConnectionProfileName name = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteConnectionProfileAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfileAsync(DeleteConnectionProfileRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectionProfileAsync(DeleteConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConnectionProfileRequest request = new DeleteConnectionProfileRequest
    {
        ConnectionProfileName = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteConnectionProfileAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfileAsync(DeleteConnectionProfileRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectionProfileAsync(DeleteConnectionProfileRequest request, CancellationToken cancellationToken)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConnectionProfileRequest request = new DeleteConnectionProfileRequest
    {
        ConnectionProfileName = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteConnectionProfileAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfileAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectionProfileAsync(string name, CallSettings callSettings = null)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connection profile resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectionProfiles/[CONNECTION_PROFILE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteConnectionProfileAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConnectionProfileAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteConnectionProfileAsync(string name, CancellationToken cancellationToken)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connection profile resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectionProfiles/[CONNECTION_PROFILE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteConnectionProfileAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnection(DeletePrivateConnectionRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeletePrivateConnection(DeletePrivateConnectionRequest request, CallSettings callSettings = null)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeletePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    DeletePrivateConnectionRequest request = new DeletePrivateConnectionRequest
    {
        PrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeletePrivateConnection(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeletePrivateConnection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnection(PrivateConnectionName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeletePrivateConnection(PrivateConnectionName name, CallSettings callSettings = null)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The name of the private connectivity configuration to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    PrivateConnectionName name = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeletePrivateConnection(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeletePrivateConnection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnection(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeletePrivateConnection(string name, CallSettings callSettings = null)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the private connectivity configuration to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeletePrivateConnection(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeletePrivateConnection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnectionAsync(DeletePrivateConnectionRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrivateConnectionAsync(DeletePrivateConnectionRequest request, CallSettings callSettings = null)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeletePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DeletePrivateConnectionRequest request = new DeletePrivateConnectionRequest
    {
        PrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeletePrivateConnectionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeletePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnectionAsync(DeletePrivateConnectionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrivateConnectionAsync(DeletePrivateConnectionRequest request, CancellationToken cancellationToken)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeletePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DeletePrivateConnectionRequest request = new DeletePrivateConnectionRequest
    {
        PrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeletePrivateConnectionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeletePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnectionAsync(PrivateConnectionName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrivateConnectionAsync(PrivateConnectionName name, CallSettings callSettings = null)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The name of the private connectivity configuration to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    PrivateConnectionName name = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeletePrivateConnectionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeletePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnectionAsync(PrivateConnectionName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrivateConnectionAsync(PrivateConnectionName name, CancellationToken cancellationToken)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The name of the private connectivity configuration to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    PrivateConnectionName name = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeletePrivateConnectionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeletePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnectionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrivateConnectionAsync(string name, CallSettings callSettings = null)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the private connectivity configuration to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeletePrivateConnectionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeletePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePrivateConnectionAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePrivateConnectionAsync(string name, CancellationToken cancellationToken)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the private connectivity configuration to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeletePrivateConnectionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeletePrivateConnectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRoute(DeleteRouteRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRoute(DeleteRouteRequest request, CallSettings callSettings = null)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    DeleteRouteRequest request = new DeleteRouteRequest
    {
        RouteName = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteRoute(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRoute(RouteName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRoute(RouteName name, CallSettings callSettings = null)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RouteName)`  
Required. The name of the Route resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    RouteName name = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteRoute(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRoute(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRoute(string name, CallSettings callSettings = null)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Route resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]/routes/[ROUTE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteRoute(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteRoute(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRouteAsync(DeleteRouteRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRouteAsync(DeleteRouteRequest request, CallSettings callSettings = null)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DeleteRouteRequest request = new DeleteRouteRequest
    {
        RouteName = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRouteAsync(DeleteRouteRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRouteAsync(DeleteRouteRequest request, CancellationToken cancellationToken)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteRouteRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DeleteRouteRequest request = new DeleteRouteRequest
    {
        RouteName = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteRouteAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRouteAsync(RouteName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRouteAsync(RouteName name, CallSettings callSettings = null)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RouteName)`  
Required. The name of the Route resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    RouteName name = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteRouteAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRouteAsync(RouteName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRouteAsync(RouteName name, CancellationToken cancellationToken)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RouteName)`  
Required. The name of the Route resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    RouteName name = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteRouteAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRouteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRouteAsync(string name, CallSettings callSettings = null)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Route resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]/routes/[ROUTE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteRouteAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRouteAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRouteAsync(string name, CancellationToken cancellationToken)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Route resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]/routes/[ROUTE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteRouteAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteRouteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStream(DeleteStreamRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteStream(DeleteStreamRequest request, CallSettings callSettings = null)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    DeleteStreamRequest request = new DeleteStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteStream(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStream(StreamName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteStream(StreamName name, CallSettings callSettings = null)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)`  
Required. The name of the stream resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    StreamName name = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]");
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteStream(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStream(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteStream(string name, CallSettings callSettings = null)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]";
    // Make the request
    Operation<Empty, OperationMetadata> response = datastreamClient.DeleteStream(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = datastreamClient.PollOnceDeleteStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStreamAsync(DeleteStreamRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteStreamAsync(DeleteStreamRequest request, CallSettings callSettings = null)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DeleteStreamRequest request = new DeleteStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteStreamAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStreamAsync(DeleteStreamRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteStreamAsync(DeleteStreamRequest request, CancellationToken cancellationToken)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteStreamRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DeleteStreamRequest request = new DeleteStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteStreamAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStreamAsync(StreamName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteStreamAsync(StreamName name, CallSettings callSettings = null)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)`  
Required. The name of the stream resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamName name = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteStreamAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStreamAsync(StreamName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteStreamAsync(StreamName name, CancellationToken cancellationToken)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)`  
Required. The name of the stream resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamName name = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteStreamAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStreamAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteStreamAsync(string name, CallSettings callSettings = null)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteStreamAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteStreamAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteStreamAsync(string name, CancellationToken cancellationToken)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await datastreamClient.DeleteStreamAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceDeleteStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DiscoverConnectionProfile(DiscoverConnectionProfileRequest, CallSettings)
    
    
    public virtual DiscoverConnectionProfileResponse DiscoverConnectionProfile(DiscoverConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    DiscoverConnectionProfileRequest request = new DiscoverConnectionProfileRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FullHierarchy = false,
        OracleRdbms = new OracleRdbms(),
        ConnectionProfile = new ConnectionProfile(),
    };
    // Make the request
    DiscoverConnectionProfileResponse response = datastreamClient.DiscoverConnectionProfile(request);
    

### DiscoverConnectionProfileAsync(DiscoverConnectionProfileRequest, CallSettings)
    
    
    public virtual Task<DiscoverConnectionProfileResponse> DiscoverConnectionProfileAsync(DiscoverConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DiscoverConnectionProfileRequest request = new DiscoverConnectionProfileRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FullHierarchy = false,
        OracleRdbms = new OracleRdbms(),
        ConnectionProfile = new ConnectionProfile(),
    };
    // Make the request
    DiscoverConnectionProfileResponse response = await datastreamClient.DiscoverConnectionProfileAsync(request);
    

### DiscoverConnectionProfileAsync(DiscoverConnectionProfileRequest, CancellationToken)
    
    
    public virtual Task<DiscoverConnectionProfileResponse> DiscoverConnectionProfileAsync(DiscoverConnectionProfileRequest request, CancellationToken cancellationToken)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    DiscoverConnectionProfileRequest request = new DiscoverConnectionProfileRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FullHierarchy = false,
        OracleRdbms = new OracleRdbms(),
        ConnectionProfile = new ConnectionProfile(),
    };
    // Make the request
    DiscoverConnectionProfileResponse response = await datastreamClient.DiscoverConnectionProfileAsync(request);
    

### FetchStaticIps(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<FetchStaticIpsResponse, string> FetchStaticIps(LocationName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)[string](https://learn.microsoft.com/dotnet/api/system.string)` | A pageable sequence of [string](https://learn.microsoft.com/dotnet/api/system.string) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    LocationName name = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<FetchStaticIpsResponse, string> response = datastreamClient.FetchStaticIps(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (string item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (FetchStaticIpsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (string item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<string> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (string item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### FetchStaticIps(FetchStaticIpsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<FetchStaticIpsResponse, string> FetchStaticIps(FetchStaticIpsRequest request, CallSettings callSettings = null)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)[string](https://learn.microsoft.com/dotnet/api/system.string)` | A pageable sequence of [string](https://learn.microsoft.com/dotnet/api/system.string) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    FetchStaticIpsRequest request = new FetchStaticIpsRequest
    {
        LocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<FetchStaticIpsResponse, string> response = datastreamClient.FetchStaticIps(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (string item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (FetchStaticIpsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (string item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<string> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (string item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### FetchStaticIps(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<FetchStaticIpsResponse, string> FetchStaticIps(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)[string](https://learn.microsoft.com/dotnet/api/system.string)` | A pageable sequence of [string](https://learn.microsoft.com/dotnet/api/system.string) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<FetchStaticIpsResponse, string> response = datastreamClient.FetchStaticIps(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (string item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (FetchStaticIpsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (string item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<string> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (string item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### FetchStaticIpsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<FetchStaticIpsResponse, string> FetchStaticIpsAsync(LocationName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)[string](https://learn.microsoft.com/dotnet/api/system.string)` | A pageable asynchronous sequence of [string](https://learn.microsoft.com/dotnet/api/system.string) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName name = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<FetchStaticIpsResponse, string> response = datastreamClient.FetchStaticIpsAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((string item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((FetchStaticIpsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (string item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<string> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (string item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### FetchStaticIpsAsync(FetchStaticIpsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<FetchStaticIpsResponse, string> FetchStaticIpsAsync(FetchStaticIpsRequest request, CallSettings callSettings = null)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)[string](https://learn.microsoft.com/dotnet/api/system.string)` | A pageable asynchronous sequence of [string](https://learn.microsoft.com/dotnet/api/system.string) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    FetchStaticIpsRequest request = new FetchStaticIpsRequest
    {
        LocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<FetchStaticIpsResponse, string> response = datastreamClient.FetchStaticIpsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((string item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((FetchStaticIpsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (string item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<string> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (string item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### FetchStaticIpsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<FetchStaticIpsResponse, string> FetchStaticIpsAsync(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)[string](https://learn.microsoft.com/dotnet/api/system.string)` | A pageable asynchronous sequence of [string](https://learn.microsoft.com/dotnet/api/system.string) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<FetchStaticIpsResponse, string> response = datastreamClient.FetchStaticIpsAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((string item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((FetchStaticIpsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (string item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<string> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (string item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### GetConnectionProfile(ConnectionProfileName, CallSettings)
    
    
    public virtual ConnectionProfile GetConnectionProfile(ConnectionProfileName name, CallSettings callSettings = null)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectionProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfileName)`  
Required. The name of the connection profile resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    ConnectionProfileName name = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
    // Make the request
    ConnectionProfile response = datastreamClient.GetConnectionProfile(name);
    

### GetConnectionProfile(GetConnectionProfileRequest, CallSettings)
    
    
    public virtual ConnectionProfile GetConnectionProfile(GetConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    GetConnectionProfileRequest request = new GetConnectionProfileRequest
    {
        ConnectionProfileName = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]"),
    };
    // Make the request
    ConnectionProfile response = datastreamClient.GetConnectionProfile(request);
    

### GetConnectionProfile(string, CallSettings)
    
    
    public virtual ConnectionProfile GetConnectionProfile(string name, CallSettings callSettings = null)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connection profile resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectionProfiles/[CONNECTION_PROFILE]";
    // Make the request
    ConnectionProfile response = datastreamClient.GetConnectionProfile(name);
    

### GetConnectionProfileAsync(ConnectionProfileName, CallSettings)
    
    
    public virtual Task<ConnectionProfile> GetConnectionProfileAsync(ConnectionProfileName name, CallSettings callSettings = null)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectionProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfileName)`  
Required. The name of the connection profile resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ConnectionProfileName name = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
    // Make the request
    ConnectionProfile response = await datastreamClient.GetConnectionProfileAsync(name);
    

### GetConnectionProfileAsync(ConnectionProfileName, CancellationToken)
    
    
    public virtual Task<ConnectionProfile> GetConnectionProfileAsync(ConnectionProfileName name, CancellationToken cancellationToken)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConnectionProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfileName)`  
Required. The name of the connection profile resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ConnectionProfileName name = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
    // Make the request
    ConnectionProfile response = await datastreamClient.GetConnectionProfileAsync(name);
    

### GetConnectionProfileAsync(GetConnectionProfileRequest, CallSettings)
    
    
    public virtual Task<ConnectionProfile> GetConnectionProfileAsync(GetConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetConnectionProfileRequest request = new GetConnectionProfileRequest
    {
        ConnectionProfileName = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]"),
    };
    // Make the request
    ConnectionProfile response = await datastreamClient.GetConnectionProfileAsync(request);
    

### GetConnectionProfileAsync(GetConnectionProfileRequest, CancellationToken)
    
    
    public virtual Task<ConnectionProfile> GetConnectionProfileAsync(GetConnectionProfileRequest request, CancellationToken cancellationToken)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetConnectionProfileRequest request = new GetConnectionProfileRequest
    {
        ConnectionProfileName = ConnectionProfileName.FromProjectLocationConnectionProfile("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]"),
    };
    // Make the request
    ConnectionProfile response = await datastreamClient.GetConnectionProfileAsync(request);
    

### GetConnectionProfileAsync(string, CallSettings)
    
    
    public virtual Task<ConnectionProfile> GetConnectionProfileAsync(string name, CallSettings callSettings = null)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connection profile resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectionProfiles/[CONNECTION_PROFILE]";
    // Make the request
    ConnectionProfile response = await datastreamClient.GetConnectionProfileAsync(name);
    

### GetConnectionProfileAsync(string, CancellationToken)
    
    
    public virtual Task<ConnectionProfile> GetConnectionProfileAsync(string name, CancellationToken cancellationToken)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the connection profile resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/connectionProfiles/[CONNECTION_PROFILE]";
    // Make the request
    ConnectionProfile response = await datastreamClient.GetConnectionProfileAsync(name);
    

### GetPrivateConnection(GetPrivateConnectionRequest, CallSettings)
    
    
    public virtual PrivateConnection GetPrivateConnection(GetPrivateConnectionRequest request, CallSettings callSettings = null)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetPrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    GetPrivateConnectionRequest request = new GetPrivateConnectionRequest
    {
        PrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
    };
    // Make the request
    PrivateConnection response = datastreamClient.GetPrivateConnection(request);
    

### GetPrivateConnection(PrivateConnectionName, CallSettings)
    
    
    public virtual PrivateConnection GetPrivateConnection(PrivateConnectionName name, CallSettings callSettings = null)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The name of the private connectivity configuration to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    PrivateConnectionName name = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    // Make the request
    PrivateConnection response = datastreamClient.GetPrivateConnection(name);
    

### GetPrivateConnection(string, CallSettings)
    
    
    public virtual PrivateConnection GetPrivateConnection(string name, CallSettings callSettings = null)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the private connectivity configuration to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    // Make the request
    PrivateConnection response = datastreamClient.GetPrivateConnection(name);
    

### GetPrivateConnectionAsync(GetPrivateConnectionRequest, CallSettings)
    
    
    public virtual Task<PrivateConnection> GetPrivateConnectionAsync(GetPrivateConnectionRequest request, CallSettings callSettings = null)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetPrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetPrivateConnectionRequest request = new GetPrivateConnectionRequest
    {
        PrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
    };
    // Make the request
    PrivateConnection response = await datastreamClient.GetPrivateConnectionAsync(request);
    

### GetPrivateConnectionAsync(GetPrivateConnectionRequest, CancellationToken)
    
    
    public virtual Task<PrivateConnection> GetPrivateConnectionAsync(GetPrivateConnectionRequest request, CancellationToken cancellationToken)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetPrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetPrivateConnectionRequest request = new GetPrivateConnectionRequest
    {
        PrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
    };
    // Make the request
    PrivateConnection response = await datastreamClient.GetPrivateConnectionAsync(request);
    

### GetPrivateConnectionAsync(PrivateConnectionName, CallSettings)
    
    
    public virtual Task<PrivateConnection> GetPrivateConnectionAsync(PrivateConnectionName name, CallSettings callSettings = null)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The name of the private connectivity configuration to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    PrivateConnectionName name = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    // Make the request
    PrivateConnection response = await datastreamClient.GetPrivateConnectionAsync(name);
    

### GetPrivateConnectionAsync(PrivateConnectionName, CancellationToken)
    
    
    public virtual Task<PrivateConnection> GetPrivateConnectionAsync(PrivateConnectionName name, CancellationToken cancellationToken)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The name of the private connectivity configuration to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    PrivateConnectionName name = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    // Make the request
    PrivateConnection response = await datastreamClient.GetPrivateConnectionAsync(name);
    

### GetPrivateConnectionAsync(string, CallSettings)
    
    
    public virtual Task<PrivateConnection> GetPrivateConnectionAsync(string name, CallSettings callSettings = null)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the private connectivity configuration to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    // Make the request
    PrivateConnection response = await datastreamClient.GetPrivateConnectionAsync(name);
    

### GetPrivateConnectionAsync(string, CancellationToken)
    
    
    public virtual Task<PrivateConnection> GetPrivateConnectionAsync(string name, CancellationToken cancellationToken)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the private connectivity configuration to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    // Make the request
    PrivateConnection response = await datastreamClient.GetPrivateConnectionAsync(name);
    

### GetRoute(GetRouteRequest, CallSettings)
    
    
    public virtual Route GetRoute(GetRouteRequest request, CallSettings callSettings = null)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    GetRouteRequest request = new GetRouteRequest
    {
        RouteName = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]"),
    };
    // Make the request
    Route response = datastreamClient.GetRoute(request);
    

### GetRoute(RouteName, CallSettings)
    
    
    public virtual Route GetRoute(RouteName name, CallSettings callSettings = null)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RouteName)`  
Required. The name of the Route resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    RouteName name = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]");
    // Make the request
    Route response = datastreamClient.GetRoute(name);
    

### GetRoute(string, CallSettings)
    
    
    public virtual Route GetRoute(string name, CallSettings callSettings = null)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Route resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]/routes/[ROUTE]";
    // Make the request
    Route response = datastreamClient.GetRoute(name);
    

### GetRouteAsync(GetRouteRequest, CallSettings)
    
    
    public virtual Task<Route> GetRouteAsync(GetRouteRequest request, CallSettings callSettings = null)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetRouteRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetRouteRequest request = new GetRouteRequest
    {
        RouteName = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]"),
    };
    // Make the request
    Route response = await datastreamClient.GetRouteAsync(request);
    

### GetRouteAsync(GetRouteRequest, CancellationToken)
    
    
    public virtual Task<Route> GetRouteAsync(GetRouteRequest request, CancellationToken cancellationToken)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetRouteRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetRouteRequest request = new GetRouteRequest
    {
        RouteName = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]"),
    };
    // Make the request
    Route response = await datastreamClient.GetRouteAsync(request);
    

### GetRouteAsync(RouteName, CallSettings)
    
    
    public virtual Task<Route> GetRouteAsync(RouteName name, CallSettings callSettings = null)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RouteName)`  
Required. The name of the Route resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    RouteName name = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]");
    // Make the request
    Route response = await datastreamClient.GetRouteAsync(name);
    

### GetRouteAsync(RouteName, CancellationToken)
    
    
    public virtual Task<Route> GetRouteAsync(RouteName name, CancellationToken cancellationToken)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RouteName)`  
Required. The name of the Route resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    RouteName name = RouteName.FromProjectLocationPrivateConnectionRoute("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]");
    // Make the request
    Route response = await datastreamClient.GetRouteAsync(name);
    

### GetRouteAsync(string, CallSettings)
    
    
    public virtual Task<Route> GetRouteAsync(string name, CallSettings callSettings = null)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Route resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]/routes/[ROUTE]";
    // Make the request
    Route response = await datastreamClient.GetRouteAsync(name);
    

### GetRouteAsync(string, CancellationToken)
    
    
    public virtual Task<Route> GetRouteAsync(string name, CancellationToken cancellationToken)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Route resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]/routes/[ROUTE]";
    // Make the request
    Route response = await datastreamClient.GetRouteAsync(name);
    

### GetStream(GetStreamRequest, CallSettings)
    
    
    public virtual Stream GetStream(GetStreamRequest request, CallSettings callSettings = null)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    GetStreamRequest request = new GetStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
    };
    // Make the request
    Stream response = datastreamClient.GetStream(request);
    

### GetStream(StreamName, CallSettings)
    
    
    public virtual Stream GetStream(StreamName name, CallSettings callSettings = null)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)`  
Required. The name of the stream resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    StreamName name = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]");
    // Make the request
    Stream response = datastreamClient.GetStream(name);
    

### GetStream(string, CallSettings)
    
    
    public virtual Stream GetStream(string name, CallSettings callSettings = null)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]";
    // Make the request
    Stream response = datastreamClient.GetStream(name);
    

### GetStreamAsync(GetStreamRequest, CallSettings)
    
    
    public virtual Task<Stream> GetStreamAsync(GetStreamRequest request, CallSettings callSettings = null)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetStreamRequest request = new GetStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
    };
    // Make the request
    Stream response = await datastreamClient.GetStreamAsync(request);
    

### GetStreamAsync(GetStreamRequest, CancellationToken)
    
    
    public virtual Task<Stream> GetStreamAsync(GetStreamRequest request, CancellationToken cancellationToken)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetStreamRequest request = new GetStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
    };
    // Make the request
    Stream response = await datastreamClient.GetStreamAsync(request);
    

### GetStreamAsync(StreamName, CallSettings)
    
    
    public virtual Task<Stream> GetStreamAsync(StreamName name, CallSettings callSettings = null)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)`  
Required. The name of the stream resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamName name = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]");
    // Make the request
    Stream response = await datastreamClient.GetStreamAsync(name);
    

### GetStreamAsync(StreamName, CancellationToken)
    
    
    public virtual Task<Stream> GetStreamAsync(StreamName name, CancellationToken cancellationToken)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)`  
Required. The name of the stream resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamName name = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]");
    // Make the request
    Stream response = await datastreamClient.GetStreamAsync(name);
    

### GetStreamAsync(string, CallSettings)
    
    
    public virtual Task<Stream> GetStreamAsync(string name, CallSettings callSettings = null)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]";
    // Make the request
    Stream response = await datastreamClient.GetStreamAsync(name);
    

### GetStreamAsync(string, CancellationToken)
    
    
    public virtual Task<Stream> GetStreamAsync(string name, CancellationToken cancellationToken)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]";
    // Make the request
    Stream response = await datastreamClient.GetStreamAsync(name);
    

### GetStreamObject(GetStreamObjectRequest, CallSettings)
    
    
    public virtual StreamObject GetStreamObject(GetStreamObjectRequest request, CallSettings callSettings = null)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamObjectRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    GetStreamObjectRequest request = new GetStreamObjectRequest
    {
        StreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StreamObject response = datastreamClient.GetStreamObject(request);
    

### GetStreamObject(StreamObjectName, CallSettings)
    
    
    public virtual StreamObject GetStreamObject(StreamObjectName name, CallSettings callSettings = null)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    StreamObjectName name = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StreamObject response = datastreamClient.GetStreamObject(name);
    

### GetStreamObject(string, CallSettings)
    
    
    public virtual StreamObject GetStreamObject(string name, CallSettings callSettings = null)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StreamObject response = datastreamClient.GetStreamObject(name);
    

### GetStreamObjectAsync(GetStreamObjectRequest, CallSettings)
    
    
    public virtual Task<StreamObject> GetStreamObjectAsync(GetStreamObjectRequest request, CallSettings callSettings = null)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamObjectRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetStreamObjectRequest request = new GetStreamObjectRequest
    {
        StreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StreamObject response = await datastreamClient.GetStreamObjectAsync(request);
    

### GetStreamObjectAsync(GetStreamObjectRequest, CancellationToken)
    
    
    public virtual Task<StreamObject> GetStreamObjectAsync(GetStreamObjectRequest request, CancellationToken cancellationToken)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamObjectRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    GetStreamObjectRequest request = new GetStreamObjectRequest
    {
        StreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StreamObject response = await datastreamClient.GetStreamObjectAsync(request);
    

### GetStreamObjectAsync(StreamObjectName, CallSettings)
    
    
    public virtual Task<StreamObject> GetStreamObjectAsync(StreamObjectName name, CallSettings callSettings = null)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamObjectName name = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StreamObject response = await datastreamClient.GetStreamObjectAsync(name);
    

### GetStreamObjectAsync(StreamObjectName, CancellationToken)
    
    
    public virtual Task<StreamObject> GetStreamObjectAsync(StreamObjectName name, CancellationToken cancellationToken)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamObjectName name = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StreamObject response = await datastreamClient.GetStreamObjectAsync(name);
    

### GetStreamObjectAsync(string, CallSettings)
    
    
    public virtual Task<StreamObject> GetStreamObjectAsync(string name, CallSettings callSettings = null)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StreamObject response = await datastreamClient.GetStreamObjectAsync(name);
    

### GetStreamObjectAsync(string, CancellationToken)
    
    
    public virtual Task<StreamObject> GetStreamObjectAsync(string name, CancellationToken cancellationToken)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StreamObject response = await datastreamClient.GetStreamObjectAsync(name);
    

### ListConnectionProfiles(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectionProfilesResponse, ConnectionProfile> ListConnectionProfiles(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of connection profiles.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A pageable sequence of [ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListConnectionProfilesResponse, ConnectionProfile> response = datastreamClient.ListConnectionProfiles(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConnectionProfile item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectionProfilesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectionProfile item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectionProfile> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectionProfile item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectionProfiles(ListConnectionProfilesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectionProfilesResponse, ConnectionProfile> ListConnectionProfiles(ListConnectionProfilesRequest request, CallSettings callSettings = null)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A pageable sequence of [ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    ListConnectionProfilesRequest request = new ListConnectionProfilesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListConnectionProfilesResponse, ConnectionProfile> response = datastreamClient.ListConnectionProfiles(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConnectionProfile item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectionProfilesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectionProfile item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectionProfile> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectionProfile item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectionProfiles(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectionProfilesResponse, ConnectionProfile> ListConnectionProfiles(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of connection profiles.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A pageable sequence of [ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListConnectionProfilesResponse, ConnectionProfile> response = datastreamClient.ListConnectionProfiles(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConnectionProfile item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectionProfilesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectionProfile item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectionProfile> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectionProfile item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectionProfilesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectionProfilesResponse, ConnectionProfile> ListConnectionProfilesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of connection profiles.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A pageable asynchronous sequence of [ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListConnectionProfilesResponse, ConnectionProfile> response = datastreamClient.ListConnectionProfilesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConnectionProfile item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectionProfilesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectionProfile item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectionProfile> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectionProfile item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectionProfilesAsync(ListConnectionProfilesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectionProfilesResponse, ConnectionProfile> ListConnectionProfilesAsync(ListConnectionProfilesRequest request, CallSettings callSettings = null)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A pageable asynchronous sequence of [ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ListConnectionProfilesRequest request = new ListConnectionProfilesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListConnectionProfilesResponse, ConnectionProfile> response = datastreamClient.ListConnectionProfilesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConnectionProfile item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectionProfilesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectionProfile item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectionProfile> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectionProfile item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectionProfilesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectionProfilesResponse, ConnectionProfile> ListConnectionProfilesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of connection profiles.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | A pageable asynchronous sequence of [ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListConnectionProfilesResponse, ConnectionProfile> response = datastreamClient.ListConnectionProfilesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConnectionProfile item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectionProfilesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConnectionProfile item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConnectionProfile> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConnectionProfile item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrivateConnections(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListPrivateConnectionsResponse, PrivateConnection> ListPrivateConnections(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of private connectivity configurations.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A pageable sequence of [PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListPrivateConnectionsResponse, PrivateConnection> response = datastreamClient.ListPrivateConnections(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PrivateConnection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListPrivateConnectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrivateConnection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrivateConnection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrivateConnection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrivateConnections(ListPrivateConnectionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListPrivateConnectionsResponse, PrivateConnection> ListPrivateConnections(ListPrivateConnectionsRequest request, CallSettings callSettings = null)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A pageable sequence of [PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    ListPrivateConnectionsRequest request = new ListPrivateConnectionsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListPrivateConnectionsResponse, PrivateConnection> response = datastreamClient.ListPrivateConnections(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PrivateConnection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListPrivateConnectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrivateConnection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrivateConnection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrivateConnection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrivateConnections(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListPrivateConnectionsResponse, PrivateConnection> ListPrivateConnections(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of private connectivity configurations.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A pageable sequence of [PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListPrivateConnectionsResponse, PrivateConnection> response = datastreamClient.ListPrivateConnections(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (PrivateConnection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListPrivateConnectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrivateConnection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrivateConnection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrivateConnection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrivateConnectionsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPrivateConnectionsResponse, PrivateConnection> ListPrivateConnectionsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of private connectivity configurations.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A pageable asynchronous sequence of [PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListPrivateConnectionsResponse, PrivateConnection> response = datastreamClient.ListPrivateConnectionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((PrivateConnection item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListPrivateConnectionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrivateConnection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrivateConnection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrivateConnection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrivateConnectionsAsync(ListPrivateConnectionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPrivateConnectionsResponse, PrivateConnection> ListPrivateConnectionsAsync(ListPrivateConnectionsRequest request, CallSettings callSettings = null)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A pageable asynchronous sequence of [PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ListPrivateConnectionsRequest request = new ListPrivateConnectionsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListPrivateConnectionsResponse, PrivateConnection> response = datastreamClient.ListPrivateConnectionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((PrivateConnection item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListPrivateConnectionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrivateConnection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrivateConnection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrivateConnection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPrivateConnectionsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPrivateConnectionsResponse, PrivateConnection> ListPrivateConnectionsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of private connectivity configurations.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | A pageable asynchronous sequence of [PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListPrivateConnectionsResponse, PrivateConnection> response = datastreamClient.ListPrivateConnectionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((PrivateConnection item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListPrivateConnectionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (PrivateConnection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<PrivateConnection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (PrivateConnection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutes(ListRoutesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListRoutesResponse, Route> ListRoutes(ListRoutesRequest request, CallSettings callSettings = null)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A pageable sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    ListRoutesRequest request = new ListRoutesRequest
    {
        ParentAsPrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListRoutesResponse, Route> response = datastreamClient.ListRoutes(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutes(PrivateConnectionName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRoutesResponse, Route> ListRoutes(PrivateConnectionName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The parent that owns the collection of Routess.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A pageable sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    PrivateConnectionName parent = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    // Make the request
    PagedEnumerable<ListRoutesResponse, Route> response = datastreamClient.ListRoutes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutes(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRoutesResponse, Route> ListRoutes(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of Routess.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A pageable sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    // Make the request
    PagedEnumerable<ListRoutesResponse, Route> response = datastreamClient.ListRoutes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Route item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRoutesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutesAsync(ListRoutesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRoutesResponse, Route> ListRoutesAsync(ListRoutesRequest request, CallSettings callSettings = null)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A pageable asynchronous sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ListRoutesRequest request = new ListRoutesRequest
    {
        ParentAsPrivateConnectionName = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListRoutesResponse, Route> response = datastreamClient.ListRoutesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Route item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListRoutesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutesAsync(PrivateConnectionName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRoutesResponse, Route> ListRoutesAsync(PrivateConnectionName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[PrivateConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectionName)`  
Required. The parent that owns the collection of Routess.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A pageable asynchronous sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    PrivateConnectionName parent = PrivateConnectionName.FromProjectLocationPrivateConnection("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
    // Make the request
    PagedAsyncEnumerable<ListRoutesResponse, Route> response = datastreamClient.ListRoutesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Route item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListRoutesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRoutesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRoutesResponse, Route> ListRoutesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of Routess.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | A pageable asynchronous sequence of [Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/privateConnections/[PRIVATE_CONNECTION]";
    // Make the request
    PagedAsyncEnumerable<ListRoutesResponse, Route> response = datastreamClient.ListRoutesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Route item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListRoutesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Route item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Route> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Route item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamObjects(ListStreamObjectsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListStreamObjectsResponse, StreamObject> ListStreamObjects(ListStreamObjectsRequest request, CallSettings callSettings = null)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamObjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A pageable sequence of [StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    ListStreamObjectsRequest request = new ListStreamObjectsRequest
    {
        ParentAsStreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
    };
    // Make the request
    PagedEnumerable<ListStreamObjectsResponse, StreamObject> response = datastreamClient.ListStreamObjects(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (StreamObject item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListStreamObjectsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (StreamObject item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<StreamObject> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (StreamObject item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamObjects(StreamName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListStreamObjectsResponse, StreamObject> ListStreamObjects(StreamName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)`  
Required. The parent stream that owns the collection of objects.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A pageable sequence of [StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    StreamName parent = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]");
    // Make the request
    PagedEnumerable<ListStreamObjectsResponse, StreamObject> response = datastreamClient.ListStreamObjects(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (StreamObject item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListStreamObjectsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (StreamObject item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<StreamObject> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (StreamObject item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamObjects(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListStreamObjectsResponse, StreamObject> ListStreamObjects(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent stream that owns the collection of objects.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A pageable sequence of [StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]";
    // Make the request
    PagedEnumerable<ListStreamObjectsResponse, StreamObject> response = datastreamClient.ListStreamObjects(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (StreamObject item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListStreamObjectsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (StreamObject item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<StreamObject> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (StreamObject item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamObjectsAsync(ListStreamObjectsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListStreamObjectsResponse, StreamObject> ListStreamObjectsAsync(ListStreamObjectsRequest request, CallSettings callSettings = null)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamObjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A pageable asynchronous sequence of [StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ListStreamObjectsRequest request = new ListStreamObjectsRequest
    {
        ParentAsStreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListStreamObjectsResponse, StreamObject> response = datastreamClient.ListStreamObjectsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((StreamObject item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListStreamObjectsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (StreamObject item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<StreamObject> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (StreamObject item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamObjectsAsync(StreamName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListStreamObjectsResponse, StreamObject> ListStreamObjectsAsync(StreamName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[StreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamName)`  
Required. The parent stream that owns the collection of objects.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A pageable asynchronous sequence of [StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamName parent = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]");
    // Make the request
    PagedAsyncEnumerable<ListStreamObjectsResponse, StreamObject> response = datastreamClient.ListStreamObjectsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((StreamObject item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListStreamObjectsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (StreamObject item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<StreamObject> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (StreamObject item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamObjectsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListStreamObjectsResponse, StreamObject> ListStreamObjectsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent stream that owns the collection of objects.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A pageable asynchronous sequence of [StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]";
    // Make the request
    PagedAsyncEnumerable<ListStreamObjectsResponse, StreamObject> response = datastreamClient.ListStreamObjectsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((StreamObject item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListStreamObjectsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (StreamObject item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<StreamObject> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (StreamObject item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreams(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListStreamsResponse, Stream> ListStreams(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of streams.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A pageable sequence of [Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListStreamsResponse, Stream> response = datastreamClient.ListStreams(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Stream item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListStreamsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Stream item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Stream> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Stream item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreams(ListStreamsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListStreamsResponse, Stream> ListStreams(ListStreamsRequest request, CallSettings callSettings = null)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A pageable sequence of [Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    ListStreamsRequest request = new ListStreamsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListStreamsResponse, Stream> response = datastreamClient.ListStreams(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Stream item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListStreamsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Stream item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Stream> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Stream item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreams(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListStreamsResponse, Stream> ListStreams(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of streams.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A pageable sequence of [Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListStreamsResponse, Stream> response = datastreamClient.ListStreams(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Stream item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListStreamsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Stream item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Stream> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Stream item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListStreamsResponse, Stream> ListStreamsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent that owns the collection of streams.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A pageable asynchronous sequence of [Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListStreamsResponse, Stream> response = datastreamClient.ListStreamsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Stream item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListStreamsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Stream item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Stream> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Stream item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamsAsync(ListStreamsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListStreamsResponse, Stream> ListStreamsAsync(ListStreamsRequest request, CallSettings callSettings = null)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A pageable asynchronous sequence of [Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ListStreamsRequest request = new ListStreamsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListStreamsResponse, Stream> response = datastreamClient.ListStreamsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Stream item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListStreamsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Stream item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Stream> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Stream item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListStreamsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListStreamsResponse, Stream> ListStreamsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent that owns the collection of streams.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | A pageable asynchronous sequence of [Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream) resources.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListStreamsResponse, Stream> response = datastreamClient.ListStreamsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Stream item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListStreamsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Stream item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Stream> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Stream item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### LookupStreamObject(LookupStreamObjectRequest, CallSettings)
    
    
    public virtual StreamObject LookupStreamObject(LookupStreamObjectRequest request, CallSettings callSettings = null)

Use this method to look up a stream object by its source object identifier.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.LookupStreamObjectRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    LookupStreamObjectRequest request = new LookupStreamObjectRequest
    {
        ParentAsStreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        SourceObjectIdentifier = new SourceObjectIdentifier(),
    };
    // Make the request
    StreamObject response = datastreamClient.LookupStreamObject(request);
    

### LookupStreamObjectAsync(LookupStreamObjectRequest, CallSettings)
    
    
    public virtual Task<StreamObject> LookupStreamObjectAsync(LookupStreamObjectRequest request, CallSettings callSettings = null)

Use this method to look up a stream object by its source object identifier.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.LookupStreamObjectRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LookupStreamObjectRequest request = new LookupStreamObjectRequest
    {
        ParentAsStreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        SourceObjectIdentifier = new SourceObjectIdentifier(),
    };
    // Make the request
    StreamObject response = await datastreamClient.LookupStreamObjectAsync(request);
    

### LookupStreamObjectAsync(LookupStreamObjectRequest, CancellationToken)
    
    
    public virtual Task<StreamObject> LookupStreamObjectAsync(LookupStreamObjectRequest request, CancellationToken cancellationToken)

Use this method to look up a stream object by its source object identifier.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.LookupStreamObjectRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    LookupStreamObjectRequest request = new LookupStreamObjectRequest
    {
        ParentAsStreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        SourceObjectIdentifier = new SourceObjectIdentifier(),
    };
    // Make the request
    StreamObject response = await datastreamClient.LookupStreamObjectAsync(request);
    

### PollOnceCreateConnectionProfile(string, CallSettings)
    
    
    public virtual Operation<ConnectionProfile, OperationMetadata> PollOnceCreateConnectionProfile(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateConnectionProfile`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateConnectionProfileAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> PollOnceCreateConnectionProfileAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateConnectionProfile`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreatePrivateConnection(string, CallSettings)
    
    
    public virtual Operation<PrivateConnection, OperationMetadata> PollOnceCreatePrivateConnection(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreatePrivateConnection`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreatePrivateConnectionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<PrivateConnection, OperationMetadata>> PollOnceCreatePrivateConnectionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreatePrivateConnection`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateRoute(string, CallSettings)
    
    
    public virtual Operation<Route, OperationMetadata> PollOnceCreateRoute(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateRoute`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateRouteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Route, OperationMetadata>> PollOnceCreateRouteAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateRoute`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateStream(string, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> PollOnceCreateStream(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateStream`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateStreamAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> PollOnceCreateStreamAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateStream`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteConnectionProfile(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteConnectionProfile(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteConnectionProfile`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteConnectionProfileAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteConnectionProfileAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteConnectionProfile`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeletePrivateConnection(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeletePrivateConnection(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeletePrivateConnection`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeletePrivateConnectionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeletePrivateConnectionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeletePrivateConnection`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteRoute(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteRoute(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteRoute`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteRouteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteRouteAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteRoute`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteStream(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteStream(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteStream`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteStreamAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteStreamAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteStream`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRunStream(string, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> PollOnceRunStream(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RunStream`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRunStreamAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> PollOnceRunStreamAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RunStream`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateConnectionProfile(string, CallSettings)
    
    
    public virtual Operation<ConnectionProfile, OperationMetadata> PollOnceUpdateConnectionProfile(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateConnectionProfile`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateConnectionProfileAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> PollOnceUpdateConnectionProfileAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateConnectionProfile`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateStream(string, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> PollOnceUpdateStream(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateStream`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateStreamAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> PollOnceUpdateStreamAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateStream`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### RunStream(RunStreamRequest, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> RunStream(RunStreamRequest request, CallSettings callSettings = null)

Use this method to start, resume or recover a stream with a non default CDC strategy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RunStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    RunStreamRequest request = new RunStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        CdcStrategy = new CdcStrategy(),
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = datastreamClient.RunStream(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = datastreamClient.PollOnceRunStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### RunStreamAsync(RunStreamRequest, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> RunStreamAsync(RunStreamRequest request, CallSettings callSettings = null)

Use this method to start, resume or recover a stream with a non default CDC strategy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RunStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    RunStreamRequest request = new RunStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        CdcStrategy = new CdcStrategy(),
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.RunStreamAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceRunStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### RunStreamAsync(RunStreamRequest, CancellationToken)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> RunStreamAsync(RunStreamRequest request, CancellationToken cancellationToken)

Use this method to start, resume or recover a stream with a non default CDC strategy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RunStreamRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    RunStreamRequest request = new RunStreamRequest
    {
        StreamName = StreamName.FromProjectLocationStream("[PROJECT]", "[LOCATION]", "[STREAM]"),
        CdcStrategy = new CdcStrategy(),
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.RunStreamAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceRunStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient#Google_Cloud_Datastream_V1_DatastreamClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient#Google_Cloud_Datastream_V1_DatastreamClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient#Google_Cloud_Datastream_V1_DatastreamClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DatastreamClient#Google_Cloud_Datastream_V1_DatastreamClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### StartBackfillJob(StartBackfillJobRequest, CallSettings)
    
    
    public virtual StartBackfillJobResponse StartBackfillJob(StartBackfillJobRequest request, CallSettings callSettings = null)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    StartBackfillJobRequest request = new StartBackfillJobRequest
    {
        ObjectAsStreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StartBackfillJobResponse response = datastreamClient.StartBackfillJob(request);
    

### StartBackfillJob(StreamObjectName, CallSettings)
    
    
    public virtual StartBackfillJobResponse StartBackfillJob(StreamObjectName @object, CallSettings callSettings = null)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to start a backfill job for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    StreamObjectName @object = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StartBackfillJobResponse response = datastreamClient.StartBackfillJob(@object);
    

### StartBackfillJob(string, CallSettings)
    
    
    public virtual StartBackfillJobResponse StartBackfillJob(string @object, CallSettings callSettings = null)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to start a backfill job for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string @object = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StartBackfillJobResponse response = datastreamClient.StartBackfillJob(@object);
    

### StartBackfillJobAsync(StartBackfillJobRequest, CallSettings)
    
    
    public virtual Task<StartBackfillJobResponse> StartBackfillJobAsync(StartBackfillJobRequest request, CallSettings callSettings = null)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StartBackfillJobRequest request = new StartBackfillJobRequest
    {
        ObjectAsStreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StartBackfillJobResponse response = await datastreamClient.StartBackfillJobAsync(request);
    

### StartBackfillJobAsync(StartBackfillJobRequest, CancellationToken)
    
    
    public virtual Task<StartBackfillJobResponse> StartBackfillJobAsync(StartBackfillJobRequest request, CancellationToken cancellationToken)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StartBackfillJobRequest request = new StartBackfillJobRequest
    {
        ObjectAsStreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StartBackfillJobResponse response = await datastreamClient.StartBackfillJobAsync(request);
    

### StartBackfillJobAsync(StreamObjectName, CallSettings)
    
    
    public virtual Task<StartBackfillJobResponse> StartBackfillJobAsync(StreamObjectName @object, CallSettings callSettings = null)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to start a backfill job for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamObjectName @object = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StartBackfillJobResponse response = await datastreamClient.StartBackfillJobAsync(@object);
    

### StartBackfillJobAsync(StreamObjectName, CancellationToken)
    
    
    public virtual Task<StartBackfillJobResponse> StartBackfillJobAsync(StreamObjectName @object, CancellationToken cancellationToken)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to start a backfill job for.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamObjectName @object = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StartBackfillJobResponse response = await datastreamClient.StartBackfillJobAsync(@object);
    

### StartBackfillJobAsync(string, CallSettings)
    
    
    public virtual Task<StartBackfillJobResponse> StartBackfillJobAsync(string @object, CallSettings callSettings = null)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to start a backfill job for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string @object = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StartBackfillJobResponse response = await datastreamClient.StartBackfillJobAsync(@object);
    

### StartBackfillJobAsync(string, CancellationToken)
    
    
    public virtual Task<StartBackfillJobResponse> StartBackfillJobAsync(string @object, CancellationToken cancellationToken)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to start a backfill job for.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string @object = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StartBackfillJobResponse response = await datastreamClient.StartBackfillJobAsync(@object);
    

### StopBackfillJob(StopBackfillJobRequest, CallSettings)
    
    
    public virtual StopBackfillJobResponse StopBackfillJob(StopBackfillJobRequest request, CallSettings callSettings = null)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    StopBackfillJobRequest request = new StopBackfillJobRequest
    {
        ObjectAsStreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StopBackfillJobResponse response = datastreamClient.StopBackfillJob(request);
    

### StopBackfillJob(StreamObjectName, CallSettings)
    
    
    public virtual StopBackfillJobResponse StopBackfillJob(StreamObjectName @object, CallSettings callSettings = null)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to stop the backfill job for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    StreamObjectName @object = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StopBackfillJobResponse response = datastreamClient.StopBackfillJob(@object);
    

### StopBackfillJob(string, CallSettings)
    
    
    public virtual StopBackfillJobResponse StopBackfillJob(string @object, CallSettings callSettings = null)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to stop the backfill job for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    string @object = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StopBackfillJobResponse response = datastreamClient.StopBackfillJob(@object);
    

### StopBackfillJobAsync(StopBackfillJobRequest, CallSettings)
    
    
    public virtual Task<StopBackfillJobResponse> StopBackfillJobAsync(StopBackfillJobRequest request, CallSettings callSettings = null)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StopBackfillJobRequest request = new StopBackfillJobRequest
    {
        ObjectAsStreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StopBackfillJobResponse response = await datastreamClient.StopBackfillJobAsync(request);
    

### StopBackfillJobAsync(StopBackfillJobRequest, CancellationToken)
    
    
    public virtual Task<StopBackfillJobResponse> StopBackfillJobAsync(StopBackfillJobRequest request, CancellationToken cancellationToken)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StopBackfillJobRequest request = new StopBackfillJobRequest
    {
        ObjectAsStreamObjectName = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]"),
    };
    // Make the request
    StopBackfillJobResponse response = await datastreamClient.StopBackfillJobAsync(request);
    

### StopBackfillJobAsync(StreamObjectName, CallSettings)
    
    
    public virtual Task<StopBackfillJobResponse> StopBackfillJobAsync(StreamObjectName @object, CallSettings callSettings = null)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to stop the backfill job for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamObjectName @object = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StopBackfillJobResponse response = await datastreamClient.StopBackfillJobAsync(@object);
    

### StopBackfillJobAsync(StreamObjectName, CancellationToken)
    
    
    public virtual Task<StopBackfillJobResponse> StopBackfillJobAsync(StreamObjectName @object, CancellationToken cancellationToken)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[StreamObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObjectName)`  
Required. The name of the stream object resource to stop the backfill job for.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    StreamObjectName @object = StreamObjectName.FromProjectLocationStreamObject("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
    // Make the request
    StopBackfillJobResponse response = await datastreamClient.StopBackfillJobAsync(@object);
    

### StopBackfillJobAsync(string, CallSettings)
    
    
    public virtual Task<StopBackfillJobResponse> StopBackfillJobAsync(string @object, CallSettings callSettings = null)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to stop the backfill job for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string @object = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StopBackfillJobResponse response = await datastreamClient.StopBackfillJobAsync(@object);
    

### StopBackfillJobAsync(string, CancellationToken)
    
    
    public virtual Task<StopBackfillJobResponse> StopBackfillJobAsync(string @object, CancellationToken cancellationToken)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`object` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the stream object resource to stop the backfill job for.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    string @object = "projects/[PROJECT]/locations/[LOCATION]/streams/[STREAM]/objects/[OBJECT]";
    // Make the request
    StopBackfillJobResponse response = await datastreamClient.StopBackfillJobAsync(@object);
    

### UpdateConnectionProfile(ConnectionProfile, FieldMask, CallSettings)
    
    
    public virtual Operation<ConnectionProfile, OperationMetadata> UpdateConnectionProfile(ConnectionProfile connectionProfile, FieldMask updateMask, CallSettings callSettings = null)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ConnectionProfile resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    ConnectionProfile connectionProfile = new ConnectionProfile();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = datastreamClient.UpdateConnectionProfile(connectionProfile, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = datastreamClient.PollOnceUpdateConnectionProfile(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectionProfile(UpdateConnectionProfileRequest, CallSettings)
    
    
    public virtual Operation<ConnectionProfile, OperationMetadata> UpdateConnectionProfile(UpdateConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    UpdateConnectionProfileRequest request = new UpdateConnectionProfileRequest
    {
        UpdateMask = new FieldMask(),
        ConnectionProfile = new ConnectionProfile(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = datastreamClient.UpdateConnectionProfile(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = datastreamClient.PollOnceUpdateConnectionProfile(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectionProfileAsync(ConnectionProfile, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> UpdateConnectionProfileAsync(ConnectionProfile connectionProfile, FieldMask updateMask, CallSettings callSettings = null)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ConnectionProfile resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ConnectionProfile connectionProfile = new ConnectionProfile();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.UpdateConnectionProfileAsync(connectionProfile, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceUpdateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectionProfileAsync(ConnectionProfile, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> UpdateConnectionProfileAsync(ConnectionProfile connectionProfile, FieldMask updateMask, CancellationToken cancellationToken)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
Required. The connection profile to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ConnectionProfile resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    ConnectionProfile connectionProfile = new ConnectionProfile();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.UpdateConnectionProfileAsync(connectionProfile, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceUpdateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectionProfileAsync(UpdateConnectionProfileRequest, CallSettings)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> UpdateConnectionProfileAsync(UpdateConnectionProfileRequest request, CallSettings callSettings = null)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    UpdateConnectionProfileRequest request = new UpdateConnectionProfileRequest
    {
        UpdateMask = new FieldMask(),
        ConnectionProfile = new ConnectionProfile(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.UpdateConnectionProfileAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceUpdateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConnectionProfileAsync(UpdateConnectionProfileRequest, CancellationToken)
    
    
    public virtual Task<Operation<ConnectionProfile, OperationMetadata>> UpdateConnectionProfileAsync(UpdateConnectionProfileRequest request, CancellationToken cancellationToken)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    UpdateConnectionProfileRequest request = new UpdateConnectionProfileRequest
    {
        UpdateMask = new FieldMask(),
        ConnectionProfile = new ConnectionProfile(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<ConnectionProfile, OperationMetadata> response = await datastreamClient.UpdateConnectionProfileAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ConnectionProfile, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ConnectionProfile result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ConnectionProfile, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceUpdateConnectionProfileAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ConnectionProfile retrievedResult = retrievedResponse.Result;
    }
    

### UpdateStream(Stream, FieldMask, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> UpdateStream(Stream stream, FieldMask updateMask, CallSettings callSettings = null)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the stream resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    Stream stream = new Stream();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Stream, OperationMetadata> response = datastreamClient.UpdateStream(stream, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = datastreamClient.PollOnceUpdateStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### UpdateStream(UpdateStreamRequest, CallSettings)
    
    
    public virtual Operation<Stream, OperationMetadata> UpdateStream(UpdateStreamRequest request, CallSettings callSettings = null)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = DatastreamClient.Create();
    // Initialize request argument(s)
    UpdateStreamRequest request = new UpdateStreamRequest
    {
        UpdateMask = new FieldMask(),
        Stream = new Stream(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = datastreamClient.UpdateStream(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = datastreamClient.PollOnceUpdateStream(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### UpdateStreamAsync(Stream, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> UpdateStreamAsync(Stream stream, FieldMask updateMask, CallSettings callSettings = null)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the stream resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    Stream stream = new Stream();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.UpdateStreamAsync(stream, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceUpdateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### UpdateStreamAsync(Stream, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> UpdateStreamAsync(Stream stream, FieldMask updateMask, CancellationToken cancellationToken)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)`  
Required. The stream resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the stream resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    Stream stream = new Stream();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.UpdateStreamAsync(stream, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceUpdateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### UpdateStreamAsync(UpdateStreamRequest, CallSettings)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> UpdateStreamAsync(UpdateStreamRequest request, CallSettings callSettings = null)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    UpdateStreamRequest request = new UpdateStreamRequest
    {
        UpdateMask = new FieldMask(),
        Stream = new Stream(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.UpdateStreamAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceUpdateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

### UpdateStreamAsync(UpdateStreamRequest, CancellationToken)
    
    
    public virtual Task<Operation<Stream, OperationMetadata>> UpdateStreamAsync(UpdateStreamRequest request, CancellationToken cancellationToken)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateStreamRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatastreamClient datastreamClient = await DatastreamClient.CreateAsync();
    // Initialize request argument(s)
    UpdateStreamRequest request = new UpdateStreamRequest
    {
        UpdateMask = new FieldMask(),
        Stream = new Stream(),
        RequestId = "",
        ValidateOnly = false,
        Force = false,
    };
    // Make the request
    Operation<Stream, OperationMetadata> response = await datastreamClient.UpdateStreamAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Stream, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Stream result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Stream, OperationMetadata> retrievedResponse = await datastreamClient.PollOnceUpdateStreamAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Stream retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
