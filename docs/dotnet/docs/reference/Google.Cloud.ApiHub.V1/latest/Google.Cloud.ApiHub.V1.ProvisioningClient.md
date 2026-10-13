---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient
title: API hub v1 API - Class ProvisioningClient (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:13.519835+00:00
---

# API hub v1 API - Class ProvisioningClient (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class ProvisioningClient (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.ProvisioningClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.ProvisioningClient)


    
    
    public abstract class ProvisioningClient

Reference documentation and code samples for the API hub v1 API class ProvisioningClient.

Provisioning client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProvisioningClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ProvisioningClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClientImpl)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Remarks

This service is used for managing the data plane provisioning of the API hub.

## Properties 

### CreateApiHubInstanceOperationsClient
    
    
    public virtual OperationsClient CreateApiHubInstanceOperationsClient { get; }

The long-running operations client for `CreateApiHubInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Provisioning service, which is a host of "apihub.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Provisioning scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Provisioning scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteApiHubInstanceOperationsClient
    
    
    public virtual OperationsClient DeleteApiHubInstanceOperationsClient { get; }

The long-running operations client for `DeleteApiHubInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual Provisioning.ProvisioningClient GrpcClient { get; }

The underlying gRPC Provisioning client

**Property Value**  
---  
**Type** | **Description**  
`[Provisioning](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Provisioning)[ProvisioningClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.Provisioning.ProvisioningClient)` |   
  
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
  
## Methods 

### Create()
    
    
    public static ProvisioningClient Create()

Synchronously creates a [ProvisioningClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ProvisioningClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ProvisioningClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient)` | The created [ProvisioningClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient).  
  
### CreateApiHubInstance(LocationName, ApiHubInstance, string, CallSettings)
    
    
    public virtual Operation<ApiHubInstance, OperationMetadata> CreateApiHubInstance(LocationName parent, ApiHubInstance apiHubInstance, string apiHubInstanceId, CallSettings callSettings = null)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`apiHubInstance` | `[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)`  
Required. The ApiHub instance.  
`apiHubInstanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Identifier to assign to the Api Hub instance. Must be unique within scope of the parent resource. If the field is not provided, system generated id will be used. This value should be 4-40 characters, and valid characters are `/[a-z][A-Z][0-9]-_/`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ApiHubInstance apiHubInstance = new ApiHubInstance();
    string apiHubInstanceId = "";
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = provisioningClient.CreateApiHubInstance(parent, apiHubInstance, apiHubInstanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = provisioningClient.PollOnceCreateApiHubInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateApiHubInstance(CreateApiHubInstanceRequest, CallSettings)
    
    
    public virtual Operation<ApiHubInstance, OperationMetadata> CreateApiHubInstance(CreateApiHubInstanceRequest request, CallSettings callSettings = null)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreateApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    CreateApiHubInstanceRequest request = new CreateApiHubInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApiHubInstanceId = "",
        ApiHubInstance = new ApiHubInstance(),
    };
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = provisioningClient.CreateApiHubInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = provisioningClient.PollOnceCreateApiHubInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateApiHubInstance(string, ApiHubInstance, string, CallSettings)
    
    
    public virtual Operation<ApiHubInstance, OperationMetadata> CreateApiHubInstance(string parent, ApiHubInstance apiHubInstance, string apiHubInstanceId, CallSettings callSettings = null)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`apiHubInstance` | `[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)`  
