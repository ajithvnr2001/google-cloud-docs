---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient
title: Vertex AI v1beta1 API - Class ReasoningEngineServiceClient (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:04.691387+00:00
---

# Vertex AI v1beta1 API - Class ReasoningEngineServiceClient (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ReasoningEngineServiceClient (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public abstract class ReasoningEngineServiceClient

Reference documentation and code samples for the Vertex AI v1beta1 API class ReasoningEngineServiceClient.

ReasoningEngineService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReasoningEngineServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ReasoningEngineServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Remarks

A service for managing Vertex AI's Reasoning Engines.

## Properties 

### CreateReasoningEngineOperationsClient
    
    
    public virtual OperationsClient CreateReasoningEngineOperationsClient { get; }

The long-running operations client for `CreateReasoningEngine`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ReasoningEngineService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ReasoningEngineService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ReasoningEngineService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteReasoningEngineOperationsClient
    
    
    public virtual OperationsClient DeleteReasoningEngineOperationsClient { get; }

The long-running operations client for `DeleteReasoningEngine`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ReasoningEngineService.ReasoningEngineServiceClient GrpcClient { get; }

The underlying gRPC ReasoningEngineService client

**Property Value**  
---  
**Type** | **Description**  
`[ReasoningEngineService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineService)[ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineService.ReasoningEngineServiceClient)` |   
  
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
  
### UpdateReasoningEngineOperationsClient
    
    
    public virtual OperationsClient UpdateReasoningEngineOperationsClient { get; }

The long-running operations client for `UpdateReasoningEngine`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static ReasoningEngineServiceClient Create()

Synchronously creates a [ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ReasoningEngineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient)` | The created [ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ReasoningEngineServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ReasoningEngineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient)` | The task representing the created [ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient).  
  
### CreateReasoningEngine(LocationName, ReasoningEngine, CallSettings)
    
    
    public virtual Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> CreateReasoningEngine(LocationName parent, ReasoningEngine reasoningEngine, CallSettings callSettings = null)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create the ReasoningEngine in. Format: `projects/{project}/locations/{location}`  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = reasoningEngineServiceClient.CreateReasoningEngine(parent, reasoningEngine);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = reasoningEngineServiceClient.PollOnceCreateReasoningEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### CreateReasoningEngine(CreateReasoningEngineRequest, CallSettings)
    
    
    public virtual Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> CreateReasoningEngine(CreateReasoningEngineRequest request, CallSettings callSettings = null)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    CreateReasoningEngineRequest request = new CreateReasoningEngineRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ReasoningEngine = new ReasoningEngine(),
    };
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = reasoningEngineServiceClient.CreateReasoningEngine(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = reasoningEngineServiceClient.PollOnceCreateReasoningEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### CreateReasoningEngine(string, ReasoningEngine, CallSettings)
    
    
    public virtual Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> CreateReasoningEngine(string parent, ReasoningEngine reasoningEngine, CallSettings callSettings = null)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create the ReasoningEngine in. Format: `projects/{project}/locations/{location}`  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = reasoningEngineServiceClient.CreateReasoningEngine(parent, reasoningEngine);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = reasoningEngineServiceClient.PollOnceCreateReasoningEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### CreateReasoningEngineAsync(LocationName, ReasoningEngine, CallSettings)
    
    
    public virtual Task<Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata>> CreateReasoningEngineAsync(LocationName parent, ReasoningEngine reasoningEngine, CallSettings callSettings = null)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create the ReasoningEngine in. Format: `projects/{project}/locations/{location}`  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.CreateReasoningEngineAsync(parent, reasoningEngine);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceCreateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### CreateReasoningEngineAsync(LocationName, ReasoningEngine, CancellationToken)
    
    
    public virtual Task<Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata>> CreateReasoningEngineAsync(LocationName parent, ReasoningEngine reasoningEngine, CancellationToken cancellationToken)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create the ReasoningEngine in. Format: `projects/{project}/locations/{location}`  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.CreateReasoningEngineAsync(parent, reasoningEngine);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceCreateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### CreateReasoningEngineAsync(CreateReasoningEngineRequest, CallSettings)
    
    
    public virtual Task<Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata>> CreateReasoningEngineAsync(CreateReasoningEngineRequest request, CallSettings callSettings = null)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateReasoningEngineRequest request = new CreateReasoningEngineRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ReasoningEngine = new ReasoningEngine(),
    };
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.CreateReasoningEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceCreateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### CreateReasoningEngineAsync(CreateReasoningEngineRequest, CancellationToken)
    
    
    public virtual Task<Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata>> CreateReasoningEngineAsync(CreateReasoningEngineRequest request, CancellationToken cancellationToken)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateReasoningEngineRequest request = new CreateReasoningEngineRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ReasoningEngine = new ReasoningEngine(),
    };
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.CreateReasoningEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceCreateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### CreateReasoningEngineAsync(string, ReasoningEngine, CallSettings)
    
    
    public virtual Task<Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata>> CreateReasoningEngineAsync(string parent, ReasoningEngine reasoningEngine, CallSettings callSettings = null)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create the ReasoningEngine in. Format: `projects/{project}/locations/{location}`  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.CreateReasoningEngineAsync(parent, reasoningEngine);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceCreateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### CreateReasoningEngineAsync(string, ReasoningEngine, CancellationToken)
    
    
    public virtual Task<Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata>> CreateReasoningEngineAsync(string parent, ReasoningEngine reasoningEngine, CancellationToken cancellationToken)

