---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient
title: Cloud IDS v1 API - Class IDSClient (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:14.259297+00:00
---

# Cloud IDS v1 API - Class IDSClient (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud IDS v1 API - Class IDSClient (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/2.4.0/Google.Cloud.Ids.V1.IDSClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/2.3.0/Google.Cloud.Ids.V1.IDSClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/2.2.0/Google.Cloud.Ids.V1.IDSClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/2.1.0/Google.Cloud.Ids.V1.IDSClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/2.0.0/Google.Cloud.Ids.V1.IDSClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/1.0.0/Google.Cloud.Ids.V1.IDSClient)


    
    
    public abstract class IDSClient

Reference documentation and code samples for the Cloud IDS v1 API class IDSClient.

IDS client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > IDSClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[IDSClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClientImpl)

## Namespace

[Google.Cloud.Ids.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1)

## Assembly

Google.Cloud.Ids.V1.dll

## Remarks

The IDS Service

## Properties 

### CreateEndpointOperationsClient
    
    
    public virtual OperationsClient CreateEndpointOperationsClient { get; }

The long-running operations client for `CreateEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the IDS service, which is a host of "ids.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default IDS scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default IDS scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteEndpointOperationsClient
    
    
    public virtual OperationsClient DeleteEndpointOperationsClient { get; }

The long-running operations client for `DeleteEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual IDS.IDSClient GrpcClient { get; }

The underlying gRPC IDS client

**Property Value**  
---  
**Type** | **Description**  
`[IDS](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDS)[IDSClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDS.IDSClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static IDSClient Create()

Synchronously creates a [IDSClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [IDSClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[IDSClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient)` | The created [IDSClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<IDSClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [IDSClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [IDSClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IDSClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient)` | The task representing the created [IDSClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient).  
  
### CreateEndpoint(LocationName, Endpoint, string, CallSettings)
    
    
    public virtual Operation<Endpoint, OperationMetadata> CreateEndpoint(LocationName parent, Endpoint endpoint, string endpointId, CallSettings callSettings = null)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The endpoint's parent.  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)`  
Required. The endpoint to create.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint identifier. This will be part of the endpoint's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. Values that do not match this pattern will trigger an INVALID_ARGUMENT error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Endpoint endpoint = new Endpoint();
    string endpointId = "";
    // Make the request
    Operation<Endpoint, OperationMetadata> response = iDSClient.CreateEndpoint(parent, endpoint, endpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = iDSClient.PollOnceCreateEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateEndpoint(CreateEndpointRequest, CallSettings)
    
    
    public virtual Operation<Endpoint, OperationMetadata> CreateEndpoint(CreateEndpointRequest request, CallSettings callSettings = null)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.CreateEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    CreateEndpointRequest request = new CreateEndpointRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        EndpointId = "",
        Endpoint = new Endpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<Endpoint, OperationMetadata> response = iDSClient.CreateEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = iDSClient.PollOnceCreateEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateEndpoint(string, Endpoint, string, CallSettings)
    
    
    public virtual Operation<Endpoint, OperationMetadata> CreateEndpoint(string parent, Endpoint endpoint, string endpointId, CallSettings callSettings = null)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint's parent.  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)`  
Required. The endpoint to create.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint identifier. This will be part of the endpoint's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. Values that do not match this pattern will trigger an INVALID_ARGUMENT error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Endpoint endpoint = new Endpoint();
    string endpointId = "";
    // Make the request
    Operation<Endpoint, OperationMetadata> response = iDSClient.CreateEndpoint(parent, endpoint, endpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = iDSClient.PollOnceCreateEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateEndpointAsync(LocationName, Endpoint, string, CallSettings)
    
    
    public virtual Task<Operation<Endpoint, OperationMetadata>> CreateEndpointAsync(LocationName parent, Endpoint endpoint, string endpointId, CallSettings callSettings = null)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The endpoint's parent.  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)`  
Required. The endpoint to create.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint identifier. This will be part of the endpoint's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. Values that do not match this pattern will trigger an INVALID_ARGUMENT error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Endpoint endpoint = new Endpoint();
    string endpointId = "";
    // Make the request
    Operation<Endpoint, OperationMetadata> response = await iDSClient.CreateEndpointAsync(parent, endpoint, endpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = await iDSClient.PollOnceCreateEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateEndpointAsync(LocationName, Endpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<Endpoint, OperationMetadata>> CreateEndpointAsync(LocationName parent, Endpoint endpoint, string endpointId, CancellationToken cancellationToken)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The endpoint's parent.  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)`  
Required. The endpoint to create.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint identifier. This will be part of the endpoint's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. Values that do not match this pattern will trigger an INVALID_ARGUMENT error.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Endpoint endpoint = new Endpoint();
    string endpointId = "";
    // Make the request
    Operation<Endpoint, OperationMetadata> response = await iDSClient.CreateEndpointAsync(parent, endpoint, endpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = await iDSClient.PollOnceCreateEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateEndpointAsync(CreateEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<Endpoint, OperationMetadata>> CreateEndpointAsync(CreateEndpointRequest request, CallSettings callSettings = null)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.CreateEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    CreateEndpointRequest request = new CreateEndpointRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        EndpointId = "",
        Endpoint = new Endpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<Endpoint, OperationMetadata> response = await iDSClient.CreateEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = await iDSClient.PollOnceCreateEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateEndpointAsync(CreateEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<Endpoint, OperationMetadata>> CreateEndpointAsync(CreateEndpointRequest request, CancellationToken cancellationToken)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.CreateEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    CreateEndpointRequest request = new CreateEndpointRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        EndpointId = "",
        Endpoint = new Endpoint(),
        RequestId = "",
    };
    // Make the request
    Operation<Endpoint, OperationMetadata> response = await iDSClient.CreateEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = await iDSClient.PollOnceCreateEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateEndpointAsync(string, Endpoint, string, CallSettings)
    
    
    public virtual Task<Operation<Endpoint, OperationMetadata>> CreateEndpointAsync(string parent, Endpoint endpoint, string endpointId, CallSettings callSettings = null)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint's parent.  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)`  
Required. The endpoint to create.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint identifier. This will be part of the endpoint's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. Values that do not match this pattern will trigger an INVALID_ARGUMENT error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Endpoint endpoint = new Endpoint();
    string endpointId = "";
    // Make the request
    Operation<Endpoint, OperationMetadata> response = await iDSClient.CreateEndpointAsync(parent, endpoint, endpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = await iDSClient.PollOnceCreateEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateEndpointAsync(string, Endpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<Endpoint, OperationMetadata>> CreateEndpointAsync(string parent, Endpoint endpoint, string endpointId, CancellationToken cancellationToken)

Creates a new Endpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint's parent.  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)`  
Required. The endpoint to create.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The endpoint identifier. This will be part of the endpoint's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. Values that do not match this pattern will trigger an INVALID_ARGUMENT error.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Endpoint endpoint = new Endpoint();
    string endpointId = "";
    // Make the request
    Operation<Endpoint, OperationMetadata> response = await iDSClient.CreateEndpointAsync(parent, endpoint, endpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<Endpoint, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Endpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Endpoint, OperationMetadata> retrievedResponse = await iDSClient.PollOnceCreateEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Endpoint retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpoint(DeleteEndpointRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteEndpoint(DeleteEndpointRequest request, CallSettings callSettings = null)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.DeleteEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    DeleteEndpointRequest request = new DeleteEndpointRequest
    {
        EndpointName = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = iDSClient.DeleteEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = iDSClient.PollOnceDeleteEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpoint(EndpointName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteEndpoint(EndpointName name, CallSettings callSettings = null)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.EndpointName)`  
Required. The name of the endpoint to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    EndpointName name = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = iDSClient.DeleteEndpoint(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = iDSClient.PollOnceDeleteEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpoint(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteEndpoint(string name, CallSettings callSettings = null)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the endpoint to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/endpoints/[ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = iDSClient.DeleteEndpoint(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = iDSClient.PollOnceDeleteEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpointAsync(DeleteEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEndpointAsync(DeleteEndpointRequest request, CallSettings callSettings = null)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.DeleteEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    DeleteEndpointRequest request = new DeleteEndpointRequest
    {
        EndpointName = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await iDSClient.DeleteEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await iDSClient.PollOnceDeleteEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpointAsync(DeleteEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEndpointAsync(DeleteEndpointRequest request, CancellationToken cancellationToken)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.DeleteEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    DeleteEndpointRequest request = new DeleteEndpointRequest
    {
        EndpointName = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await iDSClient.DeleteEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await iDSClient.PollOnceDeleteEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpointAsync(EndpointName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEndpointAsync(EndpointName name, CallSettings callSettings = null)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.EndpointName)`  
Required. The name of the endpoint to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    EndpointName name = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await iDSClient.DeleteEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await iDSClient.PollOnceDeleteEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpointAsync(EndpointName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEndpointAsync(EndpointName name, CancellationToken cancellationToken)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.EndpointName)`  
Required. The name of the endpoint to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    EndpointName name = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await iDSClient.DeleteEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await iDSClient.PollOnceDeleteEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEndpointAsync(string name, CallSettings callSettings = null)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the endpoint to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/endpoints/[ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await iDSClient.DeleteEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await iDSClient.PollOnceDeleteEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEndpointAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEndpointAsync(string name, CancellationToken cancellationToken)

Deletes a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the endpoint to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/endpoints/[ENDPOINT]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await iDSClient.DeleteEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await iDSClient.PollOnceDeleteEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetEndpoint(EndpointName, CallSettings)
    
    
    public virtual Endpoint GetEndpoint(EndpointName name, CallSettings callSettings = null)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.EndpointName)`  
Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    EndpointName name = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
    // Make the request
    Endpoint response = iDSClient.GetEndpoint(name);
    

### GetEndpoint(GetEndpointRequest, CallSettings)
    
    
    public virtual Endpoint GetEndpoint(GetEndpointRequest request, CallSettings callSettings = null)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.GetEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    GetEndpointRequest request = new GetEndpointRequest
    {
        EndpointName = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]"),
    };
    // Make the request
    Endpoint response = iDSClient.GetEndpoint(request);
    

### GetEndpoint(string, CallSettings)
    
    
    public virtual Endpoint GetEndpoint(string name, CallSettings callSettings = null)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/endpoints/[ENDPOINT]";
    // Make the request
    Endpoint response = iDSClient.GetEndpoint(name);
    

### GetEndpointAsync(EndpointName, CallSettings)
    
    
    public virtual Task<Endpoint> GetEndpointAsync(EndpointName name, CallSettings callSettings = null)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.EndpointName)`  
Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    EndpointName name = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
    // Make the request
    Endpoint response = await iDSClient.GetEndpointAsync(name);
    

### GetEndpointAsync(EndpointName, CancellationToken)
    
    
    public virtual Task<Endpoint> GetEndpointAsync(EndpointName name, CancellationToken cancellationToken)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.EndpointName)`  
Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    EndpointName name = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
    // Make the request
    Endpoint response = await iDSClient.GetEndpointAsync(name);
    

### GetEndpointAsync(GetEndpointRequest, CallSettings)
    
    
    public virtual Task<Endpoint> GetEndpointAsync(GetEndpointRequest request, CallSettings callSettings = null)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.GetEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    GetEndpointRequest request = new GetEndpointRequest
    {
        EndpointName = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]"),
    };
    // Make the request
    Endpoint response = await iDSClient.GetEndpointAsync(request);
    

### GetEndpointAsync(GetEndpointRequest, CancellationToken)
    
    
    public virtual Task<Endpoint> GetEndpointAsync(GetEndpointRequest request, CancellationToken cancellationToken)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.GetEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    GetEndpointRequest request = new GetEndpointRequest
    {
        EndpointName = EndpointName.FromProjectLocationEndpoint("[PROJECT]", "[LOCATION]", "[ENDPOINT]"),
    };
    // Make the request
    Endpoint response = await iDSClient.GetEndpointAsync(request);
    

### GetEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Endpoint> GetEndpointAsync(string name, CallSettings callSettings = null)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/endpoints/[ENDPOINT]";
    // Make the request
    Endpoint response = await iDSClient.GetEndpointAsync(name);
    

### GetEndpointAsync(string, CancellationToken)
    
    
    public virtual Task<Endpoint> GetEndpointAsync(string name, CancellationToken cancellationToken)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/endpoints/[ENDPOINT]";
    // Make the request
    Endpoint response = await iDSClient.GetEndpointAsync(name);
    

### ListEndpoints(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListEndpointsResponse, Endpoint> ListEndpoints(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent, which owns this collection of endpoints.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.ListEndpointsResponse)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A pageable sequence of [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint) resources.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListEndpointsResponse, Endpoint> response = iDSClient.ListEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Endpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Endpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Endpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Endpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEndpoints(ListEndpointsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListEndpointsResponse, Endpoint> ListEndpoints(ListEndpointsRequest request, CallSettings callSettings = null)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.ListEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.ListEndpointsResponse)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A pageable sequence of [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint) resources.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    ListEndpointsRequest request = new ListEndpointsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListEndpointsResponse, Endpoint> response = iDSClient.ListEndpoints(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Endpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Endpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Endpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Endpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEndpoints(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListEndpointsResponse, Endpoint> ListEndpoints(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of endpoints.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.ListEndpointsResponse)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A pageable sequence of [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint) resources.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = IDSClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListEndpointsResponse, Endpoint> response = iDSClient.ListEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Endpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Endpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Endpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Endpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEndpointsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEndpointsResponse, Endpoint> ListEndpointsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent, which owns this collection of endpoints.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.ListEndpointsResponse)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A pageable asynchronous sequence of [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint) resources.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListEndpointsResponse, Endpoint> response = iDSClient.ListEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Endpoint item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListEndpointsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Endpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Endpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Endpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEndpointsAsync(ListEndpointsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEndpointsResponse, Endpoint> ListEndpointsAsync(ListEndpointsRequest request, CallSettings callSettings = null)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.ListEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.ListEndpointsResponse)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A pageable asynchronous sequence of [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint) resources.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    ListEndpointsRequest request = new ListEndpointsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListEndpointsResponse, Endpoint> response = iDSClient.ListEndpointsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Endpoint item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListEndpointsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Endpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Endpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Endpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEndpointsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEndpointsResponse, Endpoint> ListEndpointsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of endpoints.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.ListEndpointsResponse)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)` | A pageable asynchronous sequence of [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint) resources.  
**Example**
    
    
    // Create client
    IDSClient iDSClient = await IDSClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListEndpointsResponse, Endpoint> response = iDSClient.ListEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Endpoint item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListEndpointsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Endpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Endpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Endpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateEndpoint(string, CallSettings)
    
    
    public virtual Operation<Endpoint, OperationMetadata> PollOnceCreateEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateEndpoint`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Endpoint, OperationMetadata>> PollOnceCreateEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.Endpoint)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteEndpoint(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteEndpoint`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient#Google_Cloud_Ids_V1_IDSClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient#Google_Cloud_Ids_V1_IDSClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient#Google_Cloud_Ids_V1_IDSClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ids.V1/latest/Google.Cloud.Ids.V1.IDSClient#Google_Cloud_Ids_V1_IDSClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
