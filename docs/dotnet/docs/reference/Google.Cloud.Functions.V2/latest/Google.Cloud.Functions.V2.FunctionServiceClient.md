---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient
title: Cloud Functions v2 API - Class FunctionServiceClient (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:44.290543+00:00
---

# Cloud Functions v2 API - Class FunctionServiceClient (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2 API - Class FunctionServiceClient (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.7.0/Google.Cloud.Functions.V2.FunctionServiceClient)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.6.0/Google.Cloud.Functions.V2.FunctionServiceClient)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.5.0/Google.Cloud.Functions.V2.FunctionServiceClient)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.4.0/Google.Cloud.Functions.V2.FunctionServiceClient)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.3.0/Google.Cloud.Functions.V2.FunctionServiceClient)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.2.0/Google.Cloud.Functions.V2.FunctionServiceClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.1.0/Google.Cloud.Functions.V2.FunctionServiceClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.0.0/Google.Cloud.Functions.V2.FunctionServiceClient)


    
    
    public abstract class FunctionServiceClient

Reference documentation and code samples for the Cloud Functions v2 API class FunctionServiceClient.

FunctionService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FunctionServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[FunctionServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClientImpl)

## Namespace

[Google.Cloud.Functions.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2)

## Assembly

Google.Cloud.Functions.V2.dll

## Remarks

Google Cloud Functions is used to deploy functions that are executed by Google in response to various events. Data connected with that event is passed to a function as the input data.

A **function** is a resource which describes a function that should be executed and how it is triggered.

## Properties 

### CreateFunctionOperationsClient
    
    
    public virtual OperationsClient CreateFunctionOperationsClient { get; }

The long-running operations client for `CreateFunction`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the FunctionService service, which is a host of "cloudfunctions.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default FunctionService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default FunctionService scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteFunctionOperationsClient
    
    
    public virtual OperationsClient DeleteFunctionOperationsClient { get; }

The long-running operations client for `DeleteFunction`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual FunctionService.FunctionServiceClient GrpcClient { get; }

The underlying gRPC FunctionService client

**Property Value**  
---  
**Type** | **Description**  
`[FunctionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionService)[FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionService.FunctionServiceClient)` |   
  
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
  
### UpdateFunctionOperationsClient
    
    
    public virtual OperationsClient UpdateFunctionOperationsClient { get; }

The long-running operations client for `UpdateFunction`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static FunctionServiceClient Create()

Synchronously creates a [FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [FunctionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient)` | The created [FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<FunctionServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [FunctionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient)` | The task representing the created [FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient).  
  
### CreateFunction(LocationName, Function, string, CallSettings)
    
    
    public virtual Operation<Function, OperationMetadata> CreateFunction(LocationName parent, Function function, string functionId, CallSettings callSettings = null)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location in which the function should be created, specified in the format `projects/*/locations/*`  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. Function to be created.  
`functionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The ID to use for the function, which will become the final component of the function's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcfv::Function function = new gcfv::Function();
    string functionId = "";
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = functionServiceClient.CreateFunction(parent, function, functionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = functionServiceClient.PollOnceCreateFunction(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### CreateFunction(CreateFunctionRequest, CallSettings)
    
    
    public virtual Operation<Function, OperationMetadata> CreateFunction(CreateFunctionRequest request, CallSettings callSettings = null)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.CreateFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::CreateFunctionRequest request = new gcfv::CreateFunctionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Function = new gcfv::Function(),
        FunctionId = "",
    };
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = functionServiceClient.CreateFunction(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = functionServiceClient.PollOnceCreateFunction(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### CreateFunction(string, Function, string, CallSettings)
    
    
    public virtual Operation<Function, OperationMetadata> CreateFunction(string parent, Function function, string functionId, CallSettings callSettings = null)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location in which the function should be created, specified in the format `projects/*/locations/*`  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. Function to be created.  
`functionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The ID to use for the function, which will become the final component of the function's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcfv::Function function = new gcfv::Function();
    string functionId = "";
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = functionServiceClient.CreateFunction(parent, function, functionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = functionServiceClient.PollOnceCreateFunction(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### CreateFunctionAsync(LocationName, Function, string, CallSettings)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> CreateFunctionAsync(LocationName parent, Function function, string functionId, CallSettings callSettings = null)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location in which the function should be created, specified in the format `projects/*/locations/*`  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. Function to be created.  
`functionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The ID to use for the function, which will become the final component of the function's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcfv::Function function = new gcfv::Function();
    string functionId = "";
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.CreateFunctionAsync(parent, function, functionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceCreateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### CreateFunctionAsync(LocationName, Function, string, CancellationToken)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> CreateFunctionAsync(LocationName parent, Function function, string functionId, CancellationToken cancellationToken)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location in which the function should be created, specified in the format `projects/*/locations/*`  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. Function to be created.  
`functionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The ID to use for the function, which will become the final component of the function's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcfv::Function function = new gcfv::Function();
    string functionId = "";
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.CreateFunctionAsync(parent, function, functionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceCreateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### CreateFunctionAsync(CreateFunctionRequest, CallSettings)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> CreateFunctionAsync(CreateFunctionRequest request, CallSettings callSettings = null)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.CreateFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::CreateFunctionRequest request = new gcfv::CreateFunctionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Function = new gcfv::Function(),
        FunctionId = "",
    };
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.CreateFunctionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceCreateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### CreateFunctionAsync(CreateFunctionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> CreateFunctionAsync(CreateFunctionRequest request, CancellationToken cancellationToken)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.CreateFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::CreateFunctionRequest request = new gcfv::CreateFunctionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Function = new gcfv::Function(),
        FunctionId = "",
    };
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.CreateFunctionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceCreateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### CreateFunctionAsync(string, Function, string, CallSettings)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> CreateFunctionAsync(string parent, Function function, string functionId, CallSettings callSettings = null)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location in which the function should be created, specified in the format `projects/*/locations/*`  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. Function to be created.  
`functionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The ID to use for the function, which will become the final component of the function's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcfv::Function function = new gcfv::Function();
    string functionId = "";
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.CreateFunctionAsync(parent, function, functionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceCreateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### CreateFunctionAsync(string, Function, string, CancellationToken)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> CreateFunctionAsync(string parent, Function function, string functionId, CancellationToken cancellationToken)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location in which the function should be created, specified in the format `projects/*/locations/*`  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. Function to be created.  
`functionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The ID to use for the function, which will become the final component of the function's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcfv::Function function = new gcfv::Function();
    string functionId = "";
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.CreateFunctionAsync(parent, function, functionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceCreateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunction(DeleteFunctionRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFunction(DeleteFunctionRequest request, CallSettings callSettings = null)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.DeleteFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::DeleteFunctionRequest request = new gcfv::DeleteFunctionRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
    };
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = functionServiceClient.DeleteFunction(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = functionServiceClient.PollOnceDeleteFunction(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunction(FunctionName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFunction(FunctionName name, CallSettings callSettings = null)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FunctionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionName)`  
Required. The name of the function which should be deleted.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::FunctionName name = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]");
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = functionServiceClient.DeleteFunction(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = functionServiceClient.PollOnceDeleteFunction(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunction(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteFunction(string name, CallSettings callSettings = null)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the function which should be deleted.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/functions/[FUNCTION]";
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = functionServiceClient.DeleteFunction(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = functionServiceClient.PollOnceDeleteFunction(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunctionAsync(DeleteFunctionRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFunctionAsync(DeleteFunctionRequest request, CallSettings callSettings = null)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.DeleteFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::DeleteFunctionRequest request = new gcfv::DeleteFunctionRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
    };
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = await functionServiceClient.DeleteFunctionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceDeleteFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunctionAsync(DeleteFunctionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFunctionAsync(DeleteFunctionRequest request, CancellationToken cancellationToken)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.DeleteFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::DeleteFunctionRequest request = new gcfv::DeleteFunctionRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
    };
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = await functionServiceClient.DeleteFunctionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceDeleteFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunctionAsync(FunctionName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFunctionAsync(FunctionName name, CallSettings callSettings = null)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FunctionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionName)`  
Required. The name of the function which should be deleted.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::FunctionName name = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]");
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = await functionServiceClient.DeleteFunctionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceDeleteFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunctionAsync(FunctionName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFunctionAsync(FunctionName name, CancellationToken cancellationToken)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FunctionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionName)`  
Required. The name of the function which should be deleted.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::FunctionName name = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]");
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = await functionServiceClient.DeleteFunctionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceDeleteFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunctionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFunctionAsync(string name, CallSettings callSettings = null)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the function which should be deleted.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/functions/[FUNCTION]";
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = await functionServiceClient.DeleteFunctionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceDeleteFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFunctionAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteFunctionAsync(string name, CancellationToken cancellationToken)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the function which should be deleted.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/functions/[FUNCTION]";
    // Make the request
    Operation<Empty, gcfv::OperationMetadata> response = await functionServiceClient.DeleteFunctionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceDeleteFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GenerateDownloadUrl(GenerateDownloadUrlRequest, CallSettings)
    
    
    public virtual GenerateDownloadUrlResponse GenerateDownloadUrl(GenerateDownloadUrlRequest request, CallSettings callSettings = null)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateDownloadUrlRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateDownloadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateDownloadUrlResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::GenerateDownloadUrlRequest request = new gcfv::GenerateDownloadUrlRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
    };
    // Make the request
    gcfv::GenerateDownloadUrlResponse response = functionServiceClient.GenerateDownloadUrl(request);
    

### GenerateDownloadUrlAsync(GenerateDownloadUrlRequest, CallSettings)
    
    
    public virtual Task<GenerateDownloadUrlResponse> GenerateDownloadUrlAsync(GenerateDownloadUrlRequest request, CallSettings callSettings = null)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateDownloadUrlRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateDownloadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateDownloadUrlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::GenerateDownloadUrlRequest request = new gcfv::GenerateDownloadUrlRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
    };
    // Make the request
    gcfv::GenerateDownloadUrlResponse response = await functionServiceClient.GenerateDownloadUrlAsync(request);
    

### GenerateDownloadUrlAsync(GenerateDownloadUrlRequest, CancellationToken)
    
    
    public virtual Task<GenerateDownloadUrlResponse> GenerateDownloadUrlAsync(GenerateDownloadUrlRequest request, CancellationToken cancellationToken)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateDownloadUrlRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateDownloadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateDownloadUrlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::GenerateDownloadUrlRequest request = new gcfv::GenerateDownloadUrlRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
    };
    // Make the request
    gcfv::GenerateDownloadUrlResponse response = await functionServiceClient.GenerateDownloadUrlAsync(request);
    

### GenerateUploadUrl(GenerateUploadUrlRequest, CallSettings)
    
    
    public virtual GenerateUploadUrlResponse GenerateUploadUrl(GenerateUploadUrlRequest request, CallSettings callSettings = null)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateUploadUrlRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateUploadUrlResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::GenerateUploadUrlRequest request = new gcfv::GenerateUploadUrlRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        KmsKeyNameAsCryptoKeyName = gcfv::CryptoKeyName.FromProjectLocationKeyRingCryptoKey("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]"),
        Environment = gcfv::Environment.Unspecified,
    };
    // Make the request
    gcfv::GenerateUploadUrlResponse response = functionServiceClient.GenerateUploadUrl(request);
    

### GenerateUploadUrlAsync(GenerateUploadUrlRequest, CallSettings)
    
    
    public virtual Task<GenerateUploadUrlResponse> GenerateUploadUrlAsync(GenerateUploadUrlRequest request, CallSettings callSettings = null)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateUploadUrlRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateUploadUrlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::GenerateUploadUrlRequest request = new gcfv::GenerateUploadUrlRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        KmsKeyNameAsCryptoKeyName = gcfv::CryptoKeyName.FromProjectLocationKeyRingCryptoKey("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]"),
        Environment = gcfv::Environment.Unspecified,
    };
    // Make the request
    gcfv::GenerateUploadUrlResponse response = await functionServiceClient.GenerateUploadUrlAsync(request);
    

### GenerateUploadUrlAsync(GenerateUploadUrlRequest, CancellationToken)
    
    
    public virtual Task<GenerateUploadUrlResponse> GenerateUploadUrlAsync(GenerateUploadUrlRequest request, CancellationToken cancellationToken)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateUploadUrlRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GenerateUploadUrlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::GenerateUploadUrlRequest request = new gcfv::GenerateUploadUrlRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        KmsKeyNameAsCryptoKeyName = gcfv::CryptoKeyName.FromProjectLocationKeyRingCryptoKey("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]"),
        Environment = gcfv::Environment.Unspecified,
    };
    // Make the request
    gcfv::GenerateUploadUrlResponse response = await functionServiceClient.GenerateUploadUrlAsync(request);
    

### GetFunction(FunctionName, CallSettings)
    
    
    public virtual Function GetFunction(FunctionName name, CallSettings callSettings = null)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FunctionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionName)`  
Required. The name of the function which details should be obtained.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::FunctionName name = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]");
    // Make the request
    gcfv::Function response = functionServiceClient.GetFunction(name);
    

### GetFunction(GetFunctionRequest, CallSettings)
    
    
    public virtual Function GetFunction(GetFunctionRequest request, CallSettings callSettings = null)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GetFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::GetFunctionRequest request = new gcfv::GetFunctionRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
        Revision = "",
    };
    // Make the request
    gcfv::Function response = functionServiceClient.GetFunction(request);
    

### GetFunction(string, CallSettings)
    
    
    public virtual Function GetFunction(string name, CallSettings callSettings = null)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the function which details should be obtained.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/functions/[FUNCTION]";
    // Make the request
    gcfv::Function response = functionServiceClient.GetFunction(name);
    

### GetFunctionAsync(FunctionName, CallSettings)
    
    
    public virtual Task<Function> GetFunctionAsync(FunctionName name, CallSettings callSettings = null)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FunctionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionName)`  
Required. The name of the function which details should be obtained.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::FunctionName name = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]");
    // Make the request
    gcfv::Function response = await functionServiceClient.GetFunctionAsync(name);
    

### GetFunctionAsync(FunctionName, CancellationToken)
    
    
    public virtual Task<Function> GetFunctionAsync(FunctionName name, CancellationToken cancellationToken)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FunctionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionName)`  
Required. The name of the function which details should be obtained.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::FunctionName name = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]");
    // Make the request
    gcfv::Function response = await functionServiceClient.GetFunctionAsync(name);
    

### GetFunctionAsync(GetFunctionRequest, CallSettings)
    
    
    public virtual Task<Function> GetFunctionAsync(GetFunctionRequest request, CallSettings callSettings = null)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GetFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::GetFunctionRequest request = new gcfv::GetFunctionRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
        Revision = "",
    };
    // Make the request
    gcfv::Function response = await functionServiceClient.GetFunctionAsync(request);
    

### GetFunctionAsync(GetFunctionRequest, CancellationToken)
    
    
    public virtual Task<Function> GetFunctionAsync(GetFunctionRequest request, CancellationToken cancellationToken)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.GetFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::GetFunctionRequest request = new gcfv::GetFunctionRequest
    {
        FunctionName = gcfv::FunctionName.FromProjectLocationFunction("[PROJECT]", "[LOCATION]", "[FUNCTION]"),
        Revision = "",
    };
    // Make the request
    gcfv::Function response = await functionServiceClient.GetFunctionAsync(request);
    

### GetFunctionAsync(string, CallSettings)
    
    
    public virtual Task<Function> GetFunctionAsync(string name, CallSettings callSettings = null)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the function which details should be obtained.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/functions/[FUNCTION]";
    // Make the request
    gcfv::Function response = await functionServiceClient.GetFunctionAsync(name);
    

### GetFunctionAsync(string, CancellationToken)
    
    
    public virtual Task<Function> GetFunctionAsync(string name, CancellationToken cancellationToken)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the function which details should be obtained.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/functions/[FUNCTION]";
    // Make the request
    gcfv::Function response = await functionServiceClient.GetFunctionAsync(name);
    

### ListFunctions(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFunctionsResponse, Function> ListFunctions(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location from which the function should be listed, specified in the format `projects/*/locations/*` If you want to list functions in all locations, use "-" in place of a location. When listing functions in all locations, if one or more location(s) are unreachable, the response will contain functions from all reachable locations along with the names of any unreachable locations.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsResponse)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A pageable sequence of [Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function) resources.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<gcfv::ListFunctionsResponse, gcfv::Function> response = functionServiceClient.ListFunctions(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcfv::Function item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcfv::ListFunctionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcfv::Function item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcfv::Function> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcfv::Function item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFunctions(ListFunctionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFunctionsResponse, Function> ListFunctions(ListFunctionsRequest request, CallSettings callSettings = null)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFunctionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsResponse)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A pageable sequence of [Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function) resources.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::ListFunctionsRequest request = new gcfv::ListFunctionsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<gcfv::ListFunctionsResponse, gcfv::Function> response = functionServiceClient.ListFunctions(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcfv::Function item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcfv::ListFunctionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcfv::Function item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcfv::Function> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcfv::Function item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFunctions(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFunctionsResponse, Function> ListFunctions(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location from which the function should be listed, specified in the format `projects/*/locations/*` If you want to list functions in all locations, use "-" in place of a location. When listing functions in all locations, if one or more location(s) are unreachable, the response will contain functions from all reachable locations along with the names of any unreachable locations.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsResponse)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A pageable sequence of [Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function) resources.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<gcfv::ListFunctionsResponse, gcfv::Function> response = functionServiceClient.ListFunctions(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcfv::Function item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcfv::ListFunctionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcfv::Function item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcfv::Function> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcfv::Function item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFunctionsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFunctionsResponse, Function> ListFunctionsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location from which the function should be listed, specified in the format `projects/*/locations/*` If you want to list functions in all locations, use "-" in place of a location. When listing functions in all locations, if one or more location(s) are unreachable, the response will contain functions from all reachable locations along with the names of any unreachable locations.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsResponse)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A pageable asynchronous sequence of [Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function) resources.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<gcfv::ListFunctionsResponse, gcfv::Function> response = functionServiceClient.ListFunctionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcfv::Function item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcfv::ListFunctionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcfv::Function item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcfv::Function> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcfv::Function item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFunctionsAsync(ListFunctionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFunctionsResponse, Function> ListFunctionsAsync(ListFunctionsRequest request, CallSettings callSettings = null)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFunctionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsResponse)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A pageable asynchronous sequence of [Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function) resources.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::ListFunctionsRequest request = new gcfv::ListFunctionsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcfv::ListFunctionsResponse, gcfv::Function> response = functionServiceClient.ListFunctionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcfv::Function item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcfv::ListFunctionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcfv::Function item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcfv::Function> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcfv::Function item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFunctionsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFunctionsResponse, Function> ListFunctionsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location from which the function should be listed, specified in the format `projects/*/locations/*` If you want to list functions in all locations, use "-" in place of a location. When listing functions in all locations, if one or more location(s) are unreachable, the response will contain functions from all reachable locations along with the names of any unreachable locations.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListFunctionsResponse)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)` | A pageable asynchronous sequence of [Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function) resources.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<gcfv::ListFunctionsResponse, gcfv::Function> response = functionServiceClient.ListFunctionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcfv::Function item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcfv::ListFunctionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcfv::Function item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcfv::Function> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcfv::Function item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRuntimes(LocationName, CallSettings)
    
    
    public virtual ListRuntimesResponse ListRuntimes(LocationName parent, CallSettings callSettings = null)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location from which the runtimes should be listed, specified in the format `projects/*/locations/*`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    gcfv::ListRuntimesResponse response = functionServiceClient.ListRuntimes(parent);
    

### ListRuntimes(ListRuntimesRequest, CallSettings)
    
    
    public virtual ListRuntimesResponse ListRuntimes(ListRuntimesRequest request, CallSettings callSettings = null)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuntimesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::ListRuntimesRequest request = new gcfv::ListRuntimesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    gcfv::ListRuntimesResponse response = functionServiceClient.ListRuntimes(request);
    

### ListRuntimes(string, CallSettings)
    
    
    public virtual ListRuntimesResponse ListRuntimes(string parent, CallSettings callSettings = null)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location from which the runtimes should be listed, specified in the format `projects/*/locations/*`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    gcfv::ListRuntimesResponse response = functionServiceClient.ListRuntimes(parent);
    

### ListRuntimesAsync(LocationName, CallSettings)
    
    
    public virtual Task<ListRuntimesResponse> ListRuntimesAsync(LocationName parent, CallSettings callSettings = null)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location from which the runtimes should be listed, specified in the format `projects/*/locations/*`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    gcfv::ListRuntimesResponse response = await functionServiceClient.ListRuntimesAsync(parent);
    

### ListRuntimesAsync(LocationName, CancellationToken)
    
    
    public virtual Task<ListRuntimesResponse> ListRuntimesAsync(LocationName parent, CancellationToken cancellationToken)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location from which the runtimes should be listed, specified in the format `projects/*/locations/*`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    gcfv::ListRuntimesResponse response = await functionServiceClient.ListRuntimesAsync(parent);
    

### ListRuntimesAsync(ListRuntimesRequest, CallSettings)
    
    
    public virtual Task<ListRuntimesResponse> ListRuntimesAsync(ListRuntimesRequest request, CallSettings callSettings = null)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuntimesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::ListRuntimesRequest request = new gcfv::ListRuntimesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    gcfv::ListRuntimesResponse response = await functionServiceClient.ListRuntimesAsync(request);
    

### ListRuntimesAsync(ListRuntimesRequest, CancellationToken)
    
    
    public virtual Task<ListRuntimesResponse> ListRuntimesAsync(ListRuntimesRequest request, CancellationToken cancellationToken)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuntimesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::ListRuntimesRequest request = new gcfv::ListRuntimesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    gcfv::ListRuntimesResponse response = await functionServiceClient.ListRuntimesAsync(request);
    

### ListRuntimesAsync(string, CallSettings)
    
    
    public virtual Task<ListRuntimesResponse> ListRuntimesAsync(string parent, CallSettings callSettings = null)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location from which the runtimes should be listed, specified in the format `projects/*/locations/*`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    gcfv::ListRuntimesResponse response = await functionServiceClient.ListRuntimesAsync(parent);
    

### ListRuntimesAsync(string, CancellationToken)
    
    
    public virtual Task<ListRuntimesResponse> ListRuntimesAsync(string parent, CancellationToken cancellationToken)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location from which the runtimes should be listed, specified in the format `projects/*/locations/*`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ListRuntimesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    gcfv::ListRuntimesResponse response = await functionServiceClient.ListRuntimesAsync(parent);
    

### PollOnceCreateFunction(string, CallSettings)
    
    
    public virtual Operation<Function, OperationMetadata> PollOnceCreateFunction(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFunction`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFunctionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> PollOnceCreateFunctionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFunction`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFunction(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteFunction(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFunction`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFunctionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteFunctionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFunction`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateFunction(string, CallSettings)
    
    
    public virtual Operation<Function, OperationMetadata> PollOnceUpdateFunction(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFunction`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFunctionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> PollOnceUpdateFunctionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFunction`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient#Google_Cloud_Functions_V2_FunctionServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient#Google_Cloud_Functions_V2_FunctionServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient#Google_Cloud_Functions_V2_FunctionServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.FunctionServiceClient#Google_Cloud_Functions_V2_FunctionServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateFunction(Function, FieldMask, CallSettings)
    
    
    public virtual Operation<Function, OperationMetadata> UpdateFunction(Function function, FieldMask updateMask, CallSettings callSettings = null)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. New version of the function.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If no field mask is provided, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::Function function = new gcfv::Function();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = functionServiceClient.UpdateFunction(function, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = functionServiceClient.PollOnceUpdateFunction(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFunction(UpdateFunctionRequest, CallSettings)
    
    
    public virtual Operation<Function, OperationMetadata> UpdateFunction(UpdateFunctionRequest request, CallSettings callSettings = null)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.UpdateFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = gcfv::FunctionServiceClient.Create();
    // Initialize request argument(s)
    gcfv::UpdateFunctionRequest request = new gcfv::UpdateFunctionRequest
    {
        Function = new gcfv::Function(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = functionServiceClient.UpdateFunction(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = functionServiceClient.PollOnceUpdateFunction(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFunctionAsync(Function, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> UpdateFunctionAsync(Function function, FieldMask updateMask, CallSettings callSettings = null)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. New version of the function.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If no field mask is provided, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::Function function = new gcfv::Function();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.UpdateFunctionAsync(function, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceUpdateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFunctionAsync(Function, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> UpdateFunctionAsync(Function function, FieldMask updateMask, CancellationToken cancellationToken)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`function` | `[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)`  
Required. New version of the function.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If no field mask is provided, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::Function function = new gcfv::Function();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.UpdateFunctionAsync(function, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceUpdateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFunctionAsync(UpdateFunctionRequest, CallSettings)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> UpdateFunctionAsync(UpdateFunctionRequest request, CallSettings callSettings = null)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.UpdateFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::UpdateFunctionRequest request = new gcfv::UpdateFunctionRequest
    {
        Function = new gcfv::Function(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.UpdateFunctionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceUpdateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFunctionAsync(UpdateFunctionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Function, OperationMetadata>> UpdateFunctionAsync(UpdateFunctionRequest request, CancellationToken cancellationToken)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.UpdateFunctionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.Function)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcfv::FunctionServiceClient functionServiceClient = await gcfv::FunctionServiceClient.CreateAsync();
    // Initialize request argument(s)
    gcfv::UpdateFunctionRequest request = new gcfv::UpdateFunctionRequest
    {
        Function = new gcfv::Function(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcfv::Function, gcfv::OperationMetadata> response = await functionServiceClient.UpdateFunctionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcfv::Function, gcfv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcfv::Function result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcfv::Function, gcfv::OperationMetadata> retrievedResponse = await functionServiceClient.PollOnceUpdateFunctionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcfv::Function retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