Required. The ApiHub instance.  
`apiHubInstanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Identifier to assign to the Api Hub instance. Must be unique within scope of the parent resource. If the field is not provided, system generated id will be used. This value should be 4-40 characters, and valid characters are `/[a-z][A-Z][0-9]-_/`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ApiHubInstance apiHubInstance = new ApiHubInstance();
    string apiHubInstanceId = "";
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = provisioningClient.CreateApiHubInstance(parent, apiHubInstance, apiHubInstanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = provisioningClient.PollOnceCreateApiHubInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateApiHubInstanceAsync(LocationName, ApiHubInstance, string, CallSettings)
    
    
    public virtual Task<Operation<ApiHubInstance, OperationMetadata>> CreateApiHubInstanceAsync(LocationName parent, ApiHubInstance apiHubInstance, string apiHubInstanceId, CallSettings callSettings = null)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`apiHubInstance` | `[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)`  
Required. The ApiHub instance.  
`apiHubInstanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Identifier to assign to the Api Hub instance. Must be unique within scope of the parent resource. If the field is not provided, system generated id will be used. This value should be 4-40 characters, and valid characters are `/[a-z][A-Z][0-9]-_/`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ApiHubInstance apiHubInstance = new ApiHubInstance();
    string apiHubInstanceId = "";
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = await provisioningClient.CreateApiHubInstanceAsync(parent, apiHubInstance, apiHubInstanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceCreateApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateApiHubInstanceAsync(LocationName, ApiHubInstance, string, CancellationToken)
    
    
    public virtual Task<Operation<ApiHubInstance, OperationMetadata>> CreateApiHubInstanceAsync(LocationName parent, ApiHubInstance apiHubInstance, string apiHubInstanceId, CancellationToken cancellationToken)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`apiHubInstance` | `[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)`  
Required. The ApiHub instance.  
`apiHubInstanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Identifier to assign to the Api Hub instance. Must be unique within scope of the parent resource. If the field is not provided, system generated id will be used. This value should be 4-40 characters, and valid characters are `/[a-z][A-Z][0-9]-_/`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    ApiHubInstance apiHubInstance = new ApiHubInstance();
    string apiHubInstanceId = "";
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = await provisioningClient.CreateApiHubInstanceAsync(parent, apiHubInstance, apiHubInstanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceCreateApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateApiHubInstanceAsync(CreateApiHubInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<ApiHubInstance, OperationMetadata>> CreateApiHubInstanceAsync(CreateApiHubInstanceRequest request, CallSettings callSettings = null)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreateApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    CreateApiHubInstanceRequest request = new CreateApiHubInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApiHubInstanceId = "",
        ApiHubInstance = new ApiHubInstance(),
    };
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = await provisioningClient.CreateApiHubInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceCreateApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateApiHubInstanceAsync(CreateApiHubInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<ApiHubInstance, OperationMetadata>> CreateApiHubInstanceAsync(CreateApiHubInstanceRequest request, CancellationToken cancellationToken)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreateApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    CreateApiHubInstanceRequest request = new CreateApiHubInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ApiHubInstanceId = "",
        ApiHubInstance = new ApiHubInstance(),
    };
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = await provisioningClient.CreateApiHubInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceCreateApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateApiHubInstanceAsync(string, ApiHubInstance, string, CallSettings)
    
    
    public virtual Task<Operation<ApiHubInstance, OperationMetadata>> CreateApiHubInstanceAsync(string parent, ApiHubInstance apiHubInstance, string apiHubInstanceId, CallSettings callSettings = null)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`apiHubInstance` | `[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)`  
Required. The ApiHub instance.  
`apiHubInstanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Identifier to assign to the Api Hub instance. Must be unique within scope of the parent resource. If the field is not provided, system generated id will be used. This value should be 4-40 characters, and valid characters are `/[a-z][A-Z][0-9]-_/`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ApiHubInstance apiHubInstance = new ApiHubInstance();
    string apiHubInstanceId = "";
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = await provisioningClient.CreateApiHubInstanceAsync(parent, apiHubInstance, apiHubInstanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceCreateApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateApiHubInstanceAsync(string, ApiHubInstance, string, CancellationToken)
    
    
    public virtual Task<Operation<ApiHubInstance, OperationMetadata>> CreateApiHubInstanceAsync(string parent, ApiHubInstance apiHubInstance, string apiHubInstanceId, CancellationToken cancellationToken)

Provisions instance resources for the API Hub.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`apiHubInstance` | `[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)`  
Required. The ApiHub instance.  
`apiHubInstanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. Identifier to assign to the Api Hub instance. Must be unique within scope of the parent resource. If the field is not provided, system generated id will be used. This value should be 4-40 characters, and valid characters are `/[a-z][A-Z][0-9]-_/`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    ApiHubInstance apiHubInstance = new ApiHubInstance();
    string apiHubInstanceId = "";
    // Make the request
    Operation<ApiHubInstance, OperationMetadata> response = await provisioningClient.CreateApiHubInstanceAsync(parent, apiHubInstance, apiHubInstanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<ApiHubInstance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ApiHubInstance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ApiHubInstance, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceCreateApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ApiHubInstance retrievedResult = retrievedResponse.Result;
    }
    

### CreateAsync(CancellationToken)
    
    
    public static Task<ProvisioningClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ProvisioningClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ProvisioningClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProvisioningClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient)` | The task representing the created [ProvisioningClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient).  
  
### DeleteApiHubInstance(ApiHubInstanceName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApiHubInstance(ApiHubInstanceName name, CallSettings callSettings = null)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApiHubInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstanceName)`  
Required. The name of the Api Hub instance to delete. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    ApiHubInstanceName name = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = provisioningClient.DeleteApiHubInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = provisioningClient.PollOnceDeleteApiHubInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApiHubInstance(DeleteApiHubInstanceRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApiHubInstance(DeleteApiHubInstanceRequest request, CallSettings callSettings = null)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeleteApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    DeleteApiHubInstanceRequest request = new DeleteApiHubInstanceRequest
    {
        ApiHubInstanceName = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = provisioningClient.DeleteApiHubInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = provisioningClient.PollOnceDeleteApiHubInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApiHubInstance(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApiHubInstance(string name, CallSettings callSettings = null)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Api Hub instance to delete. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apiHubInstances/[API_HUB_INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = provisioningClient.DeleteApiHubInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = provisioningClient.PollOnceDeleteApiHubInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApiHubInstanceAsync(ApiHubInstanceName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApiHubInstanceAsync(ApiHubInstanceName name, CallSettings callSettings = null)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApiHubInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstanceName)`  
Required. The name of the Api Hub instance to delete. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    ApiHubInstanceName name = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await provisioningClient.DeleteApiHubInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceDeleteApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApiHubInstanceAsync(ApiHubInstanceName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApiHubInstanceAsync(ApiHubInstanceName name, CancellationToken cancellationToken)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApiHubInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstanceName)`  
Required. The name of the Api Hub instance to delete. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    ApiHubInstanceName name = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await provisioningClient.DeleteApiHubInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceDeleteApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApiHubInstanceAsync(DeleteApiHubInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApiHubInstanceAsync(DeleteApiHubInstanceRequest request, CallSettings callSettings = null)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeleteApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    DeleteApiHubInstanceRequest request = new DeleteApiHubInstanceRequest
    {
        ApiHubInstanceName = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await provisioningClient.DeleteApiHubInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceDeleteApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApiHubInstanceAsync(DeleteApiHubInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApiHubInstanceAsync(DeleteApiHubInstanceRequest request, CancellationToken cancellationToken)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeleteApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    DeleteApiHubInstanceRequest request = new DeleteApiHubInstanceRequest
    {
        ApiHubInstanceName = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await provisioningClient.DeleteApiHubInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceDeleteApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApiHubInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApiHubInstanceAsync(string name, CallSettings callSettings = null)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Api Hub instance to delete. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apiHubInstances/[API_HUB_INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await provisioningClient.DeleteApiHubInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceDeleteApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApiHubInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteApiHubInstanceAsync(string name, CancellationToken cancellationToken)

Deletes the API hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Api Hub instance to delete. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apiHubInstances/[API_HUB_INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await provisioningClient.DeleteApiHubInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await provisioningClient.PollOnceDeleteApiHubInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetApiHubInstance(ApiHubInstanceName, CallSettings)
    
    
    public virtual ApiHubInstance GetApiHubInstance(ApiHubInstanceName name, CallSettings callSettings = null)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApiHubInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstanceName)`  
Required. The name of the Api Hub instance to retrieve. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    ApiHubInstanceName name = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]");
    // Make the request
    ApiHubInstance response = provisioningClient.GetApiHubInstance(name);
    

### GetApiHubInstance(GetApiHubInstanceRequest, CallSettings)
    
    
    public virtual ApiHubInstance GetApiHubInstance(GetApiHubInstanceRequest request, CallSettings callSettings = null)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    GetApiHubInstanceRequest request = new GetApiHubInstanceRequest
    {
        ApiHubInstanceName = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]"),
    };
    // Make the request
    ApiHubInstance response = provisioningClient.GetApiHubInstance(request);
    

### GetApiHubInstance(string, CallSettings)
    
    
    public virtual ApiHubInstance GetApiHubInstance(string name, CallSettings callSettings = null)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Api Hub instance to retrieve. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apiHubInstances/[API_HUB_INSTANCE]";
    // Make the request
    ApiHubInstance response = provisioningClient.GetApiHubInstance(name);
    

### GetApiHubInstanceAsync(ApiHubInstanceName, CallSettings)
    
    
    public virtual Task<ApiHubInstance> GetApiHubInstanceAsync(ApiHubInstanceName name, CallSettings callSettings = null)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApiHubInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstanceName)`  
Required. The name of the Api Hub instance to retrieve. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    ApiHubInstanceName name = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]");
    // Make the request
    ApiHubInstance response = await provisioningClient.GetApiHubInstanceAsync(name);
    

### GetApiHubInstanceAsync(ApiHubInstanceName, CancellationToken)
    
    
    public virtual Task<ApiHubInstance> GetApiHubInstanceAsync(ApiHubInstanceName name, CancellationToken cancellationToken)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ApiHubInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstanceName)`  
Required. The name of the Api Hub instance to retrieve. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    ApiHubInstanceName name = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]");
    // Make the request
    ApiHubInstance response = await provisioningClient.GetApiHubInstanceAsync(name);
    

### GetApiHubInstanceAsync(GetApiHubInstanceRequest, CallSettings)
    
    
    public virtual Task<ApiHubInstance> GetApiHubInstanceAsync(GetApiHubInstanceRequest request, CallSettings callSettings = null)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    GetApiHubInstanceRequest request = new GetApiHubInstanceRequest
    {
        ApiHubInstanceName = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]"),
    };
    // Make the request
    ApiHubInstance response = await provisioningClient.GetApiHubInstanceAsync(request);
    

### GetApiHubInstanceAsync(GetApiHubInstanceRequest, CancellationToken)
    
    
    public virtual Task<ApiHubInstance> GetApiHubInstanceAsync(GetApiHubInstanceRequest request, CancellationToken cancellationToken)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.GetApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    GetApiHubInstanceRequest request = new GetApiHubInstanceRequest
    {
        ApiHubInstanceName = ApiHubInstanceName.FromProjectLocationApiHubInstance("[PROJECT]", "[LOCATION]", "[API_HUB_INSTANCE]"),
    };
    // Make the request
    ApiHubInstance response = await provisioningClient.GetApiHubInstanceAsync(request);
    

### GetApiHubInstanceAsync(string, CallSettings)
    
    
    public virtual Task<ApiHubInstance> GetApiHubInstanceAsync(string name, CallSettings callSettings = null)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Api Hub instance to retrieve. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apiHubInstances/[API_HUB_INSTANCE]";
    // Make the request
    ApiHubInstance response = await provisioningClient.GetApiHubInstanceAsync(name);
    

### GetApiHubInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<ApiHubInstance> GetApiHubInstanceAsync(string name, CancellationToken cancellationToken)

Gets details of a single API Hub instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Api Hub instance to retrieve. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apiHubInstances/[API_HUB_INSTANCE]";
    // Make the request
    ApiHubInstance response = await provisioningClient.GetApiHubInstanceAsync(name);
    

### LookupApiHubInstance(LocationName, CallSettings)
    
    
    public virtual LookupApiHubInstanceResponse LookupApiHubInstance(LocationName parent, CallSettings callSettings = null)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. There will always be only one Api Hub instance for a GCP project across all locations. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    LookupApiHubInstanceResponse response = provisioningClient.LookupApiHubInstance(parent);
    

### LookupApiHubInstance(LookupApiHubInstanceRequest, CallSettings)
    
    
    public virtual LookupApiHubInstanceResponse LookupApiHubInstance(LookupApiHubInstanceRequest request, CallSettings callSettings = null)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    LookupApiHubInstanceRequest request = new LookupApiHubInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    LookupApiHubInstanceResponse response = provisioningClient.LookupApiHubInstance(request);
    

### LookupApiHubInstance(string, CallSettings)
    
    
    public virtual LookupApiHubInstanceResponse LookupApiHubInstance(string parent, CallSettings callSettings = null)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. There will always be only one Api Hub instance for a GCP project across all locations. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = ProvisioningClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    LookupApiHubInstanceResponse response = provisioningClient.LookupApiHubInstance(parent);
    

### LookupApiHubInstanceAsync(LocationName, CallSettings)
    
    
    public virtual Task<LookupApiHubInstanceResponse> LookupApiHubInstanceAsync(LocationName parent, CallSettings callSettings = null)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. There will always be only one Api Hub instance for a GCP project across all locations. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    LookupApiHubInstanceResponse response = await provisioningClient.LookupApiHubInstanceAsync(parent);
    

### LookupApiHubInstanceAsync(LocationName, CancellationToken)
    
    
    public virtual Task<LookupApiHubInstanceResponse> LookupApiHubInstanceAsync(LocationName parent, CancellationToken cancellationToken)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. There will always be only one Api Hub instance for a GCP project across all locations. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    LookupApiHubInstanceResponse response = await provisioningClient.LookupApiHubInstanceAsync(parent);
    

### LookupApiHubInstanceAsync(LookupApiHubInstanceRequest, CallSettings)
    
    
    public virtual Task<LookupApiHubInstanceResponse> LookupApiHubInstanceAsync(LookupApiHubInstanceRequest request, CallSettings callSettings = null)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    LookupApiHubInstanceRequest request = new LookupApiHubInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    LookupApiHubInstanceResponse response = await provisioningClient.LookupApiHubInstanceAsync(request);
    

### LookupApiHubInstanceAsync(LookupApiHubInstanceRequest, CancellationToken)
    
    
    public virtual Task<LookupApiHubInstanceResponse> LookupApiHubInstanceAsync(LookupApiHubInstanceRequest request, CancellationToken cancellationToken)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupApiHubInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    LookupApiHubInstanceRequest request = new LookupApiHubInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    LookupApiHubInstanceResponse response = await provisioningClient.LookupApiHubInstanceAsync(request);
    

### LookupApiHubInstanceAsync(string, CallSettings)
    
    
    public virtual Task<LookupApiHubInstanceResponse> LookupApiHubInstanceAsync(string parent, CallSettings callSettings = null)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. There will always be only one Api Hub instance for a GCP project across all locations. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    LookupApiHubInstanceResponse response = await provisioningClient.LookupApiHubInstanceAsync(parent);
    

### LookupApiHubInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<LookupApiHubInstanceResponse> LookupApiHubInstanceAsync(string parent, CancellationToken cancellationToken)

Looks up an Api Hub instance in a given GCP project. There will always be only one Api Hub instance for a GCP project across all locations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. There will always be only one Api Hub instance for a GCP project across all locations. The parent resource for the Api Hub instance resource. Format: `projects/{project}/locations/{location}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupApiHubInstanceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.LookupApiHubInstanceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ProvisioningClient provisioningClient = await ProvisioningClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    LookupApiHubInstanceResponse response = await provisioningClient.LookupApiHubInstanceAsync(parent);
    

### PollOnceCreateApiHubInstance(string, CallSettings)
    
    
    public virtual Operation<ApiHubInstance, OperationMetadata> PollOnceCreateApiHubInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateApiHubInstance` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateApiHubInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ApiHubInstance, OperationMetadata>> PollOnceCreateApiHubInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateApiHubInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ApiHubInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ApiHubInstance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteApiHubInstance(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteApiHubInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteApiHubInstance` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteApiHubInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteApiHubInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteApiHubInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient#Google_Cloud_ApiHub_V1_ProvisioningClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient#Google_Cloud_ApiHub_V1_ProvisioningClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient#Google_Cloud_ApiHub_V1_ProvisioningClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ProvisioningClient#Google_Cloud_ApiHub_V1_ProvisioningClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
