---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient
title: Vision AI v1 API - Class AppPlatformClient (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:20.973624+00:00
---

# Vision AI v1 API - Class AppPlatformClient (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class AppPlatformClient (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public abstract class AppPlatformClient

Reference documentation and code samples for the Vision AI v1 API class AppPlatformClient.

AppPlatform client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AppPlatformClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AppPlatformClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClientImpl)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Remarks

Service describing handlers for resources

## Properties 

### AddApplicationStreamInputOperationsClient
    
    
    public virtual OperationsClient AddApplicationStreamInputOperationsClient { get; }

The long-running operations client for `AddApplicationStreamInput`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateApplicationInstancesOperationsClient
    
    
    public virtual OperationsClient CreateApplicationInstancesOperationsClient { get; }

The long-running operations client for `CreateApplicationInstances`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateApplicationOperationsClient
    
    
    public virtual OperationsClient CreateApplicationOperationsClient { get; }

The long-running operations client for `CreateApplication`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateDraftOperationsClient
    
    
    public virtual OperationsClient CreateDraftOperationsClient { get; }

The long-running operations client for `CreateDraft`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateProcessorOperationsClient
    
    
    public virtual OperationsClient CreateProcessorOperationsClient { get; }

The long-running operations client for `CreateProcessor`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AppPlatform service, which is a host of "visionai.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AppPlatform scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AppPlatform scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteApplicationInstancesOperationsClient
    
    
    public virtual OperationsClient DeleteApplicationInstancesOperationsClient { get; }

The long-running operations client for `DeleteApplicationInstances`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteApplicationOperationsClient
    
    
    public virtual OperationsClient DeleteApplicationOperationsClient { get; }

The long-running operations client for `DeleteApplication`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteDraftOperationsClient
    
    
    public virtual OperationsClient DeleteDraftOperationsClient { get; }

The long-running operations client for `DeleteDraft`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteProcessorOperationsClient
    
    
    public virtual OperationsClient DeleteProcessorOperationsClient { get; }

The long-running operations client for `DeleteProcessor`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeployApplicationOperationsClient
    
    
    public virtual OperationsClient DeployApplicationOperationsClient { get; }

The long-running operations client for `DeployApplication`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual AppPlatform.AppPlatformClient GrpcClient { get; }

The underlying gRPC AppPlatform client

**Property Value**  
---  
**Type** | **Description**  
`[AppPlatform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatform)[AppPlatformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatform.AppPlatformClient)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### RemoveApplicationStreamInputOperationsClient
    
    
    public virtual OperationsClient RemoveApplicationStreamInputOperationsClient { get; }

The long-running operations client for `RemoveApplicationStreamInput`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
### UndeployApplicationOperationsClient
    
    
    public virtual OperationsClient UndeployApplicationOperationsClient { get; }

The long-running operations client for `UndeployApplication`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateApplicationInstancesOperationsClient
    
    
    public virtual OperationsClient UpdateApplicationInstancesOperationsClient { get; }

The long-running operations client for `UpdateApplicationInstances`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateApplicationOperationsClient
    
    
    public virtual OperationsClient UpdateApplicationOperationsClient { get; }

The long-running operations client for `UpdateApplication`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateApplicationStreamInputOperationsClient
    
    
    public virtual OperationsClient UpdateApplicationStreamInputOperationsClient { get; }

The long-running operations client for `UpdateApplicationStreamInput`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateDraftOperationsClient
    
    
    public virtual OperationsClient UpdateDraftOperationsClient { get; }

The long-running operations client for `UpdateDraft`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateProcessorOperationsClient
    
    
    public virtual OperationsClient UpdateProcessorOperationsClient { get; }

The long-running operations client for `UpdateProcessor`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### AddApplicationStreamInput(AddApplicationStreamInputRequest, CallSettings)
    
    
    public virtual Operation<AddApplicationStreamInputResponse, OperationMetadata> AddApplicationStreamInput(AddApplicationStreamInputRequest request, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    AddApplicationStreamInputRequest request = new AddApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationStreamInputs =
        {
            new ApplicationStreamInput(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.AddApplicationStreamInput(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceAddApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### AddApplicationStreamInput(ApplicationName, CallSettings)
    
    
    public virtual Operation<AddApplicationStreamInputResponse, OperationMetadata> AddApplicationStreamInput(ApplicationName name, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.AddApplicationStreamInput(name);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceAddApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### AddApplicationStreamInput(string, CallSettings)
    
    
    public virtual Operation<AddApplicationStreamInputResponse, OperationMetadata> AddApplicationStreamInput(string name, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.AddApplicationStreamInput(name);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceAddApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### AddApplicationStreamInputAsync(AddApplicationStreamInputRequest, CallSettings)
    
    
    public virtual Task<Operation<AddApplicationStreamInputResponse, OperationMetadata>> AddApplicationStreamInputAsync(AddApplicationStreamInputRequest request, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    AddApplicationStreamInputRequest request = new AddApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationStreamInputs =
        {
            new ApplicationStreamInput(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.AddApplicationStreamInputAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceAddApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### AddApplicationStreamInputAsync(AddApplicationStreamInputRequest, CancellationToken)
    
    
    public virtual Task<Operation<AddApplicationStreamInputResponse, OperationMetadata>> AddApplicationStreamInputAsync(AddApplicationStreamInputRequest request, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    AddApplicationStreamInputRequest request = new AddApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationStreamInputs =
        {
            new ApplicationStreamInput(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.AddApplicationStreamInputAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceAddApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### AddApplicationStreamInputAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<AddApplicationStreamInputResponse, OperationMetadata>> AddApplicationStreamInputAsync(ApplicationName name, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.AddApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceAddApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### AddApplicationStreamInputAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<AddApplicationStreamInputResponse, OperationMetadata>> AddApplicationStreamInputAsync(ApplicationName name, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.AddApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceAddApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### AddApplicationStreamInputAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AddApplicationStreamInputResponse, OperationMetadata>> AddApplicationStreamInputAsync(string name, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.AddApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceAddApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### AddApplicationStreamInputAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<AddApplicationStreamInputResponse, OperationMetadata>> AddApplicationStreamInputAsync(string name, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<AddApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.AddApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<AddApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    AddApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<AddApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceAddApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        AddApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static AppPlatformClient Create()

Synchronously creates a [AppPlatformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AppPlatformClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AppPlatformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient)` | The created [AppPlatformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient).  
  
