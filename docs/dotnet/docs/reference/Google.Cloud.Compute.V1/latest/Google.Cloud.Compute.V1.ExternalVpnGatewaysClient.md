---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient
title: Compute Engine v1 API - Class ExternalVpnGatewaysClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:55.203534+00:00
---

# Compute Engine v1 API - Class ExternalVpnGatewaysClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class ExternalVpnGatewaysClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class ExternalVpnGatewaysClient

Reference documentation and code samples for the Compute Engine v1 API class ExternalVpnGatewaysClient.

ExternalVpnGateways client wrapper, for convenient use. This client implements API version 2026-09-01.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExternalVpnGatewaysClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ExternalVpnGatewaysClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClientImpl)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Remarks

The ExternalVpnGateways API.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ExternalVpnGateways service, which is a host of "compute.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ExternalVpnGateways scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ExternalVpnGateways scopes are:

  * <https://www.googleapis.com/auth/compute>
  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteOperationsClient
    
    
    public virtual OperationsClient DeleteOperationsClient { get; }

The long-running operations client for `Delete`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ExternalVpnGateways.ExternalVpnGatewaysClient GrpcClient { get; }

The underlying gRPC ExternalVpnGateways client

**Property Value**  
---  
**Type** | **Description**  
`[ExternalVpnGateways](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateways)[ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateways.ExternalVpnGatewaysClient)` |   
  
### InsertOperationsClient
    
    
    public virtual OperationsClient InsertOperationsClient { get; }

The long-running operations client for `Insert`.

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
  
### SetLabelsOperationsClient
    
    
    public virtual OperationsClient SetLabelsOperationsClient { get; }

The long-running operations client for `SetLabels`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static ExternalVpnGatewaysClient Create()

Synchronously creates a [ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ExternalVpnGatewaysClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient)` | The created [ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ExternalVpnGatewaysClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ExternalVpnGatewaysClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient)` | The task representing the created [ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient).  
  
### Delete(DeleteExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Delete(DeleteExternalVpnGatewayRequest request, CallSettings callSettings = null)

