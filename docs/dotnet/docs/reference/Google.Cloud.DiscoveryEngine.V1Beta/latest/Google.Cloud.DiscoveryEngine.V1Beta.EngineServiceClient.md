---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient
title: Discovery Engine v1beta API - Class EngineServiceClient (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:15.977499+00:00
---

# Discovery Engine v1beta API - Class EngineServiceClient (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class EngineServiceClient (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public abstract class EngineServiceClient

Reference documentation and code samples for the Discovery Engine v1beta API class EngineServiceClient.

EngineService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EngineServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[EngineServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClientImpl)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Remarks

Service for managing [Engine][google.cloud.discoveryengine.v1beta.Engine] configuration.

## Properties 

### CreateEngineOperationsClient
    
    
    public virtual OperationsClient CreateEngineOperationsClient { get; }

The long-running operations client for `CreateEngine`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the EngineService service, which is a host of "discoveryengine.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default EngineService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default EngineService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/discoveryengine.readwrite>
  * <https://www.googleapis.com/auth/discoveryengine.serving.readwrite>



### DeleteEngineOperationsClient
    
    
    public virtual OperationsClient DeleteEngineOperationsClient { get; }

The long-running operations client for `DeleteEngine`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual EngineService.EngineServiceClient GrpcClient { get; }

The underlying gRPC EngineService client

**Property Value**  
---  
**Type** | **Description**  
`[EngineService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineService)[EngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineService.EngineServiceClient)` |   
  
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
  
### TuneEngineOperationsClient
    
    
    public virtual OperationsClient TuneEngineOperationsClient { get; }

The long-running operations client for `TuneEngine`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static EngineServiceClient Create()

Synchronously creates a [EngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [EngineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[EngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient)` | The created [EngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<EngineServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [EngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [EngineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient)` | The task representing the created [EngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient).  
  
### CreateEngine(CollectionName, Engine, string, CallSettings)
    
    
    public virtual Operation<Engine, CreateEngineMetadata> CreateEngine(CollectionName parent, Engine engine, string engineId, CallSettings callSettings = null)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CollectionName)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to create.  
`engineId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Engine][google.cloud.discoveryengine.v1beta.Engine], which will become the final component of the [Engine][google.cloud.discoveryengine.v1beta.Engine]'s resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    CollectionName parent = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]");
    Engine engine = new Engine();
    string engineId = "";
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = engineServiceClient.CreateEngine(parent, engine, engineId);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = engineServiceClient.PollOnceCreateEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### CreateEngine(CreateEngineRequest, CallSettings)
    
    
    public virtual Operation<Engine, CreateEngineMetadata> CreateEngine(CreateEngineRequest request, CallSettings callSettings = null)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    CreateEngineRequest request = new CreateEngineRequest
    {
        ParentAsCollectionName = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
        Engine = new Engine(),
        EngineId = "",
    };
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = engineServiceClient.CreateEngine(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = engineServiceClient.PollOnceCreateEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### CreateEngine(string, Engine, string, CallSettings)
    
    
    public virtual Operation<Engine, CreateEngineMetadata> CreateEngine(string parent, Engine engine, string engineId, CallSettings callSettings = null)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to create.  
`engineId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Engine][google.cloud.discoveryengine.v1beta.Engine], which will become the final component of the [Engine][google.cloud.discoveryengine.v1beta.Engine]'s resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]";
    Engine engine = new Engine();
    string engineId = "";
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = engineServiceClient.CreateEngine(parent, engine, engineId);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = engineServiceClient.PollOnceCreateEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### CreateEngineAsync(CollectionName, Engine, string, CallSettings)
    
    
    public virtual Task<Operation<Engine, CreateEngineMetadata>> CreateEngineAsync(CollectionName parent, Engine engine, string engineId, CallSettings callSettings = null)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CollectionName)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to create.  