Creates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create the ReasoningEngine in. Format: `projects/{project}/locations/{location}`  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    // Make the request
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.CreateReasoningEngineAsync(parent, reasoningEngine);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceCreateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngine(DeleteReasoningEngineRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteReasoningEngine(DeleteReasoningEngineRequest request, CallSettings callSettings = null)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    DeleteReasoningEngineRequest request = new DeleteReasoningEngineRequest
    {
        ReasoningEngineName = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = reasoningEngineServiceClient.DeleteReasoningEngine(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = reasoningEngineServiceClient.PollOnceDeleteReasoningEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngine(ReasoningEngineName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteReasoningEngine(ReasoningEngineName name, CallSettings callSettings = null)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReasoningEngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineName)`  
Required. The name of the ReasoningEngine resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    ReasoningEngineName name = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = reasoningEngineServiceClient.DeleteReasoningEngine(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = reasoningEngineServiceClient.PollOnceDeleteReasoningEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngine(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteReasoningEngine(string name, CallSettings callSettings = null)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the ReasoningEngine resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reasoningEngines/[REASONING_ENGINE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = reasoningEngineServiceClient.DeleteReasoningEngine(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = reasoningEngineServiceClient.PollOnceDeleteReasoningEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngineAsync(DeleteReasoningEngineRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteReasoningEngineAsync(DeleteReasoningEngineRequest request, CallSettings callSettings = null)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteReasoningEngineRequest request = new DeleteReasoningEngineRequest
    {
        ReasoningEngineName = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await reasoningEngineServiceClient.DeleteReasoningEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceDeleteReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngineAsync(DeleteReasoningEngineRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteReasoningEngineAsync(DeleteReasoningEngineRequest request, CancellationToken cancellationToken)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteReasoningEngineRequest request = new DeleteReasoningEngineRequest
    {
        ReasoningEngineName = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await reasoningEngineServiceClient.DeleteReasoningEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceDeleteReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngineAsync(ReasoningEngineName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteReasoningEngineAsync(ReasoningEngineName name, CallSettings callSettings = null)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReasoningEngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineName)`  
Required. The name of the ReasoningEngine resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ReasoningEngineName name = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await reasoningEngineServiceClient.DeleteReasoningEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceDeleteReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngineAsync(ReasoningEngineName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteReasoningEngineAsync(ReasoningEngineName name, CancellationToken cancellationToken)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReasoningEngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineName)`  
Required. The name of the ReasoningEngine resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ReasoningEngineName name = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await reasoningEngineServiceClient.DeleteReasoningEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceDeleteReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteReasoningEngineAsync(string name, CallSettings callSettings = null)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the ReasoningEngine resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reasoningEngines/[REASONING_ENGINE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await reasoningEngineServiceClient.DeleteReasoningEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceDeleteReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReasoningEngineAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteReasoningEngineAsync(string name, CancellationToken cancellationToken)

Deletes a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the ReasoningEngine resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reasoningEngines/[REASONING_ENGINE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await reasoningEngineServiceClient.DeleteReasoningEngineAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceDeleteReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetReasoningEngine(GetReasoningEngineRequest, CallSettings)
    
    
    public virtual ReasoningEngine GetReasoningEngine(GetReasoningEngineRequest request, CallSettings callSettings = null)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    GetReasoningEngineRequest request = new GetReasoningEngineRequest
    {
        ReasoningEngineName = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]"),
    };
    // Make the request
    ReasoningEngine response = reasoningEngineServiceClient.GetReasoningEngine(request);
    

### GetReasoningEngine(ReasoningEngineName, CallSettings)
    
    
    public virtual ReasoningEngine GetReasoningEngine(ReasoningEngineName name, CallSettings callSettings = null)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReasoningEngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineName)`  
Required. The name of the ReasoningEngine resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    ReasoningEngineName name = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
    // Make the request
    ReasoningEngine response = reasoningEngineServiceClient.GetReasoningEngine(name);
    

### GetReasoningEngine(string, CallSettings)
    
    
    public virtual ReasoningEngine GetReasoningEngine(string name, CallSettings callSettings = null)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the ReasoningEngine resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reasoningEngines/[REASONING_ENGINE]";
    // Make the request
    ReasoningEngine response = reasoningEngineServiceClient.GetReasoningEngine(name);
    

### GetReasoningEngineAsync(GetReasoningEngineRequest, CallSettings)
    
    
    public virtual Task<ReasoningEngine> GetReasoningEngineAsync(GetReasoningEngineRequest request, CallSettings callSettings = null)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetReasoningEngineRequest request = new GetReasoningEngineRequest
    {
        ReasoningEngineName = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]"),
    };
    // Make the request
    ReasoningEngine response = await reasoningEngineServiceClient.GetReasoningEngineAsync(request);
    

### GetReasoningEngineAsync(GetReasoningEngineRequest, CancellationToken)
    
    
    public virtual Task<ReasoningEngine> GetReasoningEngineAsync(GetReasoningEngineRequest request, CancellationToken cancellationToken)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetReasoningEngineRequest request = new GetReasoningEngineRequest
    {
        ReasoningEngineName = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]"),
    };
    // Make the request
    ReasoningEngine response = await reasoningEngineServiceClient.GetReasoningEngineAsync(request);
    

### GetReasoningEngineAsync(ReasoningEngineName, CallSettings)
    
    
    public virtual Task<ReasoningEngine> GetReasoningEngineAsync(ReasoningEngineName name, CallSettings callSettings = null)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReasoningEngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineName)`  
Required. The name of the ReasoningEngine resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ReasoningEngineName name = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
    // Make the request
    ReasoningEngine response = await reasoningEngineServiceClient.GetReasoningEngineAsync(name);
    

### GetReasoningEngineAsync(ReasoningEngineName, CancellationToken)
    
    
    public virtual Task<ReasoningEngine> GetReasoningEngineAsync(ReasoningEngineName name, CancellationToken cancellationToken)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReasoningEngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineName)`  