Deletes the specified externalVpnGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    DeleteExternalVpnGatewayRequest request = new DeleteExternalVpnGatewayRequest
    {
        RequestId = "",
        ExternalVpnGateway = "",
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = externalVpnGatewaysClient.Delete(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = externalVpnGatewaysClient.PollOnceDelete(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Delete(string, string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Delete(string project, string externalVpnGateway, CallSettings callSettings = null)

Deletes the specified externalVpnGateway.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGateway` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the externalVpnGateways to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    string project = "";
    string externalVpnGateway = "";
    // Make the request
    lro::Operation<Operation, Operation> response = externalVpnGatewaysClient.Delete(project, externalVpnGateway);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = externalVpnGatewaysClient.PollOnceDelete(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(DeleteExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(DeleteExternalVpnGatewayRequest request, CallSettings callSettings = null)

Deletes the specified externalVpnGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    DeleteExternalVpnGatewayRequest request = new DeleteExternalVpnGatewayRequest
    {
        RequestId = "",
        ExternalVpnGateway = "",
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.DeleteAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(DeleteExternalVpnGatewayRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(DeleteExternalVpnGatewayRequest request, CancellationToken cancellationToken)

Deletes the specified externalVpnGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    DeleteExternalVpnGatewayRequest request = new DeleteExternalVpnGatewayRequest
    {
        RequestId = "",
        ExternalVpnGateway = "",
        Project = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.DeleteAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(string, string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(string project, string externalVpnGateway, CallSettings callSettings = null)

Deletes the specified externalVpnGateway.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGateway` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the externalVpnGateways to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string externalVpnGateway = "";
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.DeleteAsync(project, externalVpnGateway);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(string, string, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(string project, string externalVpnGateway, CancellationToken cancellationToken)

Deletes the specified externalVpnGateway.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGateway` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the externalVpnGateways to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string externalVpnGateway = "";
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.DeleteAsync(project, externalVpnGateway);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Get(GetExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual ExternalVpnGateway Get(GetExternalVpnGatewayRequest request, CallSettings callSettings = null)

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    GetExternalVpnGatewayRequest request = new GetExternalVpnGatewayRequest
    {
        ExternalVpnGateway = "",
        Project = "",
    };
    // Make the request
    ExternalVpnGateway response = externalVpnGatewaysClient.Get(request);
    

### Get(string, string, CallSettings)
    
    
    public virtual ExternalVpnGateway Get(string project, string externalVpnGateway, CallSettings callSettings = null)

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGateway` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the externalVpnGateway to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    string project = "";
    string externalVpnGateway = "";
    // Make the request
    ExternalVpnGateway response = externalVpnGatewaysClient.Get(project, externalVpnGateway);
    

### GetAsync(GetExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual Task<ExternalVpnGateway> GetAsync(GetExternalVpnGatewayRequest request, CallSettings callSettings = null)

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    GetExternalVpnGatewayRequest request = new GetExternalVpnGatewayRequest
    {
        ExternalVpnGateway = "",
        Project = "",
    };
    // Make the request
    ExternalVpnGateway response = await externalVpnGatewaysClient.GetAsync(request);
    

### GetAsync(GetExternalVpnGatewayRequest, CancellationToken)
    
    
    public virtual Task<ExternalVpnGateway> GetAsync(GetExternalVpnGatewayRequest request, CancellationToken cancellationToken)

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    GetExternalVpnGatewayRequest request = new GetExternalVpnGatewayRequest
    {
        ExternalVpnGateway = "",
        Project = "",
    };
    // Make the request
    ExternalVpnGateway response = await externalVpnGatewaysClient.GetAsync(request);
    

### GetAsync(string, string, CallSettings)
    
    
    public virtual Task<ExternalVpnGateway> GetAsync(string project, string externalVpnGateway, CallSettings callSettings = null)

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGateway` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the externalVpnGateway to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string externalVpnGateway = "";
    // Make the request
    ExternalVpnGateway response = await externalVpnGatewaysClient.GetAsync(project, externalVpnGateway);
    

### GetAsync(string, string, CancellationToken)
    
    
    public virtual Task<ExternalVpnGateway> GetAsync(string project, string externalVpnGateway, CancellationToken cancellationToken)

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGateway` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the externalVpnGateway to return.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string externalVpnGateway = "";
    // Make the request
    ExternalVpnGateway response = await externalVpnGatewaysClient.GetAsync(project, externalVpnGateway);
    

### Insert(InsertExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Insert(InsertExternalVpnGatewayRequest request, CallSettings callSettings = null)

Creates a ExternalVpnGateway in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    InsertExternalVpnGatewayRequest request = new InsertExternalVpnGatewayRequest
    {
        RequestId = "",
        Project = "",
        ExternalVpnGatewayResource = new ExternalVpnGateway(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = externalVpnGatewaysClient.Insert(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = externalVpnGatewaysClient.PollOnceInsert(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Insert(string, ExternalVpnGateway, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Insert(string project, ExternalVpnGateway externalVpnGatewayResource, CallSettings callSettings = null)

Creates a ExternalVpnGateway in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGatewayResource` | `[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    string project = "";
    ExternalVpnGateway externalVpnGatewayResource = new ExternalVpnGateway();
    // Make the request
    lro::Operation<Operation, Operation> response = externalVpnGatewaysClient.Insert(project, externalVpnGatewayResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = externalVpnGatewaysClient.PollOnceInsert(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(InsertExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(InsertExternalVpnGatewayRequest request, CallSettings callSettings = null)

Creates a ExternalVpnGateway in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    InsertExternalVpnGatewayRequest request = new InsertExternalVpnGatewayRequest
    {
        RequestId = "",
        Project = "",
        ExternalVpnGatewayResource = new ExternalVpnGateway(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.InsertAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(InsertExternalVpnGatewayRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(InsertExternalVpnGatewayRequest request, CancellationToken cancellationToken)

Creates a ExternalVpnGateway in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    InsertExternalVpnGatewayRequest request = new InsertExternalVpnGatewayRequest
    {
        RequestId = "",
        Project = "",
        ExternalVpnGatewayResource = new ExternalVpnGateway(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.InsertAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(string, ExternalVpnGateway, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(string project, ExternalVpnGateway externalVpnGatewayResource, CallSettings callSettings = null)

Creates a ExternalVpnGateway in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGatewayResource` | `[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    ExternalVpnGateway externalVpnGatewayResource = new ExternalVpnGateway();
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.InsertAsync(project, externalVpnGatewayResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(string, ExternalVpnGateway, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(string project, ExternalVpnGateway externalVpnGatewayResource, CancellationToken cancellationToken)

Creates a ExternalVpnGateway in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`externalVpnGatewayResource` | `[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    ExternalVpnGateway externalVpnGatewayResource = new ExternalVpnGateway();
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.InsertAsync(project, externalVpnGatewayResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### List(ListExternalVpnGatewaysRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ExternalVpnGatewayList, ExternalVpnGateway> List(ListExternalVpnGatewaysRequest request, CallSettings callSettings = null)

Retrieves the list of ExternalVpnGateway available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExternalVpnGatewaysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListExternalVpnGatewaysRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ExternalVpnGatewayList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewayList)[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | A pageable sequence of [ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway) resources.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    ListExternalVpnGatewaysRequest request = new ListExternalVpnGatewaysRequest
    {
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ExternalVpnGatewayList, ExternalVpnGateway> response = externalVpnGatewaysClient.List(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ExternalVpnGateway item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ExternalVpnGatewayList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExternalVpnGateway item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExternalVpnGateway> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExternalVpnGateway item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### List(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ExternalVpnGatewayList, ExternalVpnGateway> List(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the list of ExternalVpnGateway available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ExternalVpnGatewayList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewayList)[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | A pageable sequence of [ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway) resources.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedEnumerable<ExternalVpnGatewayList, ExternalVpnGateway> response = externalVpnGatewaysClient.List(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ExternalVpnGateway item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ExternalVpnGatewayList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExternalVpnGateway item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExternalVpnGateway> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExternalVpnGateway item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(ListExternalVpnGatewaysRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ExternalVpnGatewayList, ExternalVpnGateway> ListAsync(ListExternalVpnGatewaysRequest request, CallSettings callSettings = null)

Retrieves the list of ExternalVpnGateway available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExternalVpnGatewaysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListExternalVpnGatewaysRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ExternalVpnGatewayList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewayList)[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | A pageable asynchronous sequence of [ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway) resources.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    ListExternalVpnGatewaysRequest request = new ListExternalVpnGatewaysRequest
    {
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ExternalVpnGatewayList, ExternalVpnGateway> response = externalVpnGatewaysClient.ListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ExternalVpnGateway item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ExternalVpnGatewayList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExternalVpnGateway item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExternalVpnGateway> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExternalVpnGateway item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ExternalVpnGatewayList, ExternalVpnGateway> ListAsync(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the list of ExternalVpnGateway available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ExternalVpnGatewayList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewayList)[ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway)` | A pageable asynchronous sequence of [ExternalVpnGateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGateway) resources.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedAsyncEnumerable<ExternalVpnGatewayList, ExternalVpnGateway> response = externalVpnGatewaysClient.ListAsync(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ExternalVpnGateway item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ExternalVpnGatewayList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ExternalVpnGateway item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ExternalVpnGateway> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ExternalVpnGateway item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceDelete(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceDelete(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Delete`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOnceDeleteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceDeleteAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Delete` .

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### PollOnceInsert(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceInsert(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Insert`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOnceInsertAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceInsertAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Insert` .

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### PollOnceSetLabels(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceSetLabels(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `SetLabels`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOnceSetLabelsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceSetLabelsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `SetLabels`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### SetLabels(SetLabelsExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> SetLabels(SetLabelsExternalVpnGatewayRequest request, CallSettings callSettings = null)

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLabelsExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetLabelsExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    SetLabelsExternalVpnGatewayRequest request = new SetLabelsExternalVpnGatewayRequest
    {
        Resource = "",
        Project = "",
        GlobalSetLabelsRequestResource = new GlobalSetLabelsRequest(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = externalVpnGatewaysClient.SetLabels(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = externalVpnGatewaysClient.PollOnceSetLabels(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabels(string, string, GlobalSetLabelsRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> SetLabels(string project, string resource, GlobalSetLabelsRequest globalSetLabelsRequestResource, CallSettings callSettings = null)

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`globalSetLabelsRequestResource` | `[GlobalSetLabelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalSetLabelsRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    string project = "";
    string resource = "";
    GlobalSetLabelsRequest globalSetLabelsRequestResource = new GlobalSetLabelsRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = externalVpnGatewaysClient.SetLabels(project, resource, globalSetLabelsRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = externalVpnGatewaysClient.PollOnceSetLabels(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabelsAsync(SetLabelsExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> SetLabelsAsync(SetLabelsExternalVpnGatewayRequest request, CallSettings callSettings = null)

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLabelsExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetLabelsExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    SetLabelsExternalVpnGatewayRequest request = new SetLabelsExternalVpnGatewayRequest
    {
        Resource = "",
        Project = "",
        GlobalSetLabelsRequestResource = new GlobalSetLabelsRequest(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.SetLabelsAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceSetLabelsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabelsAsync(SetLabelsExternalVpnGatewayRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> SetLabelsAsync(SetLabelsExternalVpnGatewayRequest request, CancellationToken cancellationToken)

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLabelsExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetLabelsExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    SetLabelsExternalVpnGatewayRequest request = new SetLabelsExternalVpnGatewayRequest
    {
        Resource = "",
        Project = "",
        GlobalSetLabelsRequestResource = new GlobalSetLabelsRequest(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.SetLabelsAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceSetLabelsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabelsAsync(string, string, GlobalSetLabelsRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> SetLabelsAsync(string project, string resource, GlobalSetLabelsRequest globalSetLabelsRequestResource, CallSettings callSettings = null)

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`globalSetLabelsRequestResource` | `[GlobalSetLabelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalSetLabelsRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string resource = "";
    GlobalSetLabelsRequest globalSetLabelsRequestResource = new GlobalSetLabelsRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.SetLabelsAsync(project, resource, globalSetLabelsRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceSetLabelsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabelsAsync(string, string, GlobalSetLabelsRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> SetLabelsAsync(string project, string resource, GlobalSetLabelsRequest globalSetLabelsRequestResource, CancellationToken cancellationToken)

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`globalSetLabelsRequestResource` | `[GlobalSetLabelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalSetLabelsRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string resource = "";
    GlobalSetLabelsRequest globalSetLabelsRequestResource = new GlobalSetLabelsRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = await externalVpnGatewaysClient.SetLabelsAsync(project, resource, globalSetLabelsRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await externalVpnGatewaysClient.PollOnceSetLabelsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient#Google_Cloud_Compute_V1_ExternalVpnGatewaysClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient#Google_Cloud_Compute_V1_ExternalVpnGatewaysClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient#Google_Cloud_Compute_V1_ExternalVpnGatewaysClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient#Google_Cloud_Compute_V1_ExternalVpnGatewaysClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TestIamPermissions(TestIamPermissionsExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(TestIamPermissionsExternalVpnGatewayRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    TestIamPermissionsExternalVpnGatewayRequest request = new TestIamPermissionsExternalVpnGatewayRequest
    {
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = externalVpnGatewaysClient.TestIamPermissions(request);
    

### TestIamPermissions(string, string, TestPermissionsRequest, CallSettings)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(string project, string resource, TestPermissionsRequest testPermissionsRequestResource, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.Create();
    // Initialize request argument(s)
    string project = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = externalVpnGatewaysClient.TestIamPermissions(project, resource, testPermissionsRequestResource);
    

### TestIamPermissionsAsync(TestIamPermissionsExternalVpnGatewayRequest, CallSettings)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsExternalVpnGatewayRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsExternalVpnGatewayRequest request = new TestIamPermissionsExternalVpnGatewayRequest
    {
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = await externalVpnGatewaysClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(TestIamPermissionsExternalVpnGatewayRequest, CancellationToken)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsExternalVpnGatewayRequest request, CancellationToken cancellationToken)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsExternalVpnGatewayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsExternalVpnGatewayRequest request = new TestIamPermissionsExternalVpnGatewayRequest
    {
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = await externalVpnGatewaysClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(string, string, TestPermissionsRequest, CallSettings)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(string project, string resource, TestPermissionsRequest testPermissionsRequestResource, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = await externalVpnGatewaysClient.TestIamPermissionsAsync(project, resource, testPermissionsRequestResource);
    

### TestIamPermissionsAsync(string, string, TestPermissionsRequest, CancellationToken)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(string project, string resource, TestPermissionsRequest testPermissionsRequestResource, CancellationToken cancellationToken)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ExternalVpnGatewaysClient externalVpnGatewaysClient = await ExternalVpnGatewaysClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = await externalVpnGatewaysClient.TestIamPermissionsAsync(project, resource, testPermissionsRequestResource);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