`engineId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Engine][google.cloud.discoveryengine.v1beta.Engine], which will become the final component of the [Engine][google.cloud.discoveryengine.v1beta.Engine]'s resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    CollectionName parent = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]");
    Engine engine = new Engine();
    string engineId = "";
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = await engineServiceClient.CreateEngineAsync(parent, engine, engineId);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceCreateEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### CreateEngineAsync(CollectionName, Engine, string, CancellationToken)
    
    
    public virtual Task<Operation<Engine, CreateEngineMetadata>> CreateEngineAsync(CollectionName parent, Engine engine, string engineId, CancellationToken cancellationToken)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CollectionName)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to create.  
`engineId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Engine][google.cloud.discoveryengine.v1beta.Engine], which will become the final component of the [Engine][google.cloud.discoveryengine.v1beta.Engine]'s resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    CollectionName parent = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]");
    Engine engine = new Engine();
    string engineId = "";
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = await engineServiceClient.CreateEngineAsync(parent, engine, engineId);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceCreateEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### CreateEngineAsync(CreateEngineRequest, CallSettings)
    
    
    public virtual Task<Operation<Engine, CreateEngineMetadata>> CreateEngineAsync(CreateEngineRequest request, CallSettings callSettings = null)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateEngineRequest request = new CreateEngineRequest
    {
        ParentAsCollectionName = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
        Engine = new Engine(),
        EngineId = "",
    };
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = await engineServiceClient.CreateEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceCreateEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### CreateEngineAsync(CreateEngineRequest, CancellationToken)
    
    
    public virtual Task<Operation<Engine, CreateEngineMetadata>> CreateEngineAsync(CreateEngineRequest request, CancellationToken cancellationToken)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateEngineRequest request = new CreateEngineRequest
    {
        ParentAsCollectionName = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
        Engine = new Engine(),
        EngineId = "",
    };
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = await engineServiceClient.CreateEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceCreateEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### CreateEngineAsync(string, Engine, string, CallSettings)
    
    
    public virtual Task<Operation<Engine, CreateEngineMetadata>> CreateEngineAsync(string parent, Engine engine, string engineId, CallSettings callSettings = null)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to create.  