### CreateApplication(LocationName, Application, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> CreateApplication(LocationName parent, Application application, CallSettings callSettings = null)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Application application = new Application();
    // Make the request
    Operation<Application, OperationMetadata> response = appPlatformClient.CreateApplication(parent, application);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplication(CreateApplicationRequest, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> CreateApplication(CreateApplicationRequest request, CallSettings callSettings = null)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    CreateApplicationRequest request = new CreateApplicationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApplicationId = "",
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = appPlatformClient.CreateApplication(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplication(string, Application, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> CreateApplication(string parent, Application application, CallSettings callSettings = null)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Application application = new Application();
    // Make the request
    Operation<Application, OperationMetadata> response = appPlatformClient.CreateApplication(parent, application);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(LocationName, Application, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(LocationName parent, Application application, CallSettings callSettings = null)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Application application = new Application();
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.CreateApplicationAsync(parent, application);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(LocationName, Application, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(LocationName parent, Application application, CancellationToken cancellationToken)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Application application = new Application();
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.CreateApplicationAsync(parent, application);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(CreateApplicationRequest, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(CreateApplicationRequest request, CallSettings callSettings = null)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    CreateApplicationRequest request = new CreateApplicationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApplicationId = "",
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.CreateApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(CreateApplicationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(CreateApplicationRequest request, CancellationToken cancellationToken)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    CreateApplicationRequest request = new CreateApplicationRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApplicationId = "",
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.CreateApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(string, Application, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(string parent, Application application, CallSettings callSettings = null)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Application application = new Application();
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.CreateApplicationAsync(parent, application);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationAsync(string, Application, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> CreateApplicationAsync(string parent, Application application, CancellationToken cancellationToken)

Creates a new Application in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Application application = new Application();
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.CreateApplicationAsync(parent, application);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstances(ApplicationName, CallSettings)
    
    
    public virtual Operation<CreateApplicationInstancesResponse, OperationMetadata> CreateApplicationInstances(ApplicationName name, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = appPlatformClient.CreateApplicationInstances(name);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstances(CreateApplicationInstancesRequest, CallSettings)
    
    
    public virtual Operation<CreateApplicationInstancesResponse, OperationMetadata> CreateApplicationInstances(CreateApplicationInstancesRequest request, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    CreateApplicationInstancesRequest request = new CreateApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationInstances =
        {
            new ApplicationInstance(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = appPlatformClient.CreateApplicationInstances(request);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstances(string, CallSettings)
    
    
    public virtual Operation<CreateApplicationInstancesResponse, OperationMetadata> CreateApplicationInstances(string name, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = appPlatformClient.CreateApplicationInstances(name);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstancesAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<CreateApplicationInstancesResponse, OperationMetadata>> CreateApplicationInstancesAsync(ApplicationName name, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.CreateApplicationInstancesAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstancesAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<CreateApplicationInstancesResponse, OperationMetadata>> CreateApplicationInstancesAsync(ApplicationName name, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.CreateApplicationInstancesAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstancesAsync(CreateApplicationInstancesRequest, CallSettings)
    
    
    public virtual Task<Operation<CreateApplicationInstancesResponse, OperationMetadata>> CreateApplicationInstancesAsync(CreateApplicationInstancesRequest request, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    CreateApplicationInstancesRequest request = new CreateApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationInstances =
        {
            new ApplicationInstance(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.CreateApplicationInstancesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstancesAsync(CreateApplicationInstancesRequest, CancellationToken)
    
    
    public virtual Task<Operation<CreateApplicationInstancesResponse, OperationMetadata>> CreateApplicationInstancesAsync(CreateApplicationInstancesRequest request, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    CreateApplicationInstancesRequest request = new CreateApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationInstances =
        {
            new ApplicationInstance(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.CreateApplicationInstancesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstancesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<CreateApplicationInstancesResponse, OperationMetadata>> CreateApplicationInstancesAsync(string name, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.CreateApplicationInstancesAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateApplicationInstancesAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<CreateApplicationInstancesResponse, OperationMetadata>> CreateApplicationInstancesAsync(string name, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<CreateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.CreateApplicationInstancesAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<CreateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    CreateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<CreateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        CreateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### CreateAsync(CancellationToken)
    
    
    public static Task<AppPlatformClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AppPlatformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AppPlatformClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppPlatformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient)` | The task representing the created [AppPlatformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient).  
  
### CreateDraft(ApplicationName, Draft, string, CallSettings)
    
    
    public virtual Operation<Draft, OperationMetadata> CreateDraft(ApplicationName parent, Draft draft, string draftId, CallSettings callSettings = null)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Value for parent.  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being created.  
`draftId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Draft draft = new Draft();
    string draftId = "";
    // Make the request
    Operation<Draft, OperationMetadata> response = appPlatformClient.CreateDraft(parent, draft, draftId);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateDraft(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateDraft(CreateDraftRequest, CallSettings)
    
    
    public virtual Operation<Draft, OperationMetadata> CreateDraft(CreateDraftRequest request, CallSettings callSettings = null)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateDraftRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    CreateDraftRequest request = new CreateDraftRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        DraftId = "",
        Draft = new Draft(),
        RequestId = "",
    };
    // Make the request
    Operation<Draft, OperationMetadata> response = appPlatformClient.CreateDraft(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateDraft(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateDraft(string, Draft, string, CallSettings)
    
    
    public virtual Operation<Draft, OperationMetadata> CreateDraft(string parent, Draft draft, string draftId, CallSettings callSettings = null)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being created.  
`draftId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Draft draft = new Draft();
    string draftId = "";
    // Make the request
    Operation<Draft, OperationMetadata> response = appPlatformClient.CreateDraft(parent, draft, draftId);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateDraft(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateDraftAsync(ApplicationName, Draft, string, CallSettings)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> CreateDraftAsync(ApplicationName parent, Draft draft, string draftId, CallSettings callSettings = null)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Value for parent.  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being created.  
`draftId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Draft draft = new Draft();
    string draftId = "";
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.CreateDraftAsync(parent, draft, draftId);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateDraftAsync(ApplicationName, Draft, string, CancellationToken)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> CreateDraftAsync(ApplicationName parent, Draft draft, string draftId, CancellationToken cancellationToken)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Value for parent.  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being created.  
`draftId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    Draft draft = new Draft();
    string draftId = "";
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.CreateDraftAsync(parent, draft, draftId);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateDraftAsync(CreateDraftRequest, CallSettings)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> CreateDraftAsync(CreateDraftRequest request, CallSettings callSettings = null)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateDraftRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    CreateDraftRequest request = new CreateDraftRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        DraftId = "",
        Draft = new Draft(),
        RequestId = "",
    };
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.CreateDraftAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateDraftAsync(CreateDraftRequest, CancellationToken)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> CreateDraftAsync(CreateDraftRequest request, CancellationToken cancellationToken)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateDraftRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    CreateDraftRequest request = new CreateDraftRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        DraftId = "",
        Draft = new Draft(),
        RequestId = "",
    };
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.CreateDraftAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateDraftAsync(string, Draft, string, CallSettings)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> CreateDraftAsync(string parent, Draft draft, string draftId, CallSettings callSettings = null)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being created.  
`draftId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Draft draft = new Draft();
    string draftId = "";
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.CreateDraftAsync(parent, draft, draftId);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateDraftAsync(string, Draft, string, CancellationToken)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> CreateDraftAsync(string parent, Draft draft, string draftId, CancellationToken cancellationToken)

Creates a new Draft in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being created.  
`draftId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    Draft draft = new Draft();
    string draftId = "";
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.CreateDraftAsync(parent, draft, draftId);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessor(LocationName, Processor, string, CallSettings)
    
    
    public virtual Operation<Processor, OperationMetadata> CreateProcessor(LocationName parent, Processor processor, string processorId, CallSettings callSettings = null)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being created.  
`processorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Processor processor = new Processor();
    string processorId = "";
    // Make the request
    Operation<Processor, OperationMetadata> response = appPlatformClient.CreateProcessor(parent, processor, processorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateProcessor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessor(CreateProcessorRequest, CallSettings)
    
    
    public virtual Operation<Processor, OperationMetadata> CreateProcessor(CreateProcessorRequest request, CallSettings callSettings = null)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    CreateProcessorRequest request = new CreateProcessorRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ProcessorId = "",
        Processor = new Processor(),
        RequestId = "",
    };
    // Make the request
    Operation<Processor, OperationMetadata> response = appPlatformClient.CreateProcessor(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateProcessor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessor(string, Processor, string, CallSettings)
    
    
    public virtual Operation<Processor, OperationMetadata> CreateProcessor(string parent, Processor processor, string processorId, CallSettings callSettings = null)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being created.  
`processorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Processor processor = new Processor();
    string processorId = "";
    // Make the request
    Operation<Processor, OperationMetadata> response = appPlatformClient.CreateProcessor(parent, processor, processorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceCreateProcessor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessorAsync(LocationName, Processor, string, CallSettings)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> CreateProcessorAsync(LocationName parent, Processor processor, string processorId, CallSettings callSettings = null)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being created.  
`processorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Processor processor = new Processor();
    string processorId = "";
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.CreateProcessorAsync(parent, processor, processorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessorAsync(LocationName, Processor, string, CancellationToken)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> CreateProcessorAsync(LocationName parent, Processor processor, string processorId, CancellationToken cancellationToken)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Value for parent.  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being created.  
`processorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Processor processor = new Processor();
    string processorId = "";
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.CreateProcessorAsync(parent, processor, processorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessorAsync(CreateProcessorRequest, CallSettings)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> CreateProcessorAsync(CreateProcessorRequest request, CallSettings callSettings = null)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    CreateProcessorRequest request = new CreateProcessorRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ProcessorId = "",
        Processor = new Processor(),
        RequestId = "",
    };
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.CreateProcessorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessorAsync(CreateProcessorRequest, CancellationToken)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> CreateProcessorAsync(CreateProcessorRequest request, CancellationToken cancellationToken)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    CreateProcessorRequest request = new CreateProcessorRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ProcessorId = "",
        Processor = new Processor(),
        RequestId = "",
    };
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.CreateProcessorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessorAsync(string, Processor, string, CallSettings)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> CreateProcessorAsync(string parent, Processor processor, string processorId, CallSettings callSettings = null)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being created.  
`processorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Processor processor = new Processor();
    string processorId = "";
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.CreateProcessorAsync(parent, processor, processorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### CreateProcessorAsync(string, Processor, string, CancellationToken)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> CreateProcessorAsync(string parent, Processor processor, string processorId, CancellationToken cancellationToken)

Creates a new Processor in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for parent.  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being created.  
`processorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Id of the requesting object.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Processor processor = new Processor();
    string processorId = "";
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.CreateProcessorAsync(parent, processor, processorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceCreateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplication(ApplicationName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApplication(ApplicationName name, CallSettings callSettings = null)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteApplication(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplication(DeleteApplicationRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApplication(DeleteApplicationRequest request, CallSettings callSettings = null)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    DeleteApplicationRequest request = new DeleteApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteApplication(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplication(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApplication(string name, CallSettings callSettings = null)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteApplication(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(ApplicationName name, CallSettings callSettings = null)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(ApplicationName name, CancellationToken cancellationToken)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(DeleteApplicationRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(DeleteApplicationRequest request, CallSettings callSettings = null)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeleteApplicationRequest request = new DeleteApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(DeleteApplicationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(DeleteApplicationRequest request, CancellationToken cancellationToken)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeleteApplicationRequest request = new DeleteApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(string name, CallSettings callSettings = null)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApplicationAsync(string name, CancellationToken cancellationToken)

Deletes a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstances(ApplicationName, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> DeleteApplicationInstances(ApplicationName name, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Instance, OperationMetadata> response = appPlatformClient.DeleteApplicationInstances(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstances(DeleteApplicationInstancesRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> DeleteApplicationInstances(DeleteApplicationInstancesRequest request, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    DeleteApplicationInstancesRequest request = new DeleteApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        InstanceIdsAsInstanceNames =
        {
            InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]"),
        },
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = appPlatformClient.DeleteApplicationInstances(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstances(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> DeleteApplicationInstances(string name, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Instance, OperationMetadata> response = appPlatformClient.DeleteApplicationInstances(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstancesAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> DeleteApplicationInstancesAsync(ApplicationName name, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Instance, OperationMetadata> response = await appPlatformClient.DeleteApplicationInstancesAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstancesAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> DeleteApplicationInstancesAsync(ApplicationName name, CancellationToken cancellationToken)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<Instance, OperationMetadata> response = await appPlatformClient.DeleteApplicationInstancesAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstancesAsync(DeleteApplicationInstancesRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> DeleteApplicationInstancesAsync(DeleteApplicationInstancesRequest request, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeleteApplicationInstancesRequest request = new DeleteApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        InstanceIdsAsInstanceNames =
        {
            InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]"),
        },
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await appPlatformClient.DeleteApplicationInstancesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstancesAsync(DeleteApplicationInstancesRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> DeleteApplicationInstancesAsync(DeleteApplicationInstancesRequest request, CancellationToken cancellationToken)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeleteApplicationInstancesRequest request = new DeleteApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        InstanceIdsAsInstanceNames =
        {
            InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]"),
        },
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await appPlatformClient.DeleteApplicationInstancesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstancesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> DeleteApplicationInstancesAsync(string name, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Instance, OperationMetadata> response = await appPlatformClient.DeleteApplicationInstancesAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApplicationInstancesAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> DeleteApplicationInstancesAsync(string name, CancellationToken cancellationToken)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<Instance, OperationMetadata> response = await appPlatformClient.DeleteApplicationInstancesAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraft(DeleteDraftRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDraft(DeleteDraftRequest request, CallSettings callSettings = null)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteDraftRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    DeleteDraftRequest request = new DeleteDraftRequest
    {
        DraftName = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteDraft(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteDraft(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraft(DraftName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDraft(DraftName name, CallSettings callSettings = null)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DraftName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DraftName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    DraftName name = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteDraft(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteDraft(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraft(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDraft(string name, CallSettings callSettings = null)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/drafts/[DRAFT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteDraft(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteDraft(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraftAsync(DeleteDraftRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDraftAsync(DeleteDraftRequest request, CallSettings callSettings = null)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteDraftRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDraftRequest request = new DeleteDraftRequest
    {
        DraftName = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteDraftAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraftAsync(DeleteDraftRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDraftAsync(DeleteDraftRequest request, CancellationToken cancellationToken)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteDraftRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDraftRequest request = new DeleteDraftRequest
    {
        DraftName = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteDraftAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraftAsync(DraftName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDraftAsync(DraftName name, CallSettings callSettings = null)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DraftName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DraftName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DraftName name = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteDraftAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraftAsync(DraftName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDraftAsync(DraftName name, CancellationToken cancellationToken)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DraftName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DraftName)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DraftName name = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteDraftAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraftAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDraftAsync(string name, CallSettings callSettings = null)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/drafts/[DRAFT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteDraftAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDraftAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDraftAsync(string name, CancellationToken cancellationToken)

Deletes a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/drafts/[DRAFT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteDraftAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessor(DeleteProcessorRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProcessor(DeleteProcessorRequest request, CallSettings callSettings = null)

Deletes a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    DeleteProcessorRequest request = new DeleteProcessorRequest
    {
        ProcessorName = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteProcessor(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteProcessor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessor(ProcessorName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProcessor(ProcessorName name, CallSettings callSettings = null)

Deletes a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ProcessorName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ProcessorName name = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteProcessor(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteProcessor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessor(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProcessor(string name, CallSettings callSettings = null)

Deletes a single Processor.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processors/[PROCESSOR]";
    // Make the request
    Operation<Empty, OperationMetadata> response = appPlatformClient.DeleteProcessor(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeleteProcessor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessorAsync(DeleteProcessorRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessorAsync(DeleteProcessorRequest request, CallSettings callSettings = null)

Deletes a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeleteProcessorRequest request = new DeleteProcessorRequest
    {
        ProcessorName = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteProcessorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessorAsync(DeleteProcessorRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessorAsync(DeleteProcessorRequest request, CancellationToken cancellationToken)

Deletes a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeleteProcessorRequest request = new DeleteProcessorRequest
    {
        ProcessorName = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteProcessorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessorAsync(ProcessorName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessorAsync(ProcessorName name, CallSettings callSettings = null)

Deletes a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ProcessorName)`  
Required. Name of the resource  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ProcessorName name = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteProcessorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessorAsync(ProcessorName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessorAsync(ProcessorName name, CancellationToken cancellationToken)

Deletes a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ProcessorName)`  
Required. Name of the resource  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ProcessorName name = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteProcessorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessorAsync(string name, CallSettings callSettings = null)

Deletes a single Processor.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processors/[PROCESSOR]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteProcessorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessorAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessorAsync(string name, CancellationToken cancellationToken)

Deletes a single Processor.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processors/[PROCESSOR]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await appPlatformClient.DeleteProcessorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeleteProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplication(ApplicationName, CallSettings)
    
    
    public virtual Operation<DeployApplicationResponse, OperationMetadata> DeployApplication(ApplicationName name, CallSettings callSettings = null)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = appPlatformClient.DeployApplication(name);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeployApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplication(DeployApplicationRequest, CallSettings)
    
    
    public virtual Operation<DeployApplicationResponse, OperationMetadata> DeployApplication(DeployApplicationRequest request, CallSettings callSettings = null)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    DeployApplicationRequest request = new DeployApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ValidateOnly = false,
        RequestId = "",
        EnableMonitoring = false,
    };
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = appPlatformClient.DeployApplication(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeployApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplication(string, CallSettings)
    
    
    public virtual Operation<DeployApplicationResponse, OperationMetadata> DeployApplication(string name, CallSettings callSettings = null)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = appPlatformClient.DeployApplication(name);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceDeployApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplicationAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<DeployApplicationResponse, OperationMetadata>> DeployApplicationAsync(ApplicationName name, CallSettings callSettings = null)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = await appPlatformClient.DeployApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplicationAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<DeployApplicationResponse, OperationMetadata>> DeployApplicationAsync(ApplicationName name, CancellationToken cancellationToken)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = await appPlatformClient.DeployApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplicationAsync(DeployApplicationRequest, CallSettings)
    
    
    public virtual Task<Operation<DeployApplicationResponse, OperationMetadata>> DeployApplicationAsync(DeployApplicationRequest request, CallSettings callSettings = null)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeployApplicationRequest request = new DeployApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ValidateOnly = false,
        RequestId = "",
        EnableMonitoring = false,
    };
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = await appPlatformClient.DeployApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplicationAsync(DeployApplicationRequest, CancellationToken)
    
    
    public virtual Task<Operation<DeployApplicationResponse, OperationMetadata>> DeployApplicationAsync(DeployApplicationRequest request, CancellationToken cancellationToken)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DeployApplicationRequest request = new DeployApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ValidateOnly = false,
        RequestId = "",
        EnableMonitoring = false,
    };
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = await appPlatformClient.DeployApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<DeployApplicationResponse, OperationMetadata>> DeployApplicationAsync(string name, CallSettings callSettings = null)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = await appPlatformClient.DeployApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployApplicationAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<DeployApplicationResponse, OperationMetadata>> DeployApplicationAsync(string name, CancellationToken cancellationToken)

Deploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<DeployApplicationResponse, OperationMetadata> response = await appPlatformClient.DeployApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<DeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceDeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### GetApplication(ApplicationName, CallSettings)
    
    
    public virtual Application GetApplication(ApplicationName name, CallSettings callSettings = null)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Application response = appPlatformClient.GetApplication(name);
    

### GetApplication(GetApplicationRequest, CallSettings)
    
    
    public virtual Application GetApplication(GetApplicationRequest request, CallSettings callSettings = null)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    GetApplicationRequest request = new GetApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
    };
    // Make the request
    Application response = appPlatformClient.GetApplication(request);
    

### GetApplication(string, CallSettings)
    
    
    public virtual Application GetApplication(string name, CallSettings callSettings = null)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Application response = appPlatformClient.GetApplication(name);
    

### GetApplicationAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Application> GetApplicationAsync(ApplicationName name, CallSettings callSettings = null)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Application response = await appPlatformClient.GetApplicationAsync(name);
    

### GetApplicationAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Application> GetApplicationAsync(ApplicationName name, CancellationToken cancellationToken)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Application response = await appPlatformClient.GetApplicationAsync(name);
    

### GetApplicationAsync(GetApplicationRequest, CallSettings)
    
    
    public virtual Task<Application> GetApplicationAsync(GetApplicationRequest request, CallSettings callSettings = null)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    GetApplicationRequest request = new GetApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
    };
    // Make the request
    Application response = await appPlatformClient.GetApplicationAsync(request);
    

### GetApplicationAsync(GetApplicationRequest, CancellationToken)
    
    
    public virtual Task<Application> GetApplicationAsync(GetApplicationRequest request, CancellationToken cancellationToken)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    GetApplicationRequest request = new GetApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
    };
    // Make the request
    Application response = await appPlatformClient.GetApplicationAsync(request);
    

### GetApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Application> GetApplicationAsync(string name, CallSettings callSettings = null)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Application response = await appPlatformClient.GetApplicationAsync(name);
    

### GetApplicationAsync(string, CancellationToken)
    
    
    public virtual Task<Application> GetApplicationAsync(string name, CancellationToken cancellationToken)

Gets details of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Application response = await appPlatformClient.GetApplicationAsync(name);
    

### GetDraft(DraftName, CallSettings)
    
    
    public virtual Draft GetDraft(DraftName name, CallSettings callSettings = null)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DraftName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DraftName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    DraftName name = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]");
    // Make the request
    Draft response = appPlatformClient.GetDraft(name);
    

### GetDraft(GetDraftRequest, CallSettings)
    
    
    public virtual Draft GetDraft(GetDraftRequest request, CallSettings callSettings = null)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetDraftRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    GetDraftRequest request = new GetDraftRequest
    {
        DraftName = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]"),
    };
    // Make the request
    Draft response = appPlatformClient.GetDraft(request);
    

### GetDraft(string, CallSettings)
    
    
    public virtual Draft GetDraft(string name, CallSettings callSettings = null)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/drafts/[DRAFT]";
    // Make the request
    Draft response = appPlatformClient.GetDraft(name);
    

### GetDraftAsync(DraftName, CallSettings)
    
    
    public virtual Task<Draft> GetDraftAsync(DraftName name, CallSettings callSettings = null)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DraftName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DraftName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DraftName name = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]");
    // Make the request
    Draft response = await appPlatformClient.GetDraftAsync(name);
    

### GetDraftAsync(DraftName, CancellationToken)
    
    
    public virtual Task<Draft> GetDraftAsync(DraftName name, CancellationToken cancellationToken)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DraftName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DraftName)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    DraftName name = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]");
    // Make the request
    Draft response = await appPlatformClient.GetDraftAsync(name);
    

### GetDraftAsync(GetDraftRequest, CallSettings)
    
    
    public virtual Task<Draft> GetDraftAsync(GetDraftRequest request, CallSettings callSettings = null)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetDraftRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    GetDraftRequest request = new GetDraftRequest
    {
        DraftName = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]"),
    };
    // Make the request
    Draft response = await appPlatformClient.GetDraftAsync(request);
    

### GetDraftAsync(GetDraftRequest, CancellationToken)
    
    
    public virtual Task<Draft> GetDraftAsync(GetDraftRequest request, CancellationToken cancellationToken)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetDraftRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    GetDraftRequest request = new GetDraftRequest
    {
        DraftName = DraftName.FromProjectLocationApplicationDraft("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[DRAFT]"),
    };
    // Make the request
    Draft response = await appPlatformClient.GetDraftAsync(request);
    

### GetDraftAsync(string, CallSettings)
    
    
    public virtual Task<Draft> GetDraftAsync(string name, CallSettings callSettings = null)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/drafts/[DRAFT]";
    // Make the request
    Draft response = await appPlatformClient.GetDraftAsync(name);
    

### GetDraftAsync(string, CancellationToken)
    
    
    public virtual Task<Draft> GetDraftAsync(string name, CancellationToken cancellationToken)

Gets details of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/drafts/[DRAFT]";
    // Make the request
    Draft response = await appPlatformClient.GetDraftAsync(name);
    

### GetInstance(GetInstanceRequest, CallSettings)
    
    
    public virtual Instance GetInstance(GetInstanceRequest request, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = appPlatformClient.GetInstance(request);
    

### GetInstance(InstanceName, CallSettings)
    
    
    public virtual Instance GetInstance(InstanceName name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.InstanceName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]");
    // Make the request
    Instance response = appPlatformClient.GetInstance(name);
    

### GetInstance(string, CallSettings)
    
    
    public virtual Instance GetInstance(string name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = appPlatformClient.GetInstance(name);
    

### GetInstanceAsync(GetInstanceRequest, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(GetInstanceRequest request, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = await appPlatformClient.GetInstanceAsync(request);
    

### GetInstanceAsync(GetInstanceRequest, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(GetInstanceRequest request, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = await appPlatformClient.GetInstanceAsync(request);
    

### GetInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(InstanceName name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.InstanceName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]");
    // Make the request
    Instance response = await appPlatformClient.GetInstanceAsync(name);
    

### GetInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.InstanceName)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationApplicationInstance("[PROJECT]", "[LOCATION]", "[APPLICATION]", "[INSTANCE]");
    // Make the request
    Instance response = await appPlatformClient.GetInstanceAsync(name);
    

### GetInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(string name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = await appPlatformClient.GetInstanceAsync(name);
    

### GetInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(string name, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = await appPlatformClient.GetInstanceAsync(name);
    

### GetProcessor(GetProcessorRequest, CallSettings)
    
    
    public virtual Processor GetProcessor(GetProcessorRequest request, CallSettings callSettings = null)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    GetProcessorRequest request = new GetProcessorRequest
    {
        ProcessorName = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
    };
    // Make the request
    Processor response = appPlatformClient.GetProcessor(request);
    

### GetProcessor(ProcessorName, CallSettings)
    
    
    public virtual Processor GetProcessor(ProcessorName name, CallSettings callSettings = null)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ProcessorName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ProcessorName name = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
    // Make the request
    Processor response = appPlatformClient.GetProcessor(name);
    

### GetProcessor(string, CallSettings)
    
    
    public virtual Processor GetProcessor(string name, CallSettings callSettings = null)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processors/[PROCESSOR]";
    // Make the request
    Processor response = appPlatformClient.GetProcessor(name);
    

### GetProcessorAsync(GetProcessorRequest, CallSettings)
    
    
    public virtual Task<Processor> GetProcessorAsync(GetProcessorRequest request, CallSettings callSettings = null)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    GetProcessorRequest request = new GetProcessorRequest
    {
        ProcessorName = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
    };
    // Make the request
    Processor response = await appPlatformClient.GetProcessorAsync(request);
    

### GetProcessorAsync(GetProcessorRequest, CancellationToken)
    
    
    public virtual Task<Processor> GetProcessorAsync(GetProcessorRequest request, CancellationToken cancellationToken)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    GetProcessorRequest request = new GetProcessorRequest
    {
        ProcessorName = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]"),
    };
    // Make the request
    Processor response = await appPlatformClient.GetProcessorAsync(request);
    

### GetProcessorAsync(ProcessorName, CallSettings)
    
    
    public virtual Task<Processor> GetProcessorAsync(ProcessorName name, CallSettings callSettings = null)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ProcessorName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ProcessorName name = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
    // Make the request
    Processor response = await appPlatformClient.GetProcessorAsync(name);
    

### GetProcessorAsync(ProcessorName, CancellationToken)
    
    
    public virtual Task<Processor> GetProcessorAsync(ProcessorName name, CancellationToken cancellationToken)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ProcessorName)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ProcessorName name = ProcessorName.FromProjectLocationProcessor("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
    // Make the request
    Processor response = await appPlatformClient.GetProcessorAsync(name);
    

### GetProcessorAsync(string, CallSettings)
    
    
    public virtual Task<Processor> GetProcessorAsync(string name, CallSettings callSettings = null)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processors/[PROCESSOR]";
    // Make the request
    Processor response = await appPlatformClient.GetProcessorAsync(name);
    

### GetProcessorAsync(string, CancellationToken)
    
    
    public virtual Task<Processor> GetProcessorAsync(string name, CancellationToken cancellationToken)

Gets details of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processors/[PROCESSOR]";
    // Make the request
    Processor response = await appPlatformClient.GetProcessorAsync(name);
    

### ListApplications(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListApplicationsResponse, Application> ListApplications(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Applications in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListApplicationsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A pageable sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListApplicationsResponse, Application> response = appPlatformClient.ListApplications(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplications(ListApplicationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListApplicationsResponse, Application> ListApplications(ListApplicationsRequest request, CallSettings callSettings = null)

Lists Applications in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListApplicationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A pageable sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ListApplicationsRequest request = new ListApplicationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListApplicationsResponse, Application> response = appPlatformClient.ListApplications(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplications(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListApplicationsResponse, Application> ListApplications(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Applications in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListApplicationsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A pageable sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListApplicationsResponse, Application> response = appPlatformClient.ListApplications(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplicationsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListApplicationsResponse, Application> ListApplicationsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Applications in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListApplicationsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A pageable asynchronous sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListApplicationsResponse, Application> response = appPlatformClient.ListApplicationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplicationsAsync(ListApplicationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListApplicationsResponse, Application> ListApplicationsAsync(ListApplicationsRequest request, CallSettings callSettings = null)

Lists Applications in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListApplicationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A pageable asynchronous sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ListApplicationsRequest request = new ListApplicationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListApplicationsResponse, Application> response = appPlatformClient.ListApplicationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApplicationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListApplicationsResponse, Application> ListApplicationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Applications in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListApplicationsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListApplicationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListApplicationsResponse)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)` | A pageable asynchronous sequence of [Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListApplicationsResponse, Application> response = appPlatformClient.ListApplicationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Application item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListApplicationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Application item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Application> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Application item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDrafts(ApplicationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDraftsResponse, Draft> ListDrafts(ApplicationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Drafts in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Parent value for ListDraftsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDraftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDraftsResponse)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A pageable sequence of [Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    PagedEnumerable<ListDraftsResponse, Draft> response = appPlatformClient.ListDrafts(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Draft item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDraftsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Draft item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Draft> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Draft item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDrafts(ListDraftsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDraftsResponse, Draft> ListDrafts(ListDraftsRequest request, CallSettings callSettings = null)

Lists Drafts in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDraftsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDraftsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDraftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDraftsResponse)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A pageable sequence of [Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ListDraftsRequest request = new ListDraftsRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListDraftsResponse, Draft> response = appPlatformClient.ListDrafts(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Draft item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDraftsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Draft item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Draft> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Draft item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDrafts(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDraftsResponse, Draft> ListDrafts(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Drafts in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListDraftsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDraftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDraftsResponse)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A pageable sequence of [Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    PagedEnumerable<ListDraftsResponse, Draft> response = appPlatformClient.ListDrafts(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Draft item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDraftsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Draft item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Draft> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Draft item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDraftsAsync(ApplicationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDraftsResponse, Draft> ListDraftsAsync(ApplicationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Drafts in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Parent value for ListDraftsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDraftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDraftsResponse)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A pageable asynchronous sequence of [Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    PagedAsyncEnumerable<ListDraftsResponse, Draft> response = appPlatformClient.ListDraftsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Draft item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDraftsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Draft item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Draft> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Draft item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDraftsAsync(ListDraftsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDraftsResponse, Draft> ListDraftsAsync(ListDraftsRequest request, CallSettings callSettings = null)

Lists Drafts in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDraftsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDraftsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDraftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDraftsResponse)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A pageable asynchronous sequence of [Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ListDraftsRequest request = new ListDraftsRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListDraftsResponse, Draft> response = appPlatformClient.ListDraftsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Draft item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDraftsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Draft item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Draft> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Draft item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDraftsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDraftsResponse, Draft> ListDraftsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Drafts in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListDraftsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDraftsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDraftsResponse)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)` | A pageable asynchronous sequence of [Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    PagedAsyncEnumerable<ListDraftsResponse, Draft> response = appPlatformClient.ListDraftsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Draft item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDraftsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Draft item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Draft> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Draft item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstances(ApplicationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListInstancesResponse, Instance> ListInstances(ApplicationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Parent value for ListInstancesRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = appPlatformClient.ListInstances(parent);
    
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
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ListInstancesRequest request = new ListInstancesRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = appPlatformClient.ListInstances(request);
    
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
Required. Parent value for ListInstancesRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = appPlatformClient.ListInstances(parent);
    
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
    

### ListInstancesAsync(ApplicationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInstancesResponse, Instance> ListInstancesAsync(ApplicationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. Parent value for ListInstancesRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName parent = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = appPlatformClient.ListInstancesAsync(parent);
    
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
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ListInstancesRequest request = new ListInstancesRequest
    {
        ParentAsApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = appPlatformClient.ListInstancesAsync(request);
    
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
Required. Parent value for ListInstancesRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = appPlatformClient.ListInstancesAsync(parent);
    
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
    

### ListPrebuiltProcessors(LocationName, CallSettings)
    
    
    public virtual ListPrebuiltProcessorsResponse ListPrebuiltProcessors(LocationName parent, CallSettings callSettings = null)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent path.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    ListPrebuiltProcessorsResponse response = appPlatformClient.ListPrebuiltProcessors(parent);
    

### ListPrebuiltProcessors(ListPrebuiltProcessorsRequest, CallSettings)
    
    
    public virtual ListPrebuiltProcessorsResponse ListPrebuiltProcessors(ListPrebuiltProcessorsRequest request, CallSettings callSettings = null)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrebuiltProcessorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ListPrebuiltProcessorsRequest request = new ListPrebuiltProcessorsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    ListPrebuiltProcessorsResponse response = appPlatformClient.ListPrebuiltProcessors(request);
    

### ListPrebuiltProcessors(string, CallSettings)
    
    
    public virtual ListPrebuiltProcessorsResponse ListPrebuiltProcessors(string parent, CallSettings callSettings = null)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent path.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    ListPrebuiltProcessorsResponse response = appPlatformClient.ListPrebuiltProcessors(parent);
    

### ListPrebuiltProcessorsAsync(LocationName, CallSettings)
    
    
    public virtual Task<ListPrebuiltProcessorsResponse> ListPrebuiltProcessorsAsync(LocationName parent, CallSettings callSettings = null)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent path.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    ListPrebuiltProcessorsResponse response = await appPlatformClient.ListPrebuiltProcessorsAsync(parent);
    

### ListPrebuiltProcessorsAsync(LocationName, CancellationToken)
    
    
    public virtual Task<ListPrebuiltProcessorsResponse> ListPrebuiltProcessorsAsync(LocationName parent, CancellationToken cancellationToken)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent path.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    ListPrebuiltProcessorsResponse response = await appPlatformClient.ListPrebuiltProcessorsAsync(parent);
    

### ListPrebuiltProcessorsAsync(ListPrebuiltProcessorsRequest, CallSettings)
    
    
    public virtual Task<ListPrebuiltProcessorsResponse> ListPrebuiltProcessorsAsync(ListPrebuiltProcessorsRequest request, CallSettings callSettings = null)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrebuiltProcessorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ListPrebuiltProcessorsRequest request = new ListPrebuiltProcessorsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    ListPrebuiltProcessorsResponse response = await appPlatformClient.ListPrebuiltProcessorsAsync(request);
    

### ListPrebuiltProcessorsAsync(ListPrebuiltProcessorsRequest, CancellationToken)
    
    
    public virtual Task<ListPrebuiltProcessorsResponse> ListPrebuiltProcessorsAsync(ListPrebuiltProcessorsRequest request, CancellationToken cancellationToken)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrebuiltProcessorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ListPrebuiltProcessorsRequest request = new ListPrebuiltProcessorsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    ListPrebuiltProcessorsResponse response = await appPlatformClient.ListPrebuiltProcessorsAsync(request);
    

### ListPrebuiltProcessorsAsync(string, CallSettings)
    
    
    public virtual Task<ListPrebuiltProcessorsResponse> ListPrebuiltProcessorsAsync(string parent, CallSettings callSettings = null)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent path.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    ListPrebuiltProcessorsResponse response = await appPlatformClient.ListPrebuiltProcessorsAsync(parent);
    

### ListPrebuiltProcessorsAsync(string, CancellationToken)
    
    
    public virtual Task<ListPrebuiltProcessorsResponse> ListPrebuiltProcessorsAsync(string parent, CancellationToken cancellationToken)

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent path.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPrebuiltProcessorsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    ListPrebuiltProcessorsResponse response = await appPlatformClient.ListPrebuiltProcessorsAsync(parent);
    

### ListProcessors(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListProcessorsResponse, Processor> ListProcessors(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Processors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListProcessorsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessorsResponse)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A pageable sequence of [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListProcessorsResponse, Processor> response = appPlatformClient.ListProcessors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Processor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListProcessorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Processor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Processor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Processor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcessors(ListProcessorsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListProcessorsResponse, Processor> ListProcessors(ListProcessorsRequest request, CallSettings callSettings = null)

Lists Processors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessorsResponse)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A pageable sequence of [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ListProcessorsRequest request = new ListProcessorsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListProcessorsResponse, Processor> response = appPlatformClient.ListProcessors(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Processor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListProcessorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Processor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Processor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Processor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcessors(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListProcessorsResponse, Processor> ListProcessors(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Processors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListProcessorsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessorsResponse)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A pageable sequence of [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListProcessorsResponse, Processor> response = appPlatformClient.ListProcessors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Processor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListProcessorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Processor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Processor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Processor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcessorsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListProcessorsResponse, Processor> ListProcessorsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Processors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Parent value for ListProcessorsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessorsResponse)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A pageable asynchronous sequence of [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListProcessorsResponse, Processor> response = appPlatformClient.ListProcessorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Processor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListProcessorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Processor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Processor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Processor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcessorsAsync(ListProcessorsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListProcessorsResponse, Processor> ListProcessorsAsync(ListProcessorsRequest request, CallSettings callSettings = null)

Lists Processors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessorsResponse)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A pageable asynchronous sequence of [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ListProcessorsRequest request = new ListProcessorsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListProcessorsResponse, Processor> response = appPlatformClient.ListProcessorsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Processor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListProcessorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Processor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Processor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Processor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcessorsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListProcessorsResponse, Processor> ListProcessorsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Processors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent value for ListProcessorsRequest.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListProcessorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessorsResponse)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)` | A pageable asynchronous sequence of [Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor) resources.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListProcessorsResponse, Processor> response = appPlatformClient.ListProcessorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Processor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListProcessorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Processor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Processor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Processor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceAddApplicationStreamInput(string, CallSettings)
    
    
    public virtual Operation<AddApplicationStreamInputResponse, OperationMetadata> PollOnceAddApplicationStreamInput(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `AddApplicationStreamInput`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceAddApplicationStreamInputAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AddApplicationStreamInputResponse, OperationMetadata>> PollOnceAddApplicationStreamInputAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `AddApplicationStreamInput`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AddApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateApplication(string, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> PollOnceCreateApplication(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateApplication` .

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> PollOnceCreateApplicationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateApplication`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateApplicationInstances(string, CallSettings)
    
    
    public virtual Operation<CreateApplicationInstancesResponse, OperationMetadata> PollOnceCreateApplicationInstances(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateApplicationInstances`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateApplicationInstancesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<CreateApplicationInstancesResponse, OperationMetadata>> PollOnceCreateApplicationInstancesAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateApplicationInstances`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CreateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateDraft(string, CallSettings)
    
    
    public virtual Operation<Draft, OperationMetadata> PollOnceCreateDraft(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateDraft`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateDraftAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> PollOnceCreateDraftAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateDraft`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateProcessor(string, CallSettings)
    
    
    public virtual Operation<Processor, OperationMetadata> PollOnceCreateProcessor(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateProcessor`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateProcessorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> PollOnceCreateProcessorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateProcessor`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteApplication(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteApplication(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteApplication` .

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteApplicationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteApplication`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteApplicationInstances(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceDeleteApplicationInstances(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteApplicationInstances`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteApplicationInstancesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceDeleteApplicationInstancesAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteApplicationInstances`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteDraft(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteDraft(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteDraft`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteDraftAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteDraftAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteDraft`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteProcessor(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteProcessor(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteProcessor`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteProcessorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteProcessorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteProcessor`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeployApplication(string, CallSettings)
    
    
    public virtual Operation<DeployApplicationResponse, OperationMetadata> PollOnceDeployApplication(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeployApplication` .

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeployApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<DeployApplicationResponse, OperationMetadata>> PollOnceDeployApplicationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeployApplication`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRemoveApplicationStreamInput(string, CallSettings)
    
    
    public virtual Operation<RemoveApplicationStreamInputResponse, OperationMetadata> PollOnceRemoveApplicationStreamInput(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RemoveApplicationStreamInput`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRemoveApplicationStreamInputAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RemoveApplicationStreamInputResponse, OperationMetadata>> PollOnceRemoveApplicationStreamInputAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RemoveApplicationStreamInput`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUndeployApplication(string, CallSettings)
    
    
    public virtual Operation<UndeployApplicationResponse, OperationMetadata> PollOnceUndeployApplication(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UndeployApplication` .

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUndeployApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<UndeployApplicationResponse, OperationMetadata>> PollOnceUndeployApplicationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UndeployApplication`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateApplication(string, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> PollOnceUpdateApplication(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateApplication` .

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> PollOnceUpdateApplicationAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateApplication`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateApplicationInstances(string, CallSettings)
    
    
    public virtual Operation<UpdateApplicationInstancesResponse, OperationMetadata> PollOnceUpdateApplicationInstances(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateApplicationInstances`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateApplicationInstancesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<UpdateApplicationInstancesResponse, OperationMetadata>> PollOnceUpdateApplicationInstancesAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateApplicationInstances`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateApplicationStreamInput(string, CallSettings)
    
    
    public virtual Operation<UpdateApplicationStreamInputResponse, OperationMetadata> PollOnceUpdateApplicationStreamInput(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateApplicationStreamInput`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateApplicationStreamInputAsync(string, CallSettings)
    
    
    public virtual Task<Operation<UpdateApplicationStreamInputResponse, OperationMetadata>> PollOnceUpdateApplicationStreamInputAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateApplicationStreamInput`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateDraft(string, CallSettings)
    
    
    public virtual Operation<Draft, OperationMetadata> PollOnceUpdateDraft(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateDraft`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateDraftAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> PollOnceUpdateDraftAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateDraft`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateProcessor(string, CallSettings)
    
    
    public virtual Operation<Processor, OperationMetadata> PollOnceUpdateProcessor(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateProcessor`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateProcessorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> PollOnceUpdateProcessorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateProcessor`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### RemoveApplicationStreamInput(ApplicationName, CallSettings)
    
    
    public virtual Operation<RemoveApplicationStreamInputResponse, OperationMetadata> RemoveApplicationStreamInput(ApplicationName name, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.RemoveApplicationStreamInput(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceRemoveApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveApplicationStreamInput(RemoveApplicationStreamInputRequest, CallSettings)
    
    
    public virtual Operation<RemoveApplicationStreamInputResponse, OperationMetadata> RemoveApplicationStreamInput(RemoveApplicationStreamInputRequest request, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    RemoveApplicationStreamInputRequest request = new RemoveApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        TargetStreamInputs =
        {
            new RemoveApplicationStreamInputRequest.Types.TargetStreamInput(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.RemoveApplicationStreamInput(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceRemoveApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveApplicationStreamInput(string, CallSettings)
    
    
    public virtual Operation<RemoveApplicationStreamInputResponse, OperationMetadata> RemoveApplicationStreamInput(string name, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.RemoveApplicationStreamInput(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceRemoveApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveApplicationStreamInputAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<RemoveApplicationStreamInputResponse, OperationMetadata>> RemoveApplicationStreamInputAsync(ApplicationName name, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.RemoveApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceRemoveApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveApplicationStreamInputAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<RemoveApplicationStreamInputResponse, OperationMetadata>> RemoveApplicationStreamInputAsync(ApplicationName name, CancellationToken cancellationToken)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.RemoveApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceRemoveApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveApplicationStreamInputAsync(RemoveApplicationStreamInputRequest, CallSettings)
    
    
    public virtual Task<Operation<RemoveApplicationStreamInputResponse, OperationMetadata>> RemoveApplicationStreamInputAsync(RemoveApplicationStreamInputRequest request, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    RemoveApplicationStreamInputRequest request = new RemoveApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        TargetStreamInputs =
        {
            new RemoveApplicationStreamInputRequest.Types.TargetStreamInput(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.RemoveApplicationStreamInputAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceRemoveApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveApplicationStreamInputAsync(RemoveApplicationStreamInputRequest, CancellationToken)
    
    
    public virtual Task<Operation<RemoveApplicationStreamInputResponse, OperationMetadata>> RemoveApplicationStreamInputAsync(RemoveApplicationStreamInputRequest request, CancellationToken cancellationToken)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    RemoveApplicationStreamInputRequest request = new RemoveApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        TargetStreamInputs =
        {
            new RemoveApplicationStreamInputRequest.Types.TargetStreamInput(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.RemoveApplicationStreamInputAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceRemoveApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveApplicationStreamInputAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RemoveApplicationStreamInputResponse, OperationMetadata>> RemoveApplicationStreamInputAsync(string name, CallSettings callSettings = null)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.RemoveApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceRemoveApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveApplicationStreamInputAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<RemoveApplicationStreamInputResponse, OperationMetadata>> RemoveApplicationStreamInputAsync(string name, CancellationToken cancellationToken)

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.RemoveApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RemoveApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RemoveApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceRemoveApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RemoveApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient#Google_Cloud_VisionAI_V1_AppPlatformClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient#Google_Cloud_VisionAI_V1_AppPlatformClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient#Google_Cloud_VisionAI_V1_AppPlatformClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AppPlatformClient#Google_Cloud_VisionAI_V1_AppPlatformClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UndeployApplication(ApplicationName, CallSettings)
    
    
    public virtual Operation<UndeployApplicationResponse, OperationMetadata> UndeployApplication(ApplicationName name, CallSettings callSettings = null)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = appPlatformClient.UndeployApplication(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUndeployApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployApplication(UndeployApplicationRequest, CallSettings)
    
    
    public virtual Operation<UndeployApplicationResponse, OperationMetadata> UndeployApplication(UndeployApplicationRequest request, CallSettings callSettings = null)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeployApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    UndeployApplicationRequest request = new UndeployApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = appPlatformClient.UndeployApplication(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUndeployApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployApplication(string, CallSettings)
    
    
    public virtual Operation<UndeployApplicationResponse, OperationMetadata> UndeployApplication(string name, CallSettings callSettings = null)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = appPlatformClient.UndeployApplication(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUndeployApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployApplicationAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<UndeployApplicationResponse, OperationMetadata>> UndeployApplicationAsync(ApplicationName name, CallSettings callSettings = null)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = await appPlatformClient.UndeployApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUndeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployApplicationAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<UndeployApplicationResponse, OperationMetadata>> UndeployApplicationAsync(ApplicationName name, CancellationToken cancellationToken)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = await appPlatformClient.UndeployApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUndeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployApplicationAsync(UndeployApplicationRequest, CallSettings)
    
    
    public virtual Task<Operation<UndeployApplicationResponse, OperationMetadata>> UndeployApplicationAsync(UndeployApplicationRequest request, CallSettings callSettings = null)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeployApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UndeployApplicationRequest request = new UndeployApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = await appPlatformClient.UndeployApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUndeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployApplicationAsync(UndeployApplicationRequest, CancellationToken)
    
    
    public virtual Task<Operation<UndeployApplicationResponse, OperationMetadata>> UndeployApplicationAsync(UndeployApplicationRequest request, CancellationToken cancellationToken)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeployApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UndeployApplicationRequest request = new UndeployApplicationRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        RequestId = "",
    };
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = await appPlatformClient.UndeployApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUndeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployApplicationAsync(string, CallSettings)
    
    
    public virtual Task<Operation<UndeployApplicationResponse, OperationMetadata>> UndeployApplicationAsync(string name, CallSettings callSettings = null)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = await appPlatformClient.UndeployApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUndeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployApplicationAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<UndeployApplicationResponse, OperationMetadata>> UndeployApplicationAsync(string name, CancellationToken cancellationToken)

Undeploys a single Application.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployApplicationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployApplicationResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<UndeployApplicationResponse, OperationMetadata> response = await appPlatformClient.UndeployApplicationAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UndeployApplicationResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UndeployApplicationResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UndeployApplicationResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUndeployApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UndeployApplicationResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplication(Application, FieldMask, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> UpdateApplication(Application application, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Application resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    Application application = new Application();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Application, OperationMetadata> response = appPlatformClient.UpdateApplication(application, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplication(UpdateApplicationRequest, CallSettings)
    
    
    public virtual Operation<Application, OperationMetadata> UpdateApplication(UpdateApplicationRequest request, CallSettings callSettings = null)

Updates the parameters of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    UpdateApplicationRequest request = new UpdateApplicationRequest
    {
        UpdateMask = new FieldMask(),
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = appPlatformClient.UpdateApplication(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateApplication(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationAsync(Application, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> UpdateApplicationAsync(Application application, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Application resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    Application application = new Application();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.UpdateApplicationAsync(application, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationAsync(Application, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> UpdateApplicationAsync(Application application, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`application` | `[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Application resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    Application application = new Application();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.UpdateApplicationAsync(application, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationAsync(UpdateApplicationRequest, CallSettings)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> UpdateApplicationAsync(UpdateApplicationRequest request, CallSettings callSettings = null)

Updates the parameters of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateApplicationRequest request = new UpdateApplicationRequest
    {
        UpdateMask = new FieldMask(),
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.UpdateApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationAsync(UpdateApplicationRequest, CancellationToken)
    
    
    public virtual Task<Operation<Application, OperationMetadata>> UpdateApplicationAsync(UpdateApplicationRequest request, CancellationToken cancellationToken)

Updates the parameters of a single Application.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Application](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Application)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateApplicationRequest request = new UpdateApplicationRequest
    {
        UpdateMask = new FieldMask(),
        Application = new Application(),
        RequestId = "",
    };
    // Make the request
    Operation<Application, OperationMetadata> response = await appPlatformClient.UpdateApplicationAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Application, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Application result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Application, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Application retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstances(ApplicationName, IEnumerable<UpdateApplicationInstance>, CallSettings)
    
    
    public virtual Operation<UpdateApplicationInstancesResponse, OperationMetadata> UpdateApplicationInstances(ApplicationName name, IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`applicationInstances` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types)[UpdateApplicationInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance)`  
  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances = new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance[]
    {
        new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = appPlatformClient.UpdateApplicationInstances(name, applicationInstances);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstances(UpdateApplicationInstancesRequest, CallSettings)
    
    
    public virtual Operation<UpdateApplicationInstancesResponse, OperationMetadata> UpdateApplicationInstances(UpdateApplicationInstancesRequest request, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    UpdateApplicationInstancesRequest request = new UpdateApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationInstances =
        {
            new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
        },
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = appPlatformClient.UpdateApplicationInstances(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstances(string, IEnumerable<UpdateApplicationInstance>, CallSettings)
    
    
    public virtual Operation<UpdateApplicationInstancesResponse, OperationMetadata> UpdateApplicationInstances(string name, IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`applicationInstances` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types)[UpdateApplicationInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance)`  
  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances = new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance[]
    {
        new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = appPlatformClient.UpdateApplicationInstances(name, applicationInstances);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateApplicationInstances(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstancesAsync(ApplicationName, IEnumerable<UpdateApplicationInstance>, CallSettings)
    
    
    public virtual Task<Operation<UpdateApplicationInstancesResponse, OperationMetadata>> UpdateApplicationInstancesAsync(ApplicationName name, IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`applicationInstances` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types)[UpdateApplicationInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance)`  
  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances = new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance[]
    {
        new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationInstancesAsync(name, applicationInstances);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstancesAsync(ApplicationName, IEnumerable<UpdateApplicationInstance>, CancellationToken)
    
    
    public virtual Task<Operation<UpdateApplicationInstancesResponse, OperationMetadata>> UpdateApplicationInstancesAsync(ApplicationName name, IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`applicationInstances` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types)[UpdateApplicationInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance)`  
  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances = new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance[]
    {
        new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationInstancesAsync(name, applicationInstances);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstancesAsync(UpdateApplicationInstancesRequest, CallSettings)
    
    
    public virtual Task<Operation<UpdateApplicationInstancesResponse, OperationMetadata>> UpdateApplicationInstancesAsync(UpdateApplicationInstancesRequest request, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateApplicationInstancesRequest request = new UpdateApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationInstances =
        {
            new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
        },
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationInstancesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstancesAsync(UpdateApplicationInstancesRequest, CancellationToken)
    
    
    public virtual Task<Operation<UpdateApplicationInstancesResponse, OperationMetadata>> UpdateApplicationInstancesAsync(UpdateApplicationInstancesRequest request, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateApplicationInstancesRequest request = new UpdateApplicationInstancesRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationInstances =
        {
            new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
        },
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationInstancesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstancesAsync(string, IEnumerable<UpdateApplicationInstance>, CallSettings)
    
    
    public virtual Task<Operation<UpdateApplicationInstancesResponse, OperationMetadata>> UpdateApplicationInstancesAsync(string name, IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances, CallSettings callSettings = null)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`applicationInstances` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types)[UpdateApplicationInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance)`  
  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances = new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance[]
    {
        new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationInstancesAsync(name, applicationInstances);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationInstancesAsync(string, IEnumerable<UpdateApplicationInstance>, CancellationToken)
    
    
    public virtual Task<Operation<UpdateApplicationInstancesResponse, OperationMetadata>> UpdateApplicationInstancesAsync(string name, IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances, CancellationToken cancellationToken)

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`applicationInstances` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types)[UpdateApplicationInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance)`  
  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationInstancesResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    IEnumerable<UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance> applicationInstances = new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance[]
    {
        new UpdateApplicationInstancesRequest.Types.UpdateApplicationInstance(),
    };
    // Make the request
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationInstancesAsync(name, applicationInstances);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationInstancesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationInstancesResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationInstancesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationInstancesResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInput(ApplicationName, CallSettings)
    
    
    public virtual Operation<UpdateApplicationStreamInputResponse, OperationMetadata> UpdateApplicationStreamInput(ApplicationName name, CallSettings callSettings = null)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.UpdateApplicationStreamInput(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInput(UpdateApplicationStreamInputRequest, CallSettings)
    
    
    public virtual Operation<UpdateApplicationStreamInputResponse, OperationMetadata> UpdateApplicationStreamInput(UpdateApplicationStreamInputRequest request, CallSettings callSettings = null)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    UpdateApplicationStreamInputRequest request = new UpdateApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationStreamInputs =
        {
            new ApplicationStreamInput(),
        },
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.UpdateApplicationStreamInput(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInput(string, CallSettings)
    
    
    public virtual Operation<UpdateApplicationStreamInputResponse, OperationMetadata> UpdateApplicationStreamInput(string name, CallSettings callSettings = null)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = appPlatformClient.UpdateApplicationStreamInput(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateApplicationStreamInput(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInputAsync(ApplicationName, CallSettings)
    
    
    public virtual Task<Operation<UpdateApplicationStreamInputResponse, OperationMetadata>> UpdateApplicationStreamInputAsync(ApplicationName name, CallSettings callSettings = null)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInputAsync(ApplicationName, CancellationToken)
    
    
    public virtual Task<Operation<UpdateApplicationStreamInputResponse, OperationMetadata>> UpdateApplicationStreamInputAsync(ApplicationName name, CancellationToken cancellationToken)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ApplicationName)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    ApplicationName name = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]");
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInputAsync(UpdateApplicationStreamInputRequest, CallSettings)
    
    
    public virtual Task<Operation<UpdateApplicationStreamInputResponse, OperationMetadata>> UpdateApplicationStreamInputAsync(UpdateApplicationStreamInputRequest request, CallSettings callSettings = null)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateApplicationStreamInputRequest request = new UpdateApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationStreamInputs =
        {
            new ApplicationStreamInput(),
        },
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationStreamInputAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInputAsync(UpdateApplicationStreamInputRequest, CancellationToken)
    
    
    public virtual Task<Operation<UpdateApplicationStreamInputResponse, OperationMetadata>> UpdateApplicationStreamInputAsync(UpdateApplicationStreamInputRequest request, CancellationToken cancellationToken)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationStreamInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateApplicationStreamInputRequest request = new UpdateApplicationStreamInputRequest
    {
        ApplicationName = ApplicationName.FromProjectLocationApplication("[PROJECT]", "[LOCATION]", "[APPLICATION]"),
        ApplicationStreamInputs =
        {
            new ApplicationStreamInput(),
        },
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationStreamInputAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInputAsync(string, CallSettings)
    
    
    public virtual Task<Operation<UpdateApplicationStreamInputResponse, OperationMetadata>> UpdateApplicationStreamInputAsync(string name, CallSettings callSettings = null)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateApplicationStreamInputAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<UpdateApplicationStreamInputResponse, OperationMetadata>> UpdateApplicationStreamInputAsync(string name, CancellationToken cancellationToken)

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateApplicationStreamInputResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/applications/[APPLICATION]";
    // Make the request
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> response = await appPlatformClient.UpdateApplicationStreamInputAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    UpdateApplicationStreamInputResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<UpdateApplicationStreamInputResponse, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateApplicationStreamInputAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        UpdateApplicationStreamInputResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDraft(Draft, FieldMask, CallSettings)
    
    
    public virtual Operation<Draft, OperationMetadata> UpdateDraft(Draft draft, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Draft resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    Draft draft = new Draft();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Draft, OperationMetadata> response = appPlatformClient.UpdateDraft(draft, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateDraft(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDraft(UpdateDraftRequest, CallSettings)
    
    
    public virtual Operation<Draft, OperationMetadata> UpdateDraft(UpdateDraftRequest request, CallSettings callSettings = null)

Updates the parameters of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateDraftRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    UpdateDraftRequest request = new UpdateDraftRequest
    {
        UpdateMask = new FieldMask(),
        Draft = new Draft(),
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<Draft, OperationMetadata> response = appPlatformClient.UpdateDraft(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateDraft(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDraftAsync(Draft, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> UpdateDraftAsync(Draft draft, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Draft resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    Draft draft = new Draft();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.UpdateDraftAsync(draft, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDraftAsync(Draft, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> UpdateDraftAsync(Draft draft, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`draft` | `[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Draft resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    Draft draft = new Draft();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.UpdateDraftAsync(draft, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDraftAsync(UpdateDraftRequest, CallSettings)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> UpdateDraftAsync(UpdateDraftRequest request, CallSettings callSettings = null)

Updates the parameters of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateDraftRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDraftRequest request = new UpdateDraftRequest
    {
        UpdateMask = new FieldMask(),
        Draft = new Draft(),
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.UpdateDraftAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### UpdateDraftAsync(UpdateDraftRequest, CancellationToken)
    
    
    public virtual Task<Operation<Draft, OperationMetadata>> UpdateDraftAsync(UpdateDraftRequest request, CancellationToken cancellationToken)

Updates the parameters of a single Draft.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDraftRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateDraftRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Draft](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Draft)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDraftRequest request = new UpdateDraftRequest
    {
        UpdateMask = new FieldMask(),
        Draft = new Draft(),
        RequestId = "",
        AllowMissing = false,
    };
    // Make the request
    Operation<Draft, OperationMetadata> response = await appPlatformClient.UpdateDraftAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Draft, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Draft result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Draft, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateDraftAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Draft retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProcessor(Processor, FieldMask, CallSettings)
    
    
    public virtual Operation<Processor, OperationMetadata> UpdateProcessor(Processor processor, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Processor resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    Processor processor = new Processor();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Processor, OperationMetadata> response = appPlatformClient.UpdateProcessor(processor, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateProcessor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProcessor(UpdateProcessorRequest, CallSettings)
    
    
    public virtual Operation<Processor, OperationMetadata> UpdateProcessor(UpdateProcessorRequest request, CallSettings callSettings = null)

Updates the parameters of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = AppPlatformClient.Create();
    // Initialize request argument(s)
    UpdateProcessorRequest request = new UpdateProcessorRequest
    {
        UpdateMask = new FieldMask(),
        Processor = new Processor(),
        RequestId = "",
    };
    // Make the request
    Operation<Processor, OperationMetadata> response = appPlatformClient.UpdateProcessor(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = appPlatformClient.PollOnceUpdateProcessor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProcessorAsync(Processor, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> UpdateProcessorAsync(Processor processor, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Processor resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    Processor processor = new Processor();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.UpdateProcessorAsync(processor, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProcessorAsync(Processor, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> UpdateProcessorAsync(Processor processor, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`processor` | `[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Processor resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    Processor processor = new Processor();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.UpdateProcessorAsync(processor, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProcessorAsync(UpdateProcessorRequest, CallSettings)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> UpdateProcessorAsync(UpdateProcessorRequest request, CallSettings callSettings = null)

Updates the parameters of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateProcessorRequest request = new UpdateProcessorRequest
    {
        UpdateMask = new FieldMask(),
        Processor = new Processor(),
        RequestId = "",
    };
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.UpdateProcessorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateProcessorAsync(UpdateProcessorRequest, CancellationToken)
    
    
    public virtual Task<Operation<Processor, OperationMetadata>> UpdateProcessorAsync(UpdateProcessorRequest request, CancellationToken cancellationToken)

Updates the parameters of a single Processor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateProcessorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Processor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Processor)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppPlatformClient appPlatformClient = await AppPlatformClient.CreateAsync();
    // Initialize request argument(s)
    UpdateProcessorRequest request = new UpdateProcessorRequest
    {
        UpdateMask = new FieldMask(),
        Processor = new Processor(),
        RequestId = "",
    };
    // Make the request
    Operation<Processor, OperationMetadata> response = await appPlatformClient.UpdateProcessorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Processor, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Processor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Processor, OperationMetadata> retrievedResponse = await appPlatformClient.PollOnceUpdateProcessorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Processor retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