Required. The name of the ReasoningEngine resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ReasoningEngineName name = ReasoningEngineName.FromProjectLocationReasoningEngine("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
    // Make the request
    ReasoningEngine response = await reasoningEngineServiceClient.GetReasoningEngineAsync(name);
    

### GetReasoningEngineAsync(string, CallSettings)
    
    
    public virtual Task<ReasoningEngine> GetReasoningEngineAsync(string name, CallSettings callSettings = null)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the ReasoningEngine resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reasoningEngines/[REASONING_ENGINE]";
    // Make the request
    ReasoningEngine response = await reasoningEngineServiceClient.GetReasoningEngineAsync(name);
    

### GetReasoningEngineAsync(string, CancellationToken)
    
    
    public virtual Task<ReasoningEngine> GetReasoningEngineAsync(string name, CancellationToken cancellationToken)

Gets a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the ReasoningEngine resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reasoningEngines/[REASONING_ENGINE]";
    // Make the request
    ReasoningEngine response = await reasoningEngineServiceClient.GetReasoningEngineAsync(name);
    

### ListReasoningEngines(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListReasoningEnginesResponse, ReasoningEngine> ListReasoningEngines(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists reasoning engines in a location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to list the ReasoningEngines from. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReasoningEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEnginesResponse)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A pageable sequence of [ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine) resources.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListReasoningEnginesResponse, ReasoningEngine> response = reasoningEngineServiceClient.ListReasoningEngines(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ReasoningEngine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReasoningEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReasoningEngine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReasoningEngine> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReasoningEngine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReasoningEngines(ListReasoningEnginesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListReasoningEnginesResponse, ReasoningEngine> ListReasoningEngines(ListReasoningEnginesRequest request, CallSettings callSettings = null)

Lists reasoning engines in a location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReasoningEnginesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEnginesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReasoningEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEnginesResponse)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A pageable sequence of [ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine) resources.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    ListReasoningEnginesRequest request = new ListReasoningEnginesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListReasoningEnginesResponse, ReasoningEngine> response = reasoningEngineServiceClient.ListReasoningEngines(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ReasoningEngine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReasoningEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReasoningEngine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReasoningEngine> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReasoningEngine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReasoningEngines(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListReasoningEnginesResponse, ReasoningEngine> ListReasoningEngines(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists reasoning engines in a location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list the ReasoningEngines from. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReasoningEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEnginesResponse)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A pageable sequence of [ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine) resources.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListReasoningEnginesResponse, ReasoningEngine> response = reasoningEngineServiceClient.ListReasoningEngines(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ReasoningEngine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReasoningEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReasoningEngine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReasoningEngine> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReasoningEngine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReasoningEnginesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReasoningEnginesResponse, ReasoningEngine> ListReasoningEnginesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists reasoning engines in a location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to list the ReasoningEngines from. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReasoningEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEnginesResponse)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A pageable asynchronous sequence of [ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine) resources.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListReasoningEnginesResponse, ReasoningEngine> response = reasoningEngineServiceClient.ListReasoningEnginesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ReasoningEngine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReasoningEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReasoningEngine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReasoningEngine> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReasoningEngine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReasoningEnginesAsync(ListReasoningEnginesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReasoningEnginesResponse, ReasoningEngine> ListReasoningEnginesAsync(ListReasoningEnginesRequest request, CallSettings callSettings = null)

Lists reasoning engines in a location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReasoningEnginesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEnginesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReasoningEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEnginesResponse)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A pageable asynchronous sequence of [ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine) resources.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListReasoningEnginesRequest request = new ListReasoningEnginesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListReasoningEnginesResponse, ReasoningEngine> response = reasoningEngineServiceClient.ListReasoningEnginesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ReasoningEngine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReasoningEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReasoningEngine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReasoningEngine> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReasoningEngine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReasoningEnginesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReasoningEnginesResponse, ReasoningEngine> ListReasoningEnginesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists reasoning engines in a location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list the ReasoningEngines from. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReasoningEnginesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListReasoningEnginesResponse)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)` | A pageable asynchronous sequence of [ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine) resources.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListReasoningEnginesResponse, ReasoningEngine> response = reasoningEngineServiceClient.ListReasoningEnginesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ReasoningEngine item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReasoningEnginesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReasoningEngine item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReasoningEngine> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReasoningEngine item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateReasoningEngine(string, CallSettings)
    
    
    public virtual Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata> PollOnceCreateReasoningEngine(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateReasoningEngine` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateReasoningEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ReasoningEngine, CreateReasoningEngineOperationMetadata>> PollOnceCreateReasoningEngineAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateReasoningEngine`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateReasoningEngineOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteReasoningEngine(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> PollOnceDeleteReasoningEngine(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteReasoningEngine` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteReasoningEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> PollOnceDeleteReasoningEngineAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteReasoningEngine`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateReasoningEngine(string, CallSettings)
    
    
    public virtual Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> PollOnceUpdateReasoningEngine(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateReasoningEngine` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineOperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateReasoningEngineAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata>> PollOnceUpdateReasoningEngineAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateReasoningEngine`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineOperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient#Google_Cloud_AIPlatform_V1Beta1_ReasoningEngineServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient#Google_Cloud_AIPlatform_V1Beta1_ReasoningEngineServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient#Google_Cloud_AIPlatform_V1Beta1_ReasoningEngineServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient#Google_Cloud_AIPlatform_V1Beta1_ReasoningEngineServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateReasoningEngine(ReasoningEngine, FieldMask, CallSettings)
    
    
    public virtual Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> UpdateReasoningEngine(ReasoningEngine reasoningEngine, FieldMask updateMask, CallSettings callSettings = null)

Updates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Mask specifying which fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> response = reasoningEngineServiceClient.UpdateReasoningEngine(reasoningEngine, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> retrievedResponse = reasoningEngineServiceClient.PollOnceUpdateReasoningEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### UpdateReasoningEngine(UpdateReasoningEngineRequest, CallSettings)
    
    
    public virtual Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> UpdateReasoningEngine(UpdateReasoningEngineRequest request, CallSettings callSettings = null)

Updates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = ReasoningEngineServiceClient.Create();
    // Initialize request argument(s)
    UpdateReasoningEngineRequest request = new UpdateReasoningEngineRequest
    {
        ReasoningEngine = new ReasoningEngine(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> response = reasoningEngineServiceClient.UpdateReasoningEngine(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> retrievedResponse = reasoningEngineServiceClient.PollOnceUpdateReasoningEngine(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### UpdateReasoningEngineAsync(ReasoningEngine, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata>> UpdateReasoningEngineAsync(ReasoningEngine reasoningEngine, FieldMask updateMask, CallSettings callSettings = null)

Updates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Mask specifying which fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.UpdateReasoningEngineAsync(reasoningEngine, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceUpdateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### UpdateReasoningEngineAsync(ReasoningEngine, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata>> UpdateReasoningEngineAsync(ReasoningEngine reasoningEngine, FieldMask updateMask, CancellationToken cancellationToken)

Updates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)`  
Required. The ReasoningEngine which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Mask specifying which fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    ReasoningEngine reasoningEngine = new ReasoningEngine();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.UpdateReasoningEngineAsync(reasoningEngine, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceUpdateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### UpdateReasoningEngineAsync(UpdateReasoningEngineRequest, CallSettings)
    
    
    public virtual Task<Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata>> UpdateReasoningEngineAsync(UpdateReasoningEngineRequest request, CallSettings callSettings = null)

Updates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateReasoningEngineRequest request = new UpdateReasoningEngineRequest
    {
        ReasoningEngine = new ReasoningEngine(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.UpdateReasoningEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceUpdateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

### UpdateReasoningEngineAsync(UpdateReasoningEngineRequest, CancellationToken)
    
    
    public virtual Task<Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata>> UpdateReasoningEngineAsync(UpdateReasoningEngineRequest request, CancellationToken cancellationToken)

Updates a reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReasoningEngineRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ReasoningEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngine)[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateReasoningEngineOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReasoningEngineServiceClient reasoningEngineServiceClient = await ReasoningEngineServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateReasoningEngineRequest request = new UpdateReasoningEngineRequest
    {
        ReasoningEngine = new ReasoningEngine(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> response = await reasoningEngineServiceClient.UpdateReasoningEngineAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ReasoningEngine result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ReasoningEngine, UpdateReasoningEngineOperationMetadata> retrievedResponse = await reasoningEngineServiceClient.PollOnceUpdateReasoningEngineAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ReasoningEngine retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