`engineId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Engine][google.cloud.discoveryengine.v1beta.Engine], which will become the final component of the [Engine][google.cloud.discoveryengine.v1beta.Engine]'s resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]";
    Engine engine = new Engine();
    string engineId = "";
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = await engineServiceClient.CreateEngineAsync(parent, engine, engineId);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceCreateEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### CreateEngineAsync(string, Engine, string, CancellationToken)
    
    
    public virtual Task<Operation<Engine, CreateEngineMetadata>> CreateEngineAsync(string parent, Engine engine, string engineId, CancellationToken cancellationToken)

Creates an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to create.  
`engineId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Engine][google.cloud.discoveryengine.v1beta.Engine], which will become the final component of the [Engine][google.cloud.discoveryengine.v1beta.Engine]'s resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]";
    Engine engine = new Engine();
    string engineId = "";
    // Make the request
    Operation<Engine, CreateEngineMetadata> response = await engineServiceClient.CreateEngineAsync(parent, engine, engineId);
    
    // Poll until the returned long-running operation is complete
    Operation<Engine, CreateEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Engine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Engine, CreateEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceCreateEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Engine retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngine(DeleteEngineRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteEngineMetadata> DeleteEngine(DeleteEngineRequest request, CallSettings callSettings = null)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    DeleteEngineRequest request = new DeleteEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = engineServiceClient.DeleteEngine(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = engineServiceClient.PollOnceDeleteEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngine(EngineName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteEngineMetadata> DeleteEngine(EngineName name, CallSettings callSettings = null)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. If the caller does not have permission to delete the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to delete does not exist, a NOT_FOUND error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = engineServiceClient.DeleteEngine(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = engineServiceClient.PollOnceDeleteEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngine(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteEngineMetadata> DeleteEngine(string name, CallSettings callSettings = null)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. If the caller does not have permission to delete the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to delete does not exist, a NOT_FOUND error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = engineServiceClient.DeleteEngine(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = engineServiceClient.PollOnceDeleteEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngineAsync(DeleteEngineRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteEngineMetadata>> DeleteEngineAsync(DeleteEngineRequest request, CallSettings callSettings = null)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteEngineRequest request = new DeleteEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = await engineServiceClient.DeleteEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceDeleteEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngineAsync(DeleteEngineRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteEngineMetadata>> DeleteEngineAsync(DeleteEngineRequest request, CancellationToken cancellationToken)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteEngineRequest request = new DeleteEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = await engineServiceClient.DeleteEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceDeleteEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngineAsync(EngineName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteEngineMetadata>> DeleteEngineAsync(EngineName name, CallSettings callSettings = null)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. If the caller does not have permission to delete the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to delete does not exist, a NOT_FOUND error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = await engineServiceClient.DeleteEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceDeleteEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngineAsync(EngineName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteEngineMetadata>> DeleteEngineAsync(EngineName name, CancellationToken cancellationToken)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. If the caller does not have permission to delete the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to delete does not exist, a NOT_FOUND error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = await engineServiceClient.DeleteEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceDeleteEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteEngineMetadata>> DeleteEngineAsync(string name, CallSettings callSettings = null)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. If the caller does not have permission to delete the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to delete does not exist, a NOT_FOUND error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = await engineServiceClient.DeleteEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceDeleteEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEngineAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteEngineMetadata>> DeleteEngineAsync(string name, CancellationToken cancellationToken)

Deletes an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. If the caller does not have permission to delete the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to delete does not exist, a NOT_FOUND error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Operation<Empty, DeleteEngineMetadata> response = await engineServiceClient.DeleteEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceDeleteEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetEngine(EngineName, CallSettings)
    
    
    public virtual Engine GetEngine(EngineName name, CallSettings callSettings = null)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = engineServiceClient.GetEngine(name);
    

### GetEngine(GetEngineRequest, CallSettings)
    
    
    public virtual Engine GetEngine(GetEngineRequest request, CallSettings callSettings = null)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    GetEngineRequest request = new GetEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = engineServiceClient.GetEngine(request);
    

### GetEngine(string, CallSettings)
    
    
    public virtual Engine GetEngine(string name, CallSettings callSettings = null)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = engineServiceClient.GetEngine(name);
    

### GetEngineAsync(EngineName, CallSettings)
    
    
    public virtual Task<Engine> GetEngineAsync(EngineName name, CallSettings callSettings = null)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = await engineServiceClient.GetEngineAsync(name);
    

### GetEngineAsync(EngineName, CancellationToken)
    
    
    public virtual Task<Engine> GetEngineAsync(EngineName name, CancellationToken cancellationToken)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = await engineServiceClient.GetEngineAsync(name);
    

### GetEngineAsync(GetEngineRequest, CallSettings)
    
    
    public virtual Task<Engine> GetEngineAsync(GetEngineRequest request, CallSettings callSettings = null)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetEngineRequest request = new GetEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = await engineServiceClient.GetEngineAsync(request);
    

### GetEngineAsync(GetEngineRequest, CancellationToken)
    
    
    public virtual Task<Engine> GetEngineAsync(GetEngineRequest request, CancellationToken cancellationToken)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetEngineRequest request = new GetEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = await engineServiceClient.GetEngineAsync(request);
    

### GetEngineAsync(string, CallSettings)
    
    
    public virtual Task<Engine> GetEngineAsync(string name, CallSettings callSettings = null)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = await engineServiceClient.GetEngineAsync(name);
    

### GetEngineAsync(string, CancellationToken)
    
    
    public virtual Task<Engine> GetEngineAsync(string name, CancellationToken cancellationToken)

Gets an [Engine][google.cloud.discoveryengine.v1beta.Engine].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Engine][google.cloud.discoveryengine.v1beta.Engine], such as `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = await engineServiceClient.GetEngineAsync(name);
    

### GetIamPolicy(IResourceName, CallSettings)
    
    
    public virtual Policy GetIamPolicy(IResourceName resource, CallSettings callSettings = null)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = engineServiceClient.GetIamPolicy(resource);
    

### GetIamPolicy(GetIamPolicyRequest, CallSettings)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = engineServiceClient.GetIamPolicy(request);
    

### GetIamPolicy(string, CallSettings)
    
    
    public virtual Policy GetIamPolicy(string resource, CallSettings callSettings = null)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = engineServiceClient.GetIamPolicy(resource);
    

### GetIamPolicyAsync(IResourceName, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(IResourceName resource, CallSettings callSettings = null)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = await engineServiceClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(IResourceName, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(IResourceName resource, CancellationToken cancellationToken)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = await engineServiceClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(GetIamPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = await engineServiceClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(GetIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CancellationToken cancellationToken)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = await engineServiceClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(string resource, CallSettings callSettings = null)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = await engineServiceClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(string, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(string resource, CancellationToken cancellationToken)

Gets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist. An empty policy is returned if the resource exists but does not have a policy set on it.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = await engineServiceClient.GetIamPolicyAsync(resource);
    

### ListEngines(CollectionName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListEnginesResponse, Engine> ListEngines(CollectionName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all the [Engine][google.cloud.discoveryengine.v1beta.Engine]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CollectionName)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListEnginesResponse)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A pageable sequence of [Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine) resources.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    CollectionName parent = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]");
    // Make the request
    PagedEnumerable<ListEnginesResponse, Engine> response = engineServiceClient.ListEngines(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Engine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Engine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Engine> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Engine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEngines(ListEnginesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListEnginesResponse, Engine> ListEngines(ListEnginesRequest request, CallSettings callSettings = null)

Lists all the [Engine][google.cloud.discoveryengine.v1beta.Engine]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEnginesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListEnginesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListEnginesResponse)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A pageable sequence of [Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine) resources.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    ListEnginesRequest request = new ListEnginesRequest
    {
        ParentAsCollectionName = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListEnginesResponse, Engine> response = engineServiceClient.ListEngines(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Engine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Engine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Engine> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Engine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEngines(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListEnginesResponse, Engine> ListEngines(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all the [Engine][google.cloud.discoveryengine.v1beta.Engine]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListEnginesResponse)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A pageable sequence of [Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine) resources.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]";
    // Make the request
    PagedEnumerable<ListEnginesResponse, Engine> response = engineServiceClient.ListEngines(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Engine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Engine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Engine> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Engine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEnginesAsync(CollectionName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEnginesResponse, Engine> ListEnginesAsync(CollectionName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all the [Engine][google.cloud.discoveryengine.v1beta.Engine]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CollectionName)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListEnginesResponse)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A pageable asynchronous sequence of [Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine) resources.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    CollectionName parent = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]");
    // Make the request
    PagedAsyncEnumerable<ListEnginesResponse, Engine> response = engineServiceClient.ListEnginesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Engine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Engine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Engine> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Engine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEnginesAsync(ListEnginesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEnginesResponse, Engine> ListEnginesAsync(ListEnginesRequest request, CallSettings callSettings = null)

Lists all the [Engine][google.cloud.discoveryengine.v1beta.Engine]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEnginesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListEnginesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListEnginesResponse)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A pageable asynchronous sequence of [Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine) resources.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListEnginesRequest request = new ListEnginesRequest
    {
        ParentAsCollectionName = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListEnginesResponse, Engine> response = engineServiceClient.ListEnginesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Engine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Engine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Engine> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Engine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEnginesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEnginesResponse, Engine> ListEnginesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all the [Engine][google.cloud.discoveryengine.v1beta.Engine]s associated with the project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListEnginesResponse)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A pageable asynchronous sequence of [Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine) resources.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]";
    // Make the request
    PagedAsyncEnumerable<ListEnginesResponse, Engine> response = engineServiceClient.ListEnginesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Engine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Engine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Engine> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Engine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PauseEngine(EngineName, CallSettings)
    
    
    public virtual Engine PauseEngine(EngineName name, CallSettings callSettings = null)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The name of the engine to pause. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = engineServiceClient.PauseEngine(name);
    

### PauseEngine(PauseEngineRequest, CallSettings)
    
    
    public virtual Engine PauseEngine(PauseEngineRequest request, CallSettings callSettings = null)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PauseEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    PauseEngineRequest request = new PauseEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = engineServiceClient.PauseEngine(request);
    

### PauseEngine(string, CallSettings)
    
    
    public virtual Engine PauseEngine(string name, CallSettings callSettings = null)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the engine to pause. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = engineServiceClient.PauseEngine(name);
    

### PauseEngineAsync(EngineName, CallSettings)
    
    
    public virtual Task<Engine> PauseEngineAsync(EngineName name, CallSettings callSettings = null)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The name of the engine to pause. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = await engineServiceClient.PauseEngineAsync(name);
    

### PauseEngineAsync(EngineName, CancellationToken)
    
    
    public virtual Task<Engine> PauseEngineAsync(EngineName name, CancellationToken cancellationToken)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The name of the engine to pause. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = await engineServiceClient.PauseEngineAsync(name);
    

### PauseEngineAsync(PauseEngineRequest, CallSettings)
    
    
    public virtual Task<Engine> PauseEngineAsync(PauseEngineRequest request, CallSettings callSettings = null)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PauseEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    PauseEngineRequest request = new PauseEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = await engineServiceClient.PauseEngineAsync(request);
    

### PauseEngineAsync(PauseEngineRequest, CancellationToken)
    
    
    public virtual Task<Engine> PauseEngineAsync(PauseEngineRequest request, CancellationToken cancellationToken)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PauseEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    PauseEngineRequest request = new PauseEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = await engineServiceClient.PauseEngineAsync(request);
    

### PauseEngineAsync(string, CallSettings)
    
    
    public virtual Task<Engine> PauseEngineAsync(string name, CallSettings callSettings = null)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the engine to pause. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = await engineServiceClient.PauseEngineAsync(name);
    

### PauseEngineAsync(string, CancellationToken)
    
    
    public virtual Task<Engine> PauseEngineAsync(string name, CancellationToken cancellationToken)

Pauses the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the engine to pause. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = await engineServiceClient.PauseEngineAsync(name);
    

### PollOnceCreateEngine(string, CallSettings)
    
    
    public virtual Operation<Engine, CreateEngineMetadata> PollOnceCreateEngine(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateEngine`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | The result of polling the operation.  
  
### PollOnceCreateEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Engine, CreateEngineMetadata>> PollOnceCreateEngineAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateEngine`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)[CreateEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateEngineMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteEngine(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteEngineMetadata> PollOnceDeleteEngine(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteEngine`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteEngineMetadata>> PollOnceDeleteEngineAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteEngine`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteEngineMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceTuneEngine(string, CallSettings)
    
    
    public virtual Operation<TuneEngineResponse, TuneEngineMetadata> PollOnceTuneEngine(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `TuneEngine`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | The result of polling the operation.  
  
### PollOnceTuneEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<TuneEngineResponse, TuneEngineMetadata>> PollOnceTuneEngineAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `TuneEngine`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | A task representing the result of polling the operation.  
  
### ResumeEngine(EngineName, CallSettings)
    
    
    public virtual Engine ResumeEngine(EngineName name, CallSettings callSettings = null)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The name of the engine to resume. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = engineServiceClient.ResumeEngine(name);
    

### ResumeEngine(ResumeEngineRequest, CallSettings)
    
    
    public virtual Engine ResumeEngine(ResumeEngineRequest request, CallSettings callSettings = null)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ResumeEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    ResumeEngineRequest request = new ResumeEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = engineServiceClient.ResumeEngine(request);
    

### ResumeEngine(string, CallSettings)
    
    
    public virtual Engine ResumeEngine(string name, CallSettings callSettings = null)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the engine to resume. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = engineServiceClient.ResumeEngine(name);
    

### ResumeEngineAsync(EngineName, CallSettings)
    
    
    public virtual Task<Engine> ResumeEngineAsync(EngineName name, CallSettings callSettings = null)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The name of the engine to resume. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = await engineServiceClient.ResumeEngineAsync(name);
    

### ResumeEngineAsync(EngineName, CancellationToken)
    
    
    public virtual Task<Engine> ResumeEngineAsync(EngineName name, CancellationToken cancellationToken)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The name of the engine to resume. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Engine response = await engineServiceClient.ResumeEngineAsync(name);
    

### ResumeEngineAsync(ResumeEngineRequest, CallSettings)
    
    
    public virtual Task<Engine> ResumeEngineAsync(ResumeEngineRequest request, CallSettings callSettings = null)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ResumeEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ResumeEngineRequest request = new ResumeEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = await engineServiceClient.ResumeEngineAsync(request);
    

### ResumeEngineAsync(ResumeEngineRequest, CancellationToken)
    
    
    public virtual Task<Engine> ResumeEngineAsync(ResumeEngineRequest request, CancellationToken cancellationToken)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ResumeEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ResumeEngineRequest request = new ResumeEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Engine response = await engineServiceClient.ResumeEngineAsync(request);
    

### ResumeEngineAsync(string, CallSettings)
    
    
    public virtual Task<Engine> ResumeEngineAsync(string name, CallSettings callSettings = null)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the engine to resume. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = await engineServiceClient.ResumeEngineAsync(name);
    

### ResumeEngineAsync(string, CancellationToken)
    
    
    public virtual Task<Engine> ResumeEngineAsync(string name, CancellationToken cancellationToken)

Resumes the training of an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the engine to resume. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Engine response = await engineServiceClient.ResumeEngineAsync(name);
    

### SetIamPolicy(IResourceName, Policy, CallSettings)
    
    
    public virtual Policy SetIamPolicy(IResourceName resource, Policy policy, CallSettings callSettings = null)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = engineServiceClient.SetIamPolicy(resource, policy);
    

### SetIamPolicy(SetIamPolicyRequest, CallSettings)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRequest request, CallSettings callSettings = null)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = engineServiceClient.SetIamPolicy(request);
    

### SetIamPolicy(string, Policy, CallSettings)
    
    
    public virtual Policy SetIamPolicy(string resource, Policy policy, CallSettings callSettings = null)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = engineServiceClient.SetIamPolicy(resource, policy);
    

### SetIamPolicyAsync(IResourceName, Policy, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(IResourceName resource, Policy policy, CallSettings callSettings = null)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = await engineServiceClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(IResourceName, Policy, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(IResourceName resource, Policy policy, CancellationToken cancellationToken)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = await engineServiceClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(SetIamPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CallSettings callSettings = null)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = await engineServiceClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(SetIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CancellationToken cancellationToken)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = await engineServiceClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(string, Policy, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(string resource, Policy policy, CallSettings callSettings = null)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = await engineServiceClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(string, Policy, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(string resource, Policy policy, CancellationToken cancellationToken)

Sets the IAM access control policy for an [Engine][google.cloud.discoveryengine.v1beta.Engine]. A `NOT_FOUND` error is returned if the resource does not exist.

**Important:** When setting a policy directly on an Engine resource, the only recommended roles in the bindings are: `roles/discoveryengine.admin`, `roles/discoveryengine.agentspaceAdmin`, `roles/discoveryengine.user`, `roles/discoveryengine.agentspaceUser`, `roles/discoveryengine.viewer`, `roles/discoveryengine.agentspaceViewer`. Attempting to grant any other role will result in a warning in logging.

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
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = await engineServiceClient.SetIamPolicyAsync(resource, policy);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_EngineServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_EngineServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_EngineServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_EngineServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TuneEngine(EngineName, CallSettings)
    
    
    public virtual Operation<TuneEngineResponse, TuneEngineMetadata> TuneEngine(EngineName name, CallSettings callSettings = null)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The resource name of the engine to tune. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = engineServiceClient.TuneEngine(name);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = engineServiceClient.PollOnceTuneEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### TuneEngine(TuneEngineRequest, CallSettings)
    
    
    public virtual Operation<TuneEngineResponse, TuneEngineMetadata> TuneEngine(TuneEngineRequest request, CallSettings callSettings = null)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TuneEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    TuneEngineRequest request = new TuneEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = engineServiceClient.TuneEngine(request);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = engineServiceClient.PollOnceTuneEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### TuneEngine(string, CallSettings)
    
    
    public virtual Operation<TuneEngineResponse, TuneEngineMetadata> TuneEngine(string name, CallSettings callSettings = null)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the engine to tune. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = engineServiceClient.TuneEngine(name);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = engineServiceClient.PollOnceTuneEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### TuneEngineAsync(EngineName, CallSettings)
    
    
    public virtual Task<Operation<TuneEngineResponse, TuneEngineMetadata>> TuneEngineAsync(EngineName name, CallSettings callSettings = null)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The resource name of the engine to tune. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = await engineServiceClient.TuneEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceTuneEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### TuneEngineAsync(EngineName, CancellationToken)
    
    
    public virtual Task<Operation<TuneEngineResponse, TuneEngineMetadata>> TuneEngineAsync(EngineName name, CancellationToken cancellationToken)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.EngineName)`  
Required. The resource name of the engine to tune. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    EngineName name = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]");
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = await engineServiceClient.TuneEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceTuneEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### TuneEngineAsync(TuneEngineRequest, CallSettings)
    
    
    public virtual Task<Operation<TuneEngineResponse, TuneEngineMetadata>> TuneEngineAsync(TuneEngineRequest request, CallSettings callSettings = null)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TuneEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    TuneEngineRequest request = new TuneEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = await engineServiceClient.TuneEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceTuneEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### TuneEngineAsync(TuneEngineRequest, CancellationToken)
    
    
    public virtual Task<Operation<TuneEngineResponse, TuneEngineMetadata>> TuneEngineAsync(TuneEngineRequest request, CancellationToken cancellationToken)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TuneEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    TuneEngineRequest request = new TuneEngineRequest
    {
        EngineName = EngineName.FromProjectLocationCollectionEngine("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]"),
    };
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = await engineServiceClient.TuneEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceTuneEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### TuneEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<TuneEngineResponse, TuneEngineMetadata>> TuneEngineAsync(string name, CallSettings callSettings = null)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the engine to tune. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = await engineServiceClient.TuneEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceTuneEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### TuneEngineAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<TuneEngineResponse, TuneEngineMetadata>> TuneEngineAsync(string name, CancellationToken cancellationToken)

Tunes an existing [Engine][google.cloud.discoveryengine.v1beta.Engine]. Only applicable if [SolutionType][google.cloud.discoveryengine.v1beta.SolutionType] is [SOLUTION_TYPE_RECOMMENDATION][google.cloud.discoveryengine.v1beta.SolutionType.SOLUTION_TYPE_RECOMMENDATION].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the engine to tune. Format: `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TuneEngineResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineResponse)[TuneEngineMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.TuneEngineMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/collections/[COLLECTION]/engines/[ENGINE]";
    // Make the request
    Operation<TuneEngineResponse, TuneEngineMetadata> response = await engineServiceClient.TuneEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<TuneEngineResponse, TuneEngineMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    TuneEngineResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TuneEngineResponse, TuneEngineMetadata> retrievedResponse = await engineServiceClient.PollOnceTuneEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TuneEngineResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateEngine(Engine, FieldMask, CallSettings)
    
    
    public virtual Engine UpdateEngine(Engine engine, FieldMask updateMask, CallSettings callSettings = null)

Updates an [Engine][google.cloud.discoveryengine.v1beta.Engine]

**Parameters**  
---  
**Name** | **Description**  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to update. If the caller does not have permission to update the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Indicates which fields in the provided [Engine][google.cloud.discoveryengine.v1beta.Engine] to update. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    Engine engine = new Engine();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Engine response = engineServiceClient.UpdateEngine(engine, updateMask);
    

### UpdateEngine(UpdateEngineRequest, CallSettings)
    
    
    public virtual Engine UpdateEngine(UpdateEngineRequest request, CallSettings callSettings = null)

Updates an [Engine][google.cloud.discoveryengine.v1beta.Engine]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | The RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = EngineServiceClient.Create();
    // Initialize request argument(s)
    UpdateEngineRequest request = new UpdateEngineRequest
    {
        Engine = new Engine(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Engine response = engineServiceClient.UpdateEngine(request);
    

### UpdateEngineAsync(Engine, FieldMask, CallSettings)
    
    
    public virtual Task<Engine> UpdateEngineAsync(Engine engine, FieldMask updateMask, CallSettings callSettings = null)

Updates an [Engine][google.cloud.discoveryengine.v1beta.Engine]

**Parameters**  
---  
**Name** | **Description**  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to update. If the caller does not have permission to update the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Indicates which fields in the provided [Engine][google.cloud.discoveryengine.v1beta.Engine] to update. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    Engine engine = new Engine();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Engine response = await engineServiceClient.UpdateEngineAsync(engine, updateMask);
    

### UpdateEngineAsync(Engine, FieldMask, CancellationToken)
    
    
    public virtual Task<Engine> UpdateEngineAsync(Engine engine, FieldMask updateMask, CancellationToken cancellationToken)

Updates an [Engine][google.cloud.discoveryengine.v1beta.Engine]

**Parameters**  
---  
**Name** | **Description**  
`engine` | `[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)`  
Required. The [Engine][google.cloud.discoveryengine.v1beta.Engine] to update. If the caller does not have permission to update the [Engine][google.cloud.discoveryengine.v1beta.Engine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the [Engine][google.cloud.discoveryengine.v1beta.Engine] to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Indicates which fields in the provided [Engine][google.cloud.discoveryengine.v1beta.Engine] to update. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    Engine engine = new Engine();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Engine response = await engineServiceClient.UpdateEngineAsync(engine, updateMask);
    

### UpdateEngineAsync(UpdateEngineRequest, CallSettings)
    
    
    public virtual Task<Engine> UpdateEngineAsync(UpdateEngineRequest request, CallSettings callSettings = null)

Updates an [Engine][google.cloud.discoveryengine.v1beta.Engine]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateEngineRequest request = new UpdateEngineRequest
    {
        Engine = new Engine(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Engine response = await engineServiceClient.UpdateEngineAsync(request);
    

### UpdateEngineAsync(UpdateEngineRequest, CancellationToken)
    
    
    public virtual Task<Engine> UpdateEngineAsync(UpdateEngineRequest request, CancellationToken cancellationToken)

Updates an [Engine][google.cloud.discoveryengine.v1beta.Engine]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Engine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EngineServiceClient engineServiceClient = await EngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateEngineRequest request = new UpdateEngineRequest
    {
        Engine = new Engine(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Engine response = await engineServiceClient.UpdateEngineAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
