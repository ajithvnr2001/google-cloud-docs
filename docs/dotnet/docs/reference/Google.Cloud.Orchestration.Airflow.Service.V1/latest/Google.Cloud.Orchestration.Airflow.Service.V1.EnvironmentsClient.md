---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient
title: Cloud Composer v1 API - Class EnvironmentsClient (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:23.340028+00:00
---

# Cloud Composer v1 API - Class EnvironmentsClient (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Composer v1 API - Class EnvironmentsClient (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.9.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.8.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.7.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.6.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.5.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.4.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.3.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.2.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.1.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.0.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/1.0.0/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)


    
    
    public abstract class EnvironmentsClient

Reference documentation and code samples for the Cloud Composer v1 API class EnvironmentsClient.

Environments client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EnvironmentsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[EnvironmentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClientImpl)

## Namespace

[Google.Cloud.Orchestration.Airflow.Service.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1)

## Assembly

Google.Cloud.Orchestration.Airflow.Service.V1.dll

## Remarks

Managed Apache Airflow Environments.

## Properties 

### CheckUpgradeOperationsClient
    
    
    public virtual OperationsClient CheckUpgradeOperationsClient { get; }

The long-running operations client for `CheckUpgrade`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateEnvironmentOperationsClient
    
    
    public virtual OperationsClient CreateEnvironmentOperationsClient { get; }

The long-running operations client for `CreateEnvironment`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DatabaseFailoverOperationsClient
    
    
    public virtual OperationsClient DatabaseFailoverOperationsClient { get; }

The long-running operations client for `DatabaseFailover`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Environments service, which is a host of "composer.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Environments scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Environments scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteEnvironmentOperationsClient
    
    
    public virtual OperationsClient DeleteEnvironmentOperationsClient { get; }

The long-running operations client for `DeleteEnvironment`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual Environments.EnvironmentsClient GrpcClient { get; }

The underlying gRPC Environments client

**Property Value**  
---  
**Type** | **Description**  
`[Environments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environments)[EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsClient)` |   
  
### LoadSnapshotOperationsClient
    
    
    public virtual OperationsClient LoadSnapshotOperationsClient { get; }

The long-running operations client for `LoadSnapshot`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### SaveSnapshotOperationsClient
    
    
    public virtual OperationsClient SaveSnapshotOperationsClient { get; }

The long-running operations client for `SaveSnapshot`.

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
  
### UpdateEnvironmentOperationsClient
    
    
    public virtual OperationsClient UpdateEnvironmentOperationsClient { get; }

The long-running operations client for `UpdateEnvironment`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### CheckUpgrade(CheckUpgradeRequest, CallSettings)
    
    
    public virtual Operation<CheckUpgradeResponse, OperationMetadata> CheckUpgrade(CheckUpgradeRequest request, CallSettings callSettings = null)

Check if an upgrade operation on the environment will succeed.

In case of problems detailed info can be found in the returned Operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckUpgradeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CheckUpgradeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::CheckUpgradeRequest request = new gcoasv::CheckUpgradeRequest
    {
        Environment = "",
        ImageVersion = "",
    };
    // Make the request
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> response = environmentsClient.CheckUpgrade(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcoasv::CheckUpgradeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceCheckUpgrade(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::CheckUpgradeResponse retrievedResult = retrievedResponse.Result;
    }
    

### CheckUpgradeAsync(CheckUpgradeRequest, CallSettings)
    
    
    public virtual Task<Operation<CheckUpgradeResponse, OperationMetadata>> CheckUpgradeAsync(CheckUpgradeRequest request, CallSettings callSettings = null)

Check if an upgrade operation on the environment will succeed.

In case of problems detailed info can be found in the returned Operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckUpgradeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CheckUpgradeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::CheckUpgradeRequest request = new gcoasv::CheckUpgradeRequest
    {
        Environment = "",
        ImageVersion = "",
    };
    // Make the request
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> response = await environmentsClient.CheckUpgradeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::CheckUpgradeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceCheckUpgradeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::CheckUpgradeResponse retrievedResult = retrievedResponse.Result;
    }
    

### CheckUpgradeAsync(CheckUpgradeRequest, CancellationToken)
    
    
    public virtual Task<Operation<CheckUpgradeResponse, OperationMetadata>> CheckUpgradeAsync(CheckUpgradeRequest request, CancellationToken cancellationToken)

Check if an upgrade operation on the environment will succeed.

In case of problems detailed info can be found in the returned Operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckUpgradeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CheckUpgradeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::CheckUpgradeRequest request = new gcoasv::CheckUpgradeRequest
    {
        Environment = "",
        ImageVersion = "",
    };
    // Make the request
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> response = await environmentsClient.CheckUpgradeAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::CheckUpgradeResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::CheckUpgradeResponse, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceCheckUpgradeAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::CheckUpgradeResponse retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static EnvironmentsClient Create()

Synchronously creates a [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [EnvironmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)` | The created [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<EnvironmentsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [EnvironmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient)` | The task representing the created [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient).  
  
### CreateEnvironment(CreateEnvironmentRequest, CallSettings)
    
    
    public virtual Operation<Environment, OperationMetadata> CreateEnvironment(CreateEnvironmentRequest request, CallSettings callSettings = null)

Create a new environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::CreateEnvironmentRequest request = new gcoasv::CreateEnvironmentRequest
    {
        Parent = "",
        Environment = new gcoasv::Environment(),
    };
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = environmentsClient.CreateEnvironment(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceCreateEnvironment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### CreateEnvironment(string, Environment, CallSettings)
    
    
    public virtual Operation<Environment, OperationMetadata> CreateEnvironment(string parent, Environment environment, CallSettings callSettings = null)

Create a new environment.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The parent must be of the form "projects/{projectId}/locations/{locationId}".  
`environment` | `[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)`  
The environment to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string parent = "";
    gcoasv::Environment environment = new gcoasv::Environment();
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = environmentsClient.CreateEnvironment(parent, environment);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceCreateEnvironment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### CreateEnvironmentAsync(CreateEnvironmentRequest, CallSettings)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> CreateEnvironmentAsync(CreateEnvironmentRequest request, CallSettings callSettings = null)

Create a new environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::CreateEnvironmentRequest request = new gcoasv::CreateEnvironmentRequest
    {
        Parent = "",
        Environment = new gcoasv::Environment(),
    };
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = await environmentsClient.CreateEnvironmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceCreateEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### CreateEnvironmentAsync(CreateEnvironmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> CreateEnvironmentAsync(CreateEnvironmentRequest request, CancellationToken cancellationToken)

Create a new environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::CreateEnvironmentRequest request = new gcoasv::CreateEnvironmentRequest
    {
        Parent = "",
        Environment = new gcoasv::Environment(),
    };
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = await environmentsClient.CreateEnvironmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceCreateEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### CreateEnvironmentAsync(string, Environment, CallSettings)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> CreateEnvironmentAsync(string parent, Environment environment, CallSettings callSettings = null)

Create a new environment.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The parent must be of the form "projects/{projectId}/locations/{locationId}".  
`environment` | `[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)`  
The environment to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    gcoasv::Environment environment = new gcoasv::Environment();
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = await environmentsClient.CreateEnvironmentAsync(parent, environment);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceCreateEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### CreateEnvironmentAsync(string, Environment, CancellationToken)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> CreateEnvironmentAsync(string parent, Environment environment, CancellationToken cancellationToken)

Create a new environment.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The parent must be of the form "projects/{projectId}/locations/{locationId}".  
`environment` | `[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)`  
The environment to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    gcoasv::Environment environment = new gcoasv::Environment();
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = await environmentsClient.CreateEnvironmentAsync(parent, environment);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceCreateEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### CreateUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest, CallSettings)
    
    
    public virtual UserWorkloadsConfigMap CreateUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest request, CallSettings callSettings = null)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::CreateUserWorkloadsConfigMapRequest request = new gcoasv::CreateUserWorkloadsConfigMapRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
        UserWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap(),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = environmentsClient.CreateUserWorkloadsConfigMap(request);
    

### CreateUserWorkloadsConfigMap(EnvironmentName, UserWorkloadsConfigMap, CallSettings)
    
    
    public virtual UserWorkloadsConfigMap CreateUserWorkloadsConfigMap(EnvironmentName parent, UserWorkloadsConfigMap userWorkloadsConfigMap, CallSettings callSettings = null)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Required. User workloads ConfigMap to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = environmentsClient.CreateUserWorkloadsConfigMap(parent, userWorkloadsConfigMap);
    

### CreateUserWorkloadsConfigMap(string, UserWorkloadsConfigMap, CallSettings)
    
    
    public virtual UserWorkloadsConfigMap CreateUserWorkloadsConfigMap(string parent, UserWorkloadsConfigMap userWorkloadsConfigMap, CallSettings callSettings = null)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Required. User workloads ConfigMap to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = environmentsClient.CreateUserWorkloadsConfigMap(parent, userWorkloadsConfigMap);
    

### CreateUserWorkloadsConfigMapAsync(CreateUserWorkloadsConfigMapRequest, CallSettings)
    
    
    public virtual Task<UserWorkloadsConfigMap> CreateUserWorkloadsConfigMapAsync(CreateUserWorkloadsConfigMapRequest request, CallSettings callSettings = null)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::CreateUserWorkloadsConfigMapRequest request = new gcoasv::CreateUserWorkloadsConfigMapRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
        UserWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap(),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.CreateUserWorkloadsConfigMapAsync(request);
    

### CreateUserWorkloadsConfigMapAsync(CreateUserWorkloadsConfigMapRequest, CancellationToken)
    
    
    public virtual Task<UserWorkloadsConfigMap> CreateUserWorkloadsConfigMapAsync(CreateUserWorkloadsConfigMapRequest request, CancellationToken cancellationToken)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::CreateUserWorkloadsConfigMapRequest request = new gcoasv::CreateUserWorkloadsConfigMapRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
        UserWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap(),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.CreateUserWorkloadsConfigMapAsync(request);
    

### CreateUserWorkloadsConfigMapAsync(EnvironmentName, UserWorkloadsConfigMap, CallSettings)
    
    
    public virtual Task<UserWorkloadsConfigMap> CreateUserWorkloadsConfigMapAsync(EnvironmentName parent, UserWorkloadsConfigMap userWorkloadsConfigMap, CallSettings callSettings = null)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Required. User workloads ConfigMap to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.CreateUserWorkloadsConfigMapAsync(parent, userWorkloadsConfigMap);
    

### CreateUserWorkloadsConfigMapAsync(EnvironmentName, UserWorkloadsConfigMap, CancellationToken)
    
    
    public virtual Task<UserWorkloadsConfigMap> CreateUserWorkloadsConfigMapAsync(EnvironmentName parent, UserWorkloadsConfigMap userWorkloadsConfigMap, CancellationToken cancellationToken)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Required. User workloads ConfigMap to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.CreateUserWorkloadsConfigMapAsync(parent, userWorkloadsConfigMap);
    

### CreateUserWorkloadsConfigMapAsync(string, UserWorkloadsConfigMap, CallSettings)
    
    
    public virtual Task<UserWorkloadsConfigMap> CreateUserWorkloadsConfigMapAsync(string parent, UserWorkloadsConfigMap userWorkloadsConfigMap, CallSettings callSettings = null)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Required. User workloads ConfigMap to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.CreateUserWorkloadsConfigMapAsync(parent, userWorkloadsConfigMap);
    

### CreateUserWorkloadsConfigMapAsync(string, UserWorkloadsConfigMap, CancellationToken)
    
    
    public virtual Task<UserWorkloadsConfigMap> CreateUserWorkloadsConfigMapAsync(string parent, UserWorkloadsConfigMap userWorkloadsConfigMap, CancellationToken cancellationToken)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The environment name to create a ConfigMap for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Required. User workloads ConfigMap to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.CreateUserWorkloadsConfigMapAsync(parent, userWorkloadsConfigMap);
    

### CreateUserWorkloadsSecret(CreateUserWorkloadsSecretRequest, CallSettings)
    
    
    public virtual UserWorkloadsSecret CreateUserWorkloadsSecret(CreateUserWorkloadsSecretRequest request, CallSettings callSettings = null)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::CreateUserWorkloadsSecretRequest request = new gcoasv::CreateUserWorkloadsSecretRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
        UserWorkloadsSecret = new gcoasv::UserWorkloadsSecret(),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = environmentsClient.CreateUserWorkloadsSecret(request);
    

### CreateUserWorkloadsSecret(EnvironmentName, UserWorkloadsSecret, CallSettings)
    
    
    public virtual UserWorkloadsSecret CreateUserWorkloadsSecret(EnvironmentName parent, UserWorkloadsSecret userWorkloadsSecret, CallSettings callSettings = null)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Required. User workloads Secret to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = environmentsClient.CreateUserWorkloadsSecret(parent, userWorkloadsSecret);
    

### CreateUserWorkloadsSecret(string, UserWorkloadsSecret, CallSettings)
    
    
    public virtual UserWorkloadsSecret CreateUserWorkloadsSecret(string parent, UserWorkloadsSecret userWorkloadsSecret, CallSettings callSettings = null)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Required. User workloads Secret to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = environmentsClient.CreateUserWorkloadsSecret(parent, userWorkloadsSecret);
    

### CreateUserWorkloadsSecretAsync(CreateUserWorkloadsSecretRequest, CallSettings)
    
    
    public virtual Task<UserWorkloadsSecret> CreateUserWorkloadsSecretAsync(CreateUserWorkloadsSecretRequest request, CallSettings callSettings = null)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::CreateUserWorkloadsSecretRequest request = new gcoasv::CreateUserWorkloadsSecretRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
        UserWorkloadsSecret = new gcoasv::UserWorkloadsSecret(),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.CreateUserWorkloadsSecretAsync(request);
    

### CreateUserWorkloadsSecretAsync(CreateUserWorkloadsSecretRequest, CancellationToken)
    
    
    public virtual Task<UserWorkloadsSecret> CreateUserWorkloadsSecretAsync(CreateUserWorkloadsSecretRequest request, CancellationToken cancellationToken)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::CreateUserWorkloadsSecretRequest request = new gcoasv::CreateUserWorkloadsSecretRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
        UserWorkloadsSecret = new gcoasv::UserWorkloadsSecret(),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.CreateUserWorkloadsSecretAsync(request);
    

### CreateUserWorkloadsSecretAsync(EnvironmentName, UserWorkloadsSecret, CallSettings)
    
    
    public virtual Task<UserWorkloadsSecret> CreateUserWorkloadsSecretAsync(EnvironmentName parent, UserWorkloadsSecret userWorkloadsSecret, CallSettings callSettings = null)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Required. User workloads Secret to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.CreateUserWorkloadsSecretAsync(parent, userWorkloadsSecret);
    

### CreateUserWorkloadsSecretAsync(EnvironmentName, UserWorkloadsSecret, CancellationToken)
    
    
    public virtual Task<UserWorkloadsSecret> CreateUserWorkloadsSecretAsync(EnvironmentName parent, UserWorkloadsSecret userWorkloadsSecret, CancellationToken cancellationToken)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Required. User workloads Secret to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.CreateUserWorkloadsSecretAsync(parent, userWorkloadsSecret);
    

### CreateUserWorkloadsSecretAsync(string, UserWorkloadsSecret, CallSettings)
    
    
    public virtual Task<UserWorkloadsSecret> CreateUserWorkloadsSecretAsync(string parent, UserWorkloadsSecret userWorkloadsSecret, CallSettings callSettings = null)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Required. User workloads Secret to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.CreateUserWorkloadsSecretAsync(parent, userWorkloadsSecret);
    

### CreateUserWorkloadsSecretAsync(string, UserWorkloadsSecret, CancellationToken)
    
    
    public virtual Task<UserWorkloadsSecret> CreateUserWorkloadsSecretAsync(string parent, UserWorkloadsSecret userWorkloadsSecret, CancellationToken cancellationToken)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The environment name to create a Secret for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Required. User workloads Secret to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.CreateUserWorkloadsSecretAsync(parent, userWorkloadsSecret);
    

### DatabaseFailover(DatabaseFailoverRequest, CallSettings)
    
    
    public virtual Operation<DatabaseFailoverResponse, OperationMetadata> DatabaseFailover(DatabaseFailoverRequest request, CallSettings callSettings = null)

Triggers database failover (only for highly resilient environments).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DatabaseFailoverRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DatabaseFailoverResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::DatabaseFailoverRequest request = new gcoasv::DatabaseFailoverRequest { Environment = "", };
    // Make the request
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> response = environmentsClient.DatabaseFailover(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcoasv::DatabaseFailoverResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceDatabaseFailover(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::DatabaseFailoverResponse retrievedResult = retrievedResponse.Result;
    }
    

### DatabaseFailoverAsync(DatabaseFailoverRequest, CallSettings)
    
    
    public virtual Task<Operation<DatabaseFailoverResponse, OperationMetadata>> DatabaseFailoverAsync(DatabaseFailoverRequest request, CallSettings callSettings = null)

Triggers database failover (only for highly resilient environments).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DatabaseFailoverRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DatabaseFailoverResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::DatabaseFailoverRequest request = new gcoasv::DatabaseFailoverRequest { Environment = "", };
    // Make the request
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> response = await environmentsClient.DatabaseFailoverAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::DatabaseFailoverResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceDatabaseFailoverAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::DatabaseFailoverResponse retrievedResult = retrievedResponse.Result;
    }
    

### DatabaseFailoverAsync(DatabaseFailoverRequest, CancellationToken)
    
    
    public virtual Task<Operation<DatabaseFailoverResponse, OperationMetadata>> DatabaseFailoverAsync(DatabaseFailoverRequest request, CancellationToken cancellationToken)

Triggers database failover (only for highly resilient environments).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DatabaseFailoverRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DatabaseFailoverResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::DatabaseFailoverRequest request = new gcoasv::DatabaseFailoverRequest { Environment = "", };
    // Make the request
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> response = await environmentsClient.DatabaseFailoverAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::DatabaseFailoverResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::DatabaseFailoverResponse, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceDatabaseFailoverAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::DatabaseFailoverResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEnvironment(DeleteEnvironmentRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteEnvironment(DeleteEnvironmentRequest request, CallSettings callSettings = null)

Delete an environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::DeleteEnvironmentRequest request = new gcoasv::DeleteEnvironmentRequest { Name = "", };
    // Make the request
    Operation<Empty, gcoasv::OperationMetadata> response = environmentsClient.DeleteEnvironment(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceDeleteEnvironment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEnvironment(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteEnvironment(string name, CallSettings callSettings = null)

Delete an environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The environment to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcoasv::OperationMetadata> response = environmentsClient.DeleteEnvironment(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceDeleteEnvironment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEnvironmentAsync(DeleteEnvironmentRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEnvironmentAsync(DeleteEnvironmentRequest request, CallSettings callSettings = null)

Delete an environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::DeleteEnvironmentRequest request = new gcoasv::DeleteEnvironmentRequest { Name = "", };
    // Make the request
    Operation<Empty, gcoasv::OperationMetadata> response = await environmentsClient.DeleteEnvironmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceDeleteEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEnvironmentAsync(DeleteEnvironmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEnvironmentAsync(DeleteEnvironmentRequest request, CancellationToken cancellationToken)

Delete an environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::DeleteEnvironmentRequest request = new gcoasv::DeleteEnvironmentRequest { Name = "", };
    // Make the request
    Operation<Empty, gcoasv::OperationMetadata> response = await environmentsClient.DeleteEnvironmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceDeleteEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEnvironmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEnvironmentAsync(string name, CallSettings callSettings = null)

Delete an environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The environment to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcoasv::OperationMetadata> response = await environmentsClient.DeleteEnvironmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceDeleteEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteEnvironmentAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteEnvironmentAsync(string name, CancellationToken cancellationToken)

Delete an environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The environment to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcoasv::OperationMetadata> response = await environmentsClient.DeleteEnvironmentAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceDeleteEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest, CallSettings)
    
    
    public virtual void DeleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest request, CallSettings callSettings = null)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::DeleteUserWorkloadsConfigMapRequest request = new gcoasv::DeleteUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMapName = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]"),
    };
    // Make the request
    environmentsClient.DeleteUserWorkloadsConfigMap(request);
    

### DeleteUserWorkloadsConfigMap(UserWorkloadsConfigMapName, CallSettings)
    
    
    public virtual void DeleteUserWorkloadsConfigMap(UserWorkloadsConfigMapName name, CallSettings callSettings = null)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsConfigMapName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMapName)`  
Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMapName name = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]");
    // Make the request
    environmentsClient.DeleteUserWorkloadsConfigMap(name);
    

### DeleteUserWorkloadsConfigMap(string, CallSettings)
    
    
    public virtual void DeleteUserWorkloadsConfigMap(string name, CallSettings callSettings = null)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsConfigMaps/[USER_WORKLOADS_CONFIG_MAP]";
    // Make the request
    environmentsClient.DeleteUserWorkloadsConfigMap(name);
    

### DeleteUserWorkloadsConfigMapAsync(DeleteUserWorkloadsConfigMapRequest, CallSettings)
    
    
    public virtual Task DeleteUserWorkloadsConfigMapAsync(DeleteUserWorkloadsConfigMapRequest request, CallSettings callSettings = null)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::DeleteUserWorkloadsConfigMapRequest request = new gcoasv::DeleteUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMapName = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]"),
    };
    // Make the request
    await environmentsClient.DeleteUserWorkloadsConfigMapAsync(request);
    

### DeleteUserWorkloadsConfigMapAsync(DeleteUserWorkloadsConfigMapRequest, CancellationToken)
    
    
    public virtual Task DeleteUserWorkloadsConfigMapAsync(DeleteUserWorkloadsConfigMapRequest request, CancellationToken cancellationToken)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::DeleteUserWorkloadsConfigMapRequest request = new gcoasv::DeleteUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMapName = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]"),
    };
    // Make the request
    await environmentsClient.DeleteUserWorkloadsConfigMapAsync(request);
    

### DeleteUserWorkloadsConfigMapAsync(UserWorkloadsConfigMapName, CallSettings)
    
    
    public virtual Task DeleteUserWorkloadsConfigMapAsync(UserWorkloadsConfigMapName name, CallSettings callSettings = null)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsConfigMapName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMapName)`  
Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMapName name = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]");
    // Make the request
    await environmentsClient.DeleteUserWorkloadsConfigMapAsync(name);
    

### DeleteUserWorkloadsConfigMapAsync(UserWorkloadsConfigMapName, CancellationToken)
    
    
    public virtual Task DeleteUserWorkloadsConfigMapAsync(UserWorkloadsConfigMapName name, CancellationToken cancellationToken)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsConfigMapName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMapName)`  
Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMapName name = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]");
    // Make the request
    await environmentsClient.DeleteUserWorkloadsConfigMapAsync(name);
    

### DeleteUserWorkloadsConfigMapAsync(string, CallSettings)
    
    
    public virtual Task DeleteUserWorkloadsConfigMapAsync(string name, CallSettings callSettings = null)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsConfigMaps/[USER_WORKLOADS_CONFIG_MAP]";
    // Make the request
    await environmentsClient.DeleteUserWorkloadsConfigMapAsync(name);
    

### DeleteUserWorkloadsConfigMapAsync(string, CancellationToken)
    
    
    public virtual Task DeleteUserWorkloadsConfigMapAsync(string name, CancellationToken cancellationToken)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ConfigMap to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsConfigMaps/[USER_WORKLOADS_CONFIG_MAP]";
    // Make the request
    await environmentsClient.DeleteUserWorkloadsConfigMapAsync(name);
    

### DeleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest, CallSettings)
    
    
    public virtual void DeleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest request, CallSettings callSettings = null)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::DeleteUserWorkloadsSecretRequest request = new gcoasv::DeleteUserWorkloadsSecretRequest
    {
        UserWorkloadsSecretName = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]"),
    };
    // Make the request
    environmentsClient.DeleteUserWorkloadsSecret(request);
    

### DeleteUserWorkloadsSecret(UserWorkloadsSecretName, CallSettings)
    
    
    public virtual void DeleteUserWorkloadsSecret(UserWorkloadsSecretName name, CallSettings callSettings = null)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsSecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecretName)`  
Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecretName name = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]");
    // Make the request
    environmentsClient.DeleteUserWorkloadsSecret(name);
    

### DeleteUserWorkloadsSecret(string, CallSettings)
    
    
    public virtual void DeleteUserWorkloadsSecret(string name, CallSettings callSettings = null)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsSecrets/[USER_WORKLOADS_SECRET]";
    // Make the request
    environmentsClient.DeleteUserWorkloadsSecret(name);
    

### DeleteUserWorkloadsSecretAsync(DeleteUserWorkloadsSecretRequest, CallSettings)
    
    
    public virtual Task DeleteUserWorkloadsSecretAsync(DeleteUserWorkloadsSecretRequest request, CallSettings callSettings = null)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::DeleteUserWorkloadsSecretRequest request = new gcoasv::DeleteUserWorkloadsSecretRequest
    {
        UserWorkloadsSecretName = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]"),
    };
    // Make the request
    await environmentsClient.DeleteUserWorkloadsSecretAsync(request);
    

### DeleteUserWorkloadsSecretAsync(DeleteUserWorkloadsSecretRequest, CancellationToken)
    
    
    public virtual Task DeleteUserWorkloadsSecretAsync(DeleteUserWorkloadsSecretRequest request, CancellationToken cancellationToken)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::DeleteUserWorkloadsSecretRequest request = new gcoasv::DeleteUserWorkloadsSecretRequest
    {
        UserWorkloadsSecretName = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]"),
    };
    // Make the request
    await environmentsClient.DeleteUserWorkloadsSecretAsync(request);
    

### DeleteUserWorkloadsSecretAsync(UserWorkloadsSecretName, CallSettings)
    
    
    public virtual Task DeleteUserWorkloadsSecretAsync(UserWorkloadsSecretName name, CallSettings callSettings = null)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsSecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecretName)`  
Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecretName name = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]");
    // Make the request
    await environmentsClient.DeleteUserWorkloadsSecretAsync(name);
    

### DeleteUserWorkloadsSecretAsync(UserWorkloadsSecretName, CancellationToken)
    
    
    public virtual Task DeleteUserWorkloadsSecretAsync(UserWorkloadsSecretName name, CancellationToken cancellationToken)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsSecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecretName)`  
Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecretName name = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]");
    // Make the request
    await environmentsClient.DeleteUserWorkloadsSecretAsync(name);
    

### DeleteUserWorkloadsSecretAsync(string, CallSettings)
    
    
    public virtual Task DeleteUserWorkloadsSecretAsync(string name, CallSettings callSettings = null)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsSecrets/[USER_WORKLOADS_SECRET]";
    // Make the request
    await environmentsClient.DeleteUserWorkloadsSecretAsync(name);
    

### DeleteUserWorkloadsSecretAsync(string, CancellationToken)
    
    
    public virtual Task DeleteUserWorkloadsSecretAsync(string name, CancellationToken cancellationToken)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The Secret to delete, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsSecrets/[USER_WORKLOADS_SECRET]";
    // Make the request
    await environmentsClient.DeleteUserWorkloadsSecretAsync(name);
    

### ExecuteAirflowCommand(ExecuteAirflowCommandRequest, CallSettings)
    
    
    public virtual ExecuteAirflowCommandResponse ExecuteAirflowCommand(ExecuteAirflowCommandRequest request, CallSettings callSettings = null)

Executes Airflow CLI command.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ExecuteAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ExecuteAirflowCommandResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::ExecuteAirflowCommandRequest request = new gcoasv::ExecuteAirflowCommandRequest
    {
        Environment = "",
        Command = "",
        Subcommand = "",
        Parameters = { "", },
    };
    // Make the request
    gcoasv::ExecuteAirflowCommandResponse response = environmentsClient.ExecuteAirflowCommand(request);
    

### ExecuteAirflowCommandAsync(ExecuteAirflowCommandRequest, CallSettings)
    
    
    public virtual Task<ExecuteAirflowCommandResponse> ExecuteAirflowCommandAsync(ExecuteAirflowCommandRequest request, CallSettings callSettings = null)

Executes Airflow CLI command.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ExecuteAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ExecuteAirflowCommandResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::ExecuteAirflowCommandRequest request = new gcoasv::ExecuteAirflowCommandRequest
    {
        Environment = "",
        Command = "",
        Subcommand = "",
        Parameters = { "", },
    };
    // Make the request
    gcoasv::ExecuteAirflowCommandResponse response = await environmentsClient.ExecuteAirflowCommandAsync(request);
    

### ExecuteAirflowCommandAsync(ExecuteAirflowCommandRequest, CancellationToken)
    
    
    public virtual Task<ExecuteAirflowCommandResponse> ExecuteAirflowCommandAsync(ExecuteAirflowCommandRequest request, CancellationToken cancellationToken)

Executes Airflow CLI command.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ExecuteAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ExecuteAirflowCommandResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::ExecuteAirflowCommandRequest request = new gcoasv::ExecuteAirflowCommandRequest
    {
        Environment = "",
        Command = "",
        Subcommand = "",
        Parameters = { "", },
    };
    // Make the request
    gcoasv::ExecuteAirflowCommandResponse response = await environmentsClient.ExecuteAirflowCommandAsync(request);
    

### FetchDatabaseProperties(FetchDatabasePropertiesRequest, CallSettings)
    
    
    public virtual FetchDatabasePropertiesResponse FetchDatabaseProperties(FetchDatabasePropertiesRequest request, CallSettings callSettings = null)

Fetches database properties.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchDatabasePropertiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.FetchDatabasePropertiesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchDatabasePropertiesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.FetchDatabasePropertiesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::FetchDatabasePropertiesRequest request = new gcoasv::FetchDatabasePropertiesRequest
    {
        EnvironmentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
    };
    // Make the request
    gcoasv::FetchDatabasePropertiesResponse response = environmentsClient.FetchDatabaseProperties(request);
    

### FetchDatabasePropertiesAsync(FetchDatabasePropertiesRequest, CallSettings)
    
    
    public virtual Task<FetchDatabasePropertiesResponse> FetchDatabasePropertiesAsync(FetchDatabasePropertiesRequest request, CallSettings callSettings = null)

Fetches database properties.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchDatabasePropertiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.FetchDatabasePropertiesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FetchDatabasePropertiesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.FetchDatabasePropertiesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::FetchDatabasePropertiesRequest request = new gcoasv::FetchDatabasePropertiesRequest
    {
        EnvironmentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
    };
    // Make the request
    gcoasv::FetchDatabasePropertiesResponse response = await environmentsClient.FetchDatabasePropertiesAsync(request);
    

### FetchDatabasePropertiesAsync(FetchDatabasePropertiesRequest, CancellationToken)
    
    
    public virtual Task<FetchDatabasePropertiesResponse> FetchDatabasePropertiesAsync(FetchDatabasePropertiesRequest request, CancellationToken cancellationToken)

Fetches database properties.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchDatabasePropertiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.FetchDatabasePropertiesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FetchDatabasePropertiesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.FetchDatabasePropertiesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::FetchDatabasePropertiesRequest request = new gcoasv::FetchDatabasePropertiesRequest
    {
        EnvironmentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
    };
    // Make the request
    gcoasv::FetchDatabasePropertiesResponse response = await environmentsClient.FetchDatabasePropertiesAsync(request);
    

### GetEnvironment(GetEnvironmentRequest, CallSettings)
    
    
    public virtual Environment GetEnvironment(GetEnvironmentRequest request, CallSettings callSettings = null)

Get an existing environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::GetEnvironmentRequest request = new gcoasv::GetEnvironmentRequest { Name = "", };
    // Make the request
    gcoasv::Environment response = environmentsClient.GetEnvironment(request);
    

### GetEnvironment(string, CallSettings)
    
    
    public virtual Environment GetEnvironment(string name, CallSettings callSettings = null)

Get an existing environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name of the environment to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcoasv::Environment response = environmentsClient.GetEnvironment(name);
    

### GetEnvironmentAsync(GetEnvironmentRequest, CallSettings)
    
    
    public virtual Task<Environment> GetEnvironmentAsync(GetEnvironmentRequest request, CallSettings callSettings = null)

Get an existing environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::GetEnvironmentRequest request = new gcoasv::GetEnvironmentRequest { Name = "", };
    // Make the request
    gcoasv::Environment response = await environmentsClient.GetEnvironmentAsync(request);
    

### GetEnvironmentAsync(GetEnvironmentRequest, CancellationToken)
    
    
    public virtual Task<Environment> GetEnvironmentAsync(GetEnvironmentRequest request, CancellationToken cancellationToken)

Get an existing environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::GetEnvironmentRequest request = new gcoasv::GetEnvironmentRequest { Name = "", };
    // Make the request
    gcoasv::Environment response = await environmentsClient.GetEnvironmentAsync(request);
    

### GetEnvironmentAsync(string, CallSettings)
    
    
    public virtual Task<Environment> GetEnvironmentAsync(string name, CallSettings callSettings = null)

Get an existing environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name of the environment to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcoasv::Environment response = await environmentsClient.GetEnvironmentAsync(name);
    

### GetEnvironmentAsync(string, CancellationToken)
    
    
    public virtual Task<Environment> GetEnvironmentAsync(string name, CancellationToken cancellationToken)

Get an existing environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name of the environment to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcoasv::Environment response = await environmentsClient.GetEnvironmentAsync(name);
    

### GetUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest, CallSettings)
    
    
    public virtual UserWorkloadsConfigMap GetUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest request, CallSettings callSettings = null)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::GetUserWorkloadsConfigMapRequest request = new gcoasv::GetUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMapName = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]"),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = environmentsClient.GetUserWorkloadsConfigMap(request);
    

### GetUserWorkloadsConfigMap(UserWorkloadsConfigMapName, CallSettings)
    
    
    public virtual UserWorkloadsConfigMap GetUserWorkloadsConfigMap(UserWorkloadsConfigMapName name, CallSettings callSettings = null)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsConfigMapName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMapName)`  
Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMapName name = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]");
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = environmentsClient.GetUserWorkloadsConfigMap(name);
    

### GetUserWorkloadsConfigMap(string, CallSettings)
    
    
    public virtual UserWorkloadsConfigMap GetUserWorkloadsConfigMap(string name, CallSettings callSettings = null)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsConfigMaps/[USER_WORKLOADS_CONFIG_MAP]";
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = environmentsClient.GetUserWorkloadsConfigMap(name);
    

### GetUserWorkloadsConfigMapAsync(GetUserWorkloadsConfigMapRequest, CallSettings)
    
    
    public virtual Task<UserWorkloadsConfigMap> GetUserWorkloadsConfigMapAsync(GetUserWorkloadsConfigMapRequest request, CallSettings callSettings = null)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::GetUserWorkloadsConfigMapRequest request = new gcoasv::GetUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMapName = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]"),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.GetUserWorkloadsConfigMapAsync(request);
    

### GetUserWorkloadsConfigMapAsync(GetUserWorkloadsConfigMapRequest, CancellationToken)
    
    
    public virtual Task<UserWorkloadsConfigMap> GetUserWorkloadsConfigMapAsync(GetUserWorkloadsConfigMapRequest request, CancellationToken cancellationToken)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::GetUserWorkloadsConfigMapRequest request = new gcoasv::GetUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMapName = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]"),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.GetUserWorkloadsConfigMapAsync(request);
    

### GetUserWorkloadsConfigMapAsync(UserWorkloadsConfigMapName, CallSettings)
    
    
    public virtual Task<UserWorkloadsConfigMap> GetUserWorkloadsConfigMapAsync(UserWorkloadsConfigMapName name, CallSettings callSettings = null)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsConfigMapName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMapName)`  
Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMapName name = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]");
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.GetUserWorkloadsConfigMapAsync(name);
    

### GetUserWorkloadsConfigMapAsync(UserWorkloadsConfigMapName, CancellationToken)
    
    
    public virtual Task<UserWorkloadsConfigMap> GetUserWorkloadsConfigMapAsync(UserWorkloadsConfigMapName name, CancellationToken cancellationToken)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsConfigMapName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMapName)`  
Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMapName name = gcoasv::UserWorkloadsConfigMapName.FromProjectLocationEnvironmentUserWorkloadsConfigMap("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_CONFIG_MAP]");
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.GetUserWorkloadsConfigMapAsync(name);
    

### GetUserWorkloadsConfigMapAsync(string, CallSettings)
    
    
    public virtual Task<UserWorkloadsConfigMap> GetUserWorkloadsConfigMapAsync(string name, CallSettings callSettings = null)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsConfigMaps/[USER_WORKLOADS_CONFIG_MAP]";
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.GetUserWorkloadsConfigMapAsync(name);
    

### GetUserWorkloadsConfigMapAsync(string, CancellationToken)
    
    
    public virtual Task<UserWorkloadsConfigMap> GetUserWorkloadsConfigMapAsync(string name, CancellationToken cancellationToken)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the ConfigMap to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsConfigMaps/[USER_WORKLOADS_CONFIG_MAP]";
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.GetUserWorkloadsConfigMapAsync(name);
    

### GetUserWorkloadsSecret(GetUserWorkloadsSecretRequest, CallSettings)
    
    
    public virtual UserWorkloadsSecret GetUserWorkloadsSecret(GetUserWorkloadsSecretRequest request, CallSettings callSettings = null)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::GetUserWorkloadsSecretRequest request = new gcoasv::GetUserWorkloadsSecretRequest
    {
        UserWorkloadsSecretName = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]"),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = environmentsClient.GetUserWorkloadsSecret(request);
    

### GetUserWorkloadsSecret(UserWorkloadsSecretName, CallSettings)
    
    
    public virtual UserWorkloadsSecret GetUserWorkloadsSecret(UserWorkloadsSecretName name, CallSettings callSettings = null)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsSecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecretName)`  
Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecretName name = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]");
    // Make the request
    gcoasv::UserWorkloadsSecret response = environmentsClient.GetUserWorkloadsSecret(name);
    

### GetUserWorkloadsSecret(string, CallSettings)
    
    
    public virtual UserWorkloadsSecret GetUserWorkloadsSecret(string name, CallSettings callSettings = null)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsSecrets/[USER_WORKLOADS_SECRET]";
    // Make the request
    gcoasv::UserWorkloadsSecret response = environmentsClient.GetUserWorkloadsSecret(name);
    

### GetUserWorkloadsSecretAsync(GetUserWorkloadsSecretRequest, CallSettings)
    
    
    public virtual Task<UserWorkloadsSecret> GetUserWorkloadsSecretAsync(GetUserWorkloadsSecretRequest request, CallSettings callSettings = null)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::GetUserWorkloadsSecretRequest request = new gcoasv::GetUserWorkloadsSecretRequest
    {
        UserWorkloadsSecretName = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]"),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.GetUserWorkloadsSecretAsync(request);
    

### GetUserWorkloadsSecretAsync(GetUserWorkloadsSecretRequest, CancellationToken)
    
    
    public virtual Task<UserWorkloadsSecret> GetUserWorkloadsSecretAsync(GetUserWorkloadsSecretRequest request, CancellationToken cancellationToken)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::GetUserWorkloadsSecretRequest request = new gcoasv::GetUserWorkloadsSecretRequest
    {
        UserWorkloadsSecretName = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]"),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.GetUserWorkloadsSecretAsync(request);
    

### GetUserWorkloadsSecretAsync(UserWorkloadsSecretName, CallSettings)
    
    
    public virtual Task<UserWorkloadsSecret> GetUserWorkloadsSecretAsync(UserWorkloadsSecretName name, CallSettings callSettings = null)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsSecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecretName)`  
Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecretName name = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]");
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.GetUserWorkloadsSecretAsync(name);
    

### GetUserWorkloadsSecretAsync(UserWorkloadsSecretName, CancellationToken)
    
    
    public virtual Task<UserWorkloadsSecret> GetUserWorkloadsSecretAsync(UserWorkloadsSecretName name, CancellationToken cancellationToken)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[UserWorkloadsSecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecretName)`  
Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecretName name = gcoasv::UserWorkloadsSecretName.FromProjectLocationEnvironmentUserWorkloadsSecret("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]", "[USER_WORKLOADS_SECRET]");
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.GetUserWorkloadsSecretAsync(name);
    

### GetUserWorkloadsSecretAsync(string, CallSettings)
    
    
    public virtual Task<UserWorkloadsSecret> GetUserWorkloadsSecretAsync(string name, CallSettings callSettings = null)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsSecrets/[USER_WORKLOADS_SECRET]";
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.GetUserWorkloadsSecretAsync(name);
    

### GetUserWorkloadsSecretAsync(string, CancellationToken)
    
    
    public virtual Task<UserWorkloadsSecret> GetUserWorkloadsSecretAsync(string name, CancellationToken cancellationToken)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Secret to get, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}"  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]/userWorkloadsSecrets/[USER_WORKLOADS_SECRET]";
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.GetUserWorkloadsSecretAsync(name);
    

### ListEnvironments(ListEnvironmentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListEnvironmentsResponse, Environment> ListEnvironments(ListEnvironmentsRequest request, CallSettings callSettings = null)

List environments.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEnvironmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListEnvironmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListEnvironmentsResponse)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | A pageable sequence of [Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::ListEnvironmentsRequest request = new gcoasv::ListEnvironmentsRequest { Parent = "", };
    // Make the request
    PagedEnumerable<gcoasv::ListEnvironmentsResponse, gcoasv::Environment> response = environmentsClient.ListEnvironments(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::Environment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListEnvironmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::Environment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::Environment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::Environment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEnvironments(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListEnvironmentsResponse, Environment> ListEnvironments(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List environments.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
List environments in the given project and location, in the form: "projects/{projectId}/locations/{locationId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListEnvironmentsResponse)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | A pageable sequence of [Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<gcoasv::ListEnvironmentsResponse, gcoasv::Environment> response = environmentsClient.ListEnvironments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::Environment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListEnvironmentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::Environment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::Environment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::Environment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEnvironmentsAsync(ListEnvironmentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEnvironmentsResponse, Environment> ListEnvironmentsAsync(ListEnvironmentsRequest request, CallSettings callSettings = null)

List environments.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEnvironmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListEnvironmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListEnvironmentsResponse)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | A pageable asynchronous sequence of [Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::ListEnvironmentsRequest request = new gcoasv::ListEnvironmentsRequest { Parent = "", };
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListEnvironmentsResponse, gcoasv::Environment> response = environmentsClient.ListEnvironmentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::Environment item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListEnvironmentsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::Environment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::Environment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::Environment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEnvironmentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEnvironmentsResponse, Environment> ListEnvironmentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List environments.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
List environments in the given project and location, in the form: "projects/{projectId}/locations/{locationId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListEnvironmentsResponse)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | A pageable asynchronous sequence of [Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListEnvironmentsResponse, gcoasv::Environment> response = environmentsClient.ListEnvironmentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::Environment item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListEnvironmentsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::Environment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::Environment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::Environment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsConfigMaps(EnvironmentName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUserWorkloadsConfigMapsResponse, UserWorkloadsConfigMap> ListUserWorkloadsConfigMaps(EnvironmentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. List ConfigMaps in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsResponse)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A pageable sequence of [UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    // Make the request
    PagedEnumerable<gcoasv::ListUserWorkloadsConfigMapsResponse, gcoasv::UserWorkloadsConfigMap> response = environmentsClient.ListUserWorkloadsConfigMaps(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::UserWorkloadsConfigMap item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListUserWorkloadsConfigMapsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsConfigMap item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsConfigMap> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsConfigMap item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListUserWorkloadsConfigMapsResponse, UserWorkloadsConfigMap> ListUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest request, CallSettings callSettings = null)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsResponse)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A pageable sequence of [UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::ListUserWorkloadsConfigMapsRequest request = new gcoasv::ListUserWorkloadsConfigMapsRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
    };
    // Make the request
    PagedEnumerable<gcoasv::ListUserWorkloadsConfigMapsResponse, gcoasv::UserWorkloadsConfigMap> response = environmentsClient.ListUserWorkloadsConfigMaps(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::UserWorkloadsConfigMap item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListUserWorkloadsConfigMapsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsConfigMap item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsConfigMap> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsConfigMap item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsConfigMaps(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUserWorkloadsConfigMapsResponse, UserWorkloadsConfigMap> ListUserWorkloadsConfigMaps(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. List ConfigMaps in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsResponse)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A pageable sequence of [UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    // Make the request
    PagedEnumerable<gcoasv::ListUserWorkloadsConfigMapsResponse, gcoasv::UserWorkloadsConfigMap> response = environmentsClient.ListUserWorkloadsConfigMaps(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::UserWorkloadsConfigMap item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListUserWorkloadsConfigMapsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsConfigMap item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsConfigMap> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsConfigMap item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsConfigMapsAsync(EnvironmentName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUserWorkloadsConfigMapsResponse, UserWorkloadsConfigMap> ListUserWorkloadsConfigMapsAsync(EnvironmentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. List ConfigMaps in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsResponse)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A pageable asynchronous sequence of [UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListUserWorkloadsConfigMapsResponse, gcoasv::UserWorkloadsConfigMap> response = environmentsClient.ListUserWorkloadsConfigMapsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::UserWorkloadsConfigMap item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListUserWorkloadsConfigMapsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsConfigMap item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsConfigMap> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsConfigMap item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsConfigMapsAsync(ListUserWorkloadsConfigMapsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUserWorkloadsConfigMapsResponse, UserWorkloadsConfigMap> ListUserWorkloadsConfigMapsAsync(ListUserWorkloadsConfigMapsRequest request, CallSettings callSettings = null)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsResponse)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A pageable asynchronous sequence of [UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::ListUserWorkloadsConfigMapsRequest request = new gcoasv::ListUserWorkloadsConfigMapsRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListUserWorkloadsConfigMapsResponse, gcoasv::UserWorkloadsConfigMap> response = environmentsClient.ListUserWorkloadsConfigMapsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::UserWorkloadsConfigMap item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListUserWorkloadsConfigMapsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsConfigMap item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsConfigMap> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsConfigMap item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsConfigMapsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUserWorkloadsConfigMapsResponse, UserWorkloadsConfigMap> ListUserWorkloadsConfigMapsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. List ConfigMaps in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsResponse)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A pageable asynchronous sequence of [UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListUserWorkloadsConfigMapsResponse, gcoasv::UserWorkloadsConfigMap> response = environmentsClient.ListUserWorkloadsConfigMapsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::UserWorkloadsConfigMap item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListUserWorkloadsConfigMapsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsConfigMap item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsConfigMap> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsConfigMap item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsSecrets(EnvironmentName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUserWorkloadsSecretsResponse, UserWorkloadsSecret> ListUserWorkloadsSecrets(EnvironmentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. List Secrets in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsResponse)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A pageable sequence of [UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    // Make the request
    PagedEnumerable<gcoasv::ListUserWorkloadsSecretsResponse, gcoasv::UserWorkloadsSecret> response = environmentsClient.ListUserWorkloadsSecrets(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::UserWorkloadsSecret item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListUserWorkloadsSecretsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsSecret item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsSecret> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsSecret item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListUserWorkloadsSecretsResponse, UserWorkloadsSecret> ListUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest request, CallSettings callSettings = null)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsResponse)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A pageable sequence of [UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::ListUserWorkloadsSecretsRequest request = new gcoasv::ListUserWorkloadsSecretsRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
    };
    // Make the request
    PagedEnumerable<gcoasv::ListUserWorkloadsSecretsResponse, gcoasv::UserWorkloadsSecret> response = environmentsClient.ListUserWorkloadsSecrets(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::UserWorkloadsSecret item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListUserWorkloadsSecretsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsSecret item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsSecret> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsSecret item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsSecrets(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListUserWorkloadsSecretsResponse, UserWorkloadsSecret> ListUserWorkloadsSecrets(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. List Secrets in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsResponse)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A pageable sequence of [UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    // Make the request
    PagedEnumerable<gcoasv::ListUserWorkloadsSecretsResponse, gcoasv::UserWorkloadsSecret> response = environmentsClient.ListUserWorkloadsSecrets(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::UserWorkloadsSecret item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListUserWorkloadsSecretsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsSecret item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsSecret> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsSecret item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsSecretsAsync(EnvironmentName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUserWorkloadsSecretsResponse, UserWorkloadsSecret> ListUserWorkloadsSecretsAsync(EnvironmentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. List Secrets in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsResponse)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A pageable asynchronous sequence of [UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListUserWorkloadsSecretsResponse, gcoasv::UserWorkloadsSecret> response = environmentsClient.ListUserWorkloadsSecretsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::UserWorkloadsSecret item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListUserWorkloadsSecretsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsSecret item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsSecret> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsSecret item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsSecretsAsync(ListUserWorkloadsSecretsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUserWorkloadsSecretsResponse, UserWorkloadsSecret> ListUserWorkloadsSecretsAsync(ListUserWorkloadsSecretsRequest request, CallSettings callSettings = null)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsResponse)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A pageable asynchronous sequence of [UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::ListUserWorkloadsSecretsRequest request = new gcoasv::ListUserWorkloadsSecretsRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListUserWorkloadsSecretsResponse, gcoasv::UserWorkloadsSecret> response = environmentsClient.ListUserWorkloadsSecretsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::UserWorkloadsSecret item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListUserWorkloadsSecretsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsSecret item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsSecret> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsSecret item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListUserWorkloadsSecretsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListUserWorkloadsSecretsResponse, UserWorkloadsSecret> ListUserWorkloadsSecretsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. List Secrets in the given environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsResponse)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A pageable asynchronous sequence of [UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListUserWorkloadsSecretsResponse, gcoasv::UserWorkloadsSecret> response = environmentsClient.ListUserWorkloadsSecretsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::UserWorkloadsSecret item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListUserWorkloadsSecretsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::UserWorkloadsSecret item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::UserWorkloadsSecret> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::UserWorkloadsSecret item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(EnvironmentName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, ListWorkloadsResponse.Types.ComposerWorkload> ListWorkloads(EnvironmentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. The environment name to get workloads for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types)[ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload)` | A pageable sequence of [ListWorkloadsResponse.Types.ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    // Make the request
    PagedEnumerable<gcoasv::ListWorkloadsResponse, gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> response = environmentsClient.ListWorkloads(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(ListWorkloadsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, ListWorkloadsResponse.Types.ComposerWorkload> ListWorkloads(ListWorkloadsRequest request, CallSettings callSettings = null)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types)[ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload)` | A pageable sequence of [ListWorkloadsResponse.Types.ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::ListWorkloadsRequest request = new gcoasv::ListWorkloadsRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcoasv::ListWorkloadsResponse, gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> response = environmentsClient.ListWorkloads(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloads(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWorkloadsResponse, ListWorkloadsResponse.Types.ComposerWorkload> ListWorkloads(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The environment name to get workloads for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types)[ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload)` | A pageable sequence of [ListWorkloadsResponse.Types.ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    // Make the request
    PagedEnumerable<gcoasv::ListWorkloadsResponse, gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> response = environmentsClient.ListWorkloads(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcoasv::ListWorkloadsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(EnvironmentName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, ListWorkloadsResponse.Types.ComposerWorkload> ListWorkloadsAsync(EnvironmentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentName)`  
Required. The environment name to get workloads for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types)[ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload)` | A pageable asynchronous sequence of [ListWorkloadsResponse.Types.ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::EnvironmentName parent = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]");
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListWorkloadsResponse, gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> response = environmentsClient.ListWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(ListWorkloadsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, ListWorkloadsResponse.Types.ComposerWorkload> ListWorkloadsAsync(ListWorkloadsRequest request, CallSettings callSettings = null)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types)[ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload)` | A pageable asynchronous sequence of [ListWorkloadsResponse.Types.ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::ListWorkloadsRequest request = new gcoasv::ListWorkloadsRequest
    {
        ParentAsEnvironmentName = gcoasv::EnvironmentName.FromProjectLocationEnvironment("[PROJECT]", "[LOCATION]", "[ENVIRONMENT]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListWorkloadsResponse, gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> response = environmentsClient.ListWorkloadsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWorkloadsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWorkloadsResponse, ListWorkloadsResponse.Types.ComposerWorkload> ListWorkloadsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The environment name to get workloads for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types)[ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload)` | A pageable asynchronous sequence of [ListWorkloadsResponse.Types.ComposerWorkload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse.Types.ComposerWorkload) resources.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/environments/[ENVIRONMENT]";
    // Make the request
    PagedAsyncEnumerable<gcoasv::ListWorkloadsResponse, gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> response = environmentsClient.ListWorkloadsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcoasv::ListWorkloadsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcoasv::ListWorkloadsResponse.Types.ComposerWorkload> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcoasv::ListWorkloadsResponse.Types.ComposerWorkload item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### LoadSnapshot(LoadSnapshotRequest, CallSettings)
    
    
    public virtual Operation<LoadSnapshotResponse, OperationMetadata> LoadSnapshot(LoadSnapshotRequest request, CallSettings callSettings = null)

Loads a snapshot of a Cloud Composer environment.

As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LoadSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[LoadSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::LoadSnapshotRequest request = new gcoasv::LoadSnapshotRequest
    {
        Environment = "",
        SnapshotPath = "",
        SkipPypiPackagesInstallation = false,
        SkipEnvironmentVariablesSetting = false,
        SkipAirflowOverridesSetting = false,
        SkipGcsDataCopying = false,
    };
    // Make the request
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> response = environmentsClient.LoadSnapshot(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcoasv::LoadSnapshotResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceLoadSnapshot(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::LoadSnapshotResponse retrievedResult = retrievedResponse.Result;
    }
    

### LoadSnapshotAsync(LoadSnapshotRequest, CallSettings)
    
    
    public virtual Task<Operation<LoadSnapshotResponse, OperationMetadata>> LoadSnapshotAsync(LoadSnapshotRequest request, CallSettings callSettings = null)

Loads a snapshot of a Cloud Composer environment.

As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LoadSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[LoadSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::LoadSnapshotRequest request = new gcoasv::LoadSnapshotRequest
    {
        Environment = "",
        SnapshotPath = "",
        SkipPypiPackagesInstallation = false,
        SkipEnvironmentVariablesSetting = false,
        SkipAirflowOverridesSetting = false,
        SkipGcsDataCopying = false,
    };
    // Make the request
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> response = await environmentsClient.LoadSnapshotAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::LoadSnapshotResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceLoadSnapshotAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::LoadSnapshotResponse retrievedResult = retrievedResponse.Result;
    }
    

### LoadSnapshotAsync(LoadSnapshotRequest, CancellationToken)
    
    
    public virtual Task<Operation<LoadSnapshotResponse, OperationMetadata>> LoadSnapshotAsync(LoadSnapshotRequest request, CancellationToken cancellationToken)

Loads a snapshot of a Cloud Composer environment.

As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LoadSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[LoadSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::LoadSnapshotRequest request = new gcoasv::LoadSnapshotRequest
    {
        Environment = "",
        SnapshotPath = "",
        SkipPypiPackagesInstallation = false,
        SkipEnvironmentVariablesSetting = false,
        SkipAirflowOverridesSetting = false,
        SkipGcsDataCopying = false,
    };
    // Make the request
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> response = await environmentsClient.LoadSnapshotAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::LoadSnapshotResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::LoadSnapshotResponse, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceLoadSnapshotAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::LoadSnapshotResponse retrievedResult = retrievedResponse.Result;
    }
    

### PollAirflowCommand(PollAirflowCommandRequest, CallSettings)
    
    
    public virtual PollAirflowCommandResponse PollAirflowCommand(PollAirflowCommandRequest request, CallSettings callSettings = null)

Polls Airflow CLI command execution and fetches logs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PollAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.PollAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PollAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.PollAirflowCommandResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::PollAirflowCommandRequest request = new gcoasv::PollAirflowCommandRequest
    {
        Environment = "",
        ExecutionId = "",
        Pod = "",
        PodNamespace = "",
        NextLineNumber = 0,
    };
    // Make the request
    gcoasv::PollAirflowCommandResponse response = environmentsClient.PollAirflowCommand(request);
    

### PollAirflowCommandAsync(PollAirflowCommandRequest, CallSettings)
    
    
    public virtual Task<PollAirflowCommandResponse> PollAirflowCommandAsync(PollAirflowCommandRequest request, CallSettings callSettings = null)

Polls Airflow CLI command execution and fetches logs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PollAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.PollAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PollAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.PollAirflowCommandResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::PollAirflowCommandRequest request = new gcoasv::PollAirflowCommandRequest
    {
        Environment = "",
        ExecutionId = "",
        Pod = "",
        PodNamespace = "",
        NextLineNumber = 0,
    };
    // Make the request
    gcoasv::PollAirflowCommandResponse response = await environmentsClient.PollAirflowCommandAsync(request);
    

### PollAirflowCommandAsync(PollAirflowCommandRequest, CancellationToken)
    
    
    public virtual Task<PollAirflowCommandResponse> PollAirflowCommandAsync(PollAirflowCommandRequest request, CancellationToken cancellationToken)

Polls Airflow CLI command execution and fetches logs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PollAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.PollAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PollAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.PollAirflowCommandResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::PollAirflowCommandRequest request = new gcoasv::PollAirflowCommandRequest
    {
        Environment = "",
        ExecutionId = "",
        Pod = "",
        PodNamespace = "",
        NextLineNumber = 0,
    };
    // Make the request
    gcoasv::PollAirflowCommandResponse response = await environmentsClient.PollAirflowCommandAsync(request);
    

### PollOnceCheckUpgrade(string, CallSettings)
    
    
    public virtual Operation<CheckUpgradeResponse, OperationMetadata> PollOnceCheckUpgrade(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CheckUpgrade`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CheckUpgradeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCheckUpgradeAsync(string, CallSettings)
    
    
    public virtual Task<Operation<CheckUpgradeResponse, OperationMetadata>> PollOnceCheckUpgradeAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CheckUpgrade`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[CheckUpgradeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateEnvironment(string, CallSettings)
    
    
    public virtual Operation<Environment, OperationMetadata> PollOnceCreateEnvironment(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateEnvironment` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateEnvironmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> PollOnceCreateEnvironmentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateEnvironment`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDatabaseFailover(string, CallSettings)
    
    
    public virtual Operation<DatabaseFailoverResponse, OperationMetadata> PollOnceDatabaseFailover(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DatabaseFailover`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DatabaseFailoverResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDatabaseFailoverAsync(string, CallSettings)
    
    
    public virtual Task<Operation<DatabaseFailoverResponse, OperationMetadata>> PollOnceDatabaseFailoverAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DatabaseFailover`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DatabaseFailoverResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteEnvironment(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteEnvironment(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteEnvironment` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteEnvironmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteEnvironmentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteEnvironment`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceLoadSnapshot(string, CallSettings)
    
    
    public virtual Operation<LoadSnapshotResponse, OperationMetadata> PollOnceLoadSnapshot(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `LoadSnapshot`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[LoadSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceLoadSnapshotAsync(string, CallSettings)
    
    
    public virtual Task<Operation<LoadSnapshotResponse, OperationMetadata>> PollOnceLoadSnapshotAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `LoadSnapshot`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[LoadSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceSaveSnapshot(string, CallSettings)
    
    
    public virtual Operation<SaveSnapshotResponse, OperationMetadata> PollOnceSaveSnapshot(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `SaveSnapshot`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SaveSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceSaveSnapshotAsync(string, CallSettings)
    
    
    public virtual Task<Operation<SaveSnapshotResponse, OperationMetadata>> PollOnceSaveSnapshotAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `SaveSnapshot`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SaveSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateEnvironment(string, CallSettings)
    
    
    public virtual Operation<Environment, OperationMetadata> PollOnceUpdateEnvironment(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateEnvironment` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateEnvironmentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> PollOnceUpdateEnvironmentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateEnvironment`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### SaveSnapshot(SaveSnapshotRequest, CallSettings)
    
    
    public virtual Operation<SaveSnapshotResponse, OperationMetadata> SaveSnapshot(SaveSnapshotRequest request, CallSettings callSettings = null)

Creates a snapshots of a Cloud Composer environment.

As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SaveSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SaveSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::SaveSnapshotRequest request = new gcoasv::SaveSnapshotRequest
    {
        Environment = "",
        SnapshotLocation = "",
    };
    // Make the request
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> response = environmentsClient.SaveSnapshot(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcoasv::SaveSnapshotResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceSaveSnapshot(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::SaveSnapshotResponse retrievedResult = retrievedResponse.Result;
    }
    

### SaveSnapshotAsync(SaveSnapshotRequest, CallSettings)
    
    
    public virtual Task<Operation<SaveSnapshotResponse, OperationMetadata>> SaveSnapshotAsync(SaveSnapshotRequest request, CallSettings callSettings = null)

Creates a snapshots of a Cloud Composer environment.

As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SaveSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SaveSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::SaveSnapshotRequest request = new gcoasv::SaveSnapshotRequest
    {
        Environment = "",
        SnapshotLocation = "",
    };
    // Make the request
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> response = await environmentsClient.SaveSnapshotAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::SaveSnapshotResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceSaveSnapshotAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::SaveSnapshotResponse retrievedResult = retrievedResponse.Result;
    }
    

### SaveSnapshotAsync(SaveSnapshotRequest, CancellationToken)
    
    
    public virtual Task<Operation<SaveSnapshotResponse, OperationMetadata>> SaveSnapshotAsync(SaveSnapshotRequest request, CancellationToken cancellationToken)

Creates a snapshots of a Cloud Composer environment.

As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SaveSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SaveSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::SaveSnapshotRequest request = new gcoasv::SaveSnapshotRequest
    {
        Environment = "",
        SnapshotLocation = "",
    };
    // Make the request
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> response = await environmentsClient.SaveSnapshotAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::SaveSnapshotResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::SaveSnapshotResponse, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceSaveSnapshotAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::SaveSnapshotResponse retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient#Google_Cloud_Orchestration_Airflow_Service_V1_EnvironmentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient#Google_Cloud_Orchestration_Airflow_Service_V1_EnvironmentsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient#Google_Cloud_Orchestration_Airflow_Service_V1_EnvironmentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.EnvironmentsClient#Google_Cloud_Orchestration_Airflow_Service_V1_EnvironmentsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### StopAirflowCommand(StopAirflowCommandRequest, CallSettings)
    
    
    public virtual StopAirflowCommandResponse StopAirflowCommand(StopAirflowCommandRequest request, CallSettings callSettings = null)

Stops Airflow CLI command execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.StopAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[StopAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.StopAirflowCommandResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::StopAirflowCommandRequest request = new gcoasv::StopAirflowCommandRequest
    {
        Environment = "",
        ExecutionId = "",
        Pod = "",
        PodNamespace = "",
        Force = false,
    };
    // Make the request
    gcoasv::StopAirflowCommandResponse response = environmentsClient.StopAirflowCommand(request);
    

### StopAirflowCommandAsync(StopAirflowCommandRequest, CallSettings)
    
    
    public virtual Task<StopAirflowCommandResponse> StopAirflowCommandAsync(StopAirflowCommandRequest request, CallSettings callSettings = null)

Stops Airflow CLI command execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.StopAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.StopAirflowCommandResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::StopAirflowCommandRequest request = new gcoasv::StopAirflowCommandRequest
    {
        Environment = "",
        ExecutionId = "",
        Pod = "",
        PodNamespace = "",
        Force = false,
    };
    // Make the request
    gcoasv::StopAirflowCommandResponse response = await environmentsClient.StopAirflowCommandAsync(request);
    

### StopAirflowCommandAsync(StopAirflowCommandRequest, CancellationToken)
    
    
    public virtual Task<StopAirflowCommandResponse> StopAirflowCommandAsync(StopAirflowCommandRequest request, CancellationToken cancellationToken)

Stops Airflow CLI command execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.StopAirflowCommandRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.StopAirflowCommandResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::StopAirflowCommandRequest request = new gcoasv::StopAirflowCommandRequest
    {
        Environment = "",
        ExecutionId = "",
        Pod = "",
        PodNamespace = "",
        Force = false,
    };
    // Make the request
    gcoasv::StopAirflowCommandResponse response = await environmentsClient.StopAirflowCommandAsync(request);
    

### UpdateEnvironment(UpdateEnvironmentRequest, CallSettings)
    
    
    public virtual Operation<Environment, OperationMetadata> UpdateEnvironment(UpdateEnvironmentRequest request, CallSettings callSettings = null)

Update an environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UpdateEnvironmentRequest request = new gcoasv::UpdateEnvironmentRequest
    {
        Environment = new gcoasv::Environment(),
        Name = "",
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = environmentsClient.UpdateEnvironment(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceUpdateEnvironment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateEnvironment(string, Environment, FieldMask, CallSettings)
    
    
    public virtual Operation<Environment, OperationMetadata> UpdateEnvironment(string name, Environment environment, FieldMask updateMask, CallSettings callSettings = null)

Update an environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The relative resource name of the environment to update, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`environment` | `[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)`  
A patch environment. Fields specified by the `updateMask` will be copied from the patch environment into the environment under update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A comma-separated list of paths, relative to `Environment`, of fields to update. For example, to set the version of scikit-learn to install in the environment to 0.19.0 and to remove an existing installation of numpy, the `updateMask` parameter would include the following two `paths` values: "config.softwareConfig.pypiPackages.scikit-learn" and "config.softwareConfig.pypiPackages.numpy". The included patch environment would specify the scikit-learn version as follows: { "config":{ "softwareConfig":{ "pypiPackages":{ "scikit-learn":"==0.19.0" } } } } Note that in the above example, any existing PyPI packages other than scikit-learn and numpy will be unaffected. Only one update type may be included in a single request's `updateMask`. For example, one cannot update both the PyPI packages and labels in the same request. However, it is possible to update multiple members of a map field simultaneously in the same request. For example, to set the labels "label1" and "label2" while clearing "label3" (assuming it already exists), one can provide the paths "labels.label1", "labels.label2", and "labels.label3" and populate the patch environment as follows: { "labels":{ "label1":"new-label1-value" "label2":"new-label2-value" } } Note that in the above example, any existing labels that are not included in the `updateMask` will be unaffected. It is also possible to replace an entire map field by providing the map field's path in the `updateMask`. The new value of the field will be that which is provided in the patch environment. For example, to delete all pre-existing user-specified PyPI packages and install botocore at version 1.7.14, the `updateMask` would contain the path "config.softwareConfig.pypiPackages", and the patch environment would be the following: { "config":{ "softwareConfig":{ "pypiPackages":{ "botocore":"==1.7.14" } } } } **Note:** Only the following fields can be updated:

  * `config.softwareConfig.pypiPackages`
  * Replace all custom custom PyPI packages. If a replacement package map is not included in `environment`, all custom PyPI packages are cleared. It is an error to provide both this mask and a mask specifying an individual package.
  * `config.softwareConfig.pypiPackages.`packagename
  * Update the custom PyPI package _packagename_ , preserving other packages. To delete the package, include it in `updateMask`, and omit the mapping for it in `environment.config.softwareConfig.pypiPackages`. It is an error to provide both a mask of this form and the `config.softwareConfig.pypiPackages` mask.
  * `labels`
  * Replace all environment labels. If a replacement labels map is not included in `environment`, all labels are cleared. It is an error to provide both this mask and a mask specifying one or more individual labels.
  * `labels.`labelName
  * Set the label named _labelName_ , while preserving other labels. To delete the label, include it in `updateMask` and omit its mapping in `environment.labels`. It is an error to provide both a mask of this form and the `labels` mask.
  * `config.nodeCount`
  * Horizontally scale the number of nodes in the environment. An integer greater than or equal to 3 must be provided in the `config.nodeCount` field. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.
  * `config.webServerNetworkAccessControl`
  * Replace the environment's current `WebServerNetworkAccessControl`.
  * `config.softwareConfig.airflowConfigOverrides`
  * Replace all Apache Airflow config overrides. If a replacement config overrides map is not included in `environment`, all config overrides are cleared. It is an error to provide both this mask and a mask specifying one or more individual config overrides.
  * `config.softwareConfig.airflowConfigOverrides.`section-name
  * Override the Apache Airflow config property _name_ in the section named _section_ , preserving other properties. To delete the property override, include it in `updateMask` and omit its mapping in `environment.config.softwareConfig.airflowConfigOverrides`. It is an error to provide both a mask of this form and the `config.softwareConfig.airflowConfigOverrides` mask.
  * `config.softwareConfig.envVariables`
  * Replace all environment variables. If a replacement environment variable map is not included in `environment`, all custom environment variables are cleared.
  * `config.softwareConfig.schedulerCount`
  * Horizontally scale the number of schedulers in Airflow. A positive integer not greater than the number of nodes must be provided in the `config.softwareConfig.schedulerCount` field. Supported for Cloud Composer environments in versions composer-1._._ -airflow-2._._.
  * `config.databaseConfig.machineType`
  * Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.
  * `config.webServerConfig.machineType`
  * Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    string name = "";
    gcoasv::Environment environment = new gcoasv::Environment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = environmentsClient.UpdateEnvironment(name, environment, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = environmentsClient.PollOnceUpdateEnvironment(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateEnvironmentAsync(UpdateEnvironmentRequest, CallSettings)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> UpdateEnvironmentAsync(UpdateEnvironmentRequest request, CallSettings callSettings = null)

Update an environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UpdateEnvironmentRequest request = new gcoasv::UpdateEnvironmentRequest
    {
        Environment = new gcoasv::Environment(),
        Name = "",
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = await environmentsClient.UpdateEnvironmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceUpdateEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateEnvironmentAsync(UpdateEnvironmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> UpdateEnvironmentAsync(UpdateEnvironmentRequest request, CancellationToken cancellationToken)

Update an environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateEnvironmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UpdateEnvironmentRequest request = new gcoasv::UpdateEnvironmentRequest
    {
        Environment = new gcoasv::Environment(),
        Name = "",
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = await environmentsClient.UpdateEnvironmentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceUpdateEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateEnvironmentAsync(string, Environment, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> UpdateEnvironmentAsync(string name, Environment environment, FieldMask updateMask, CallSettings callSettings = null)

Update an environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The relative resource name of the environment to update, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`environment` | `[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)`  
A patch environment. Fields specified by the `updateMask` will be copied from the patch environment into the environment under update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A comma-separated list of paths, relative to `Environment`, of fields to update. For example, to set the version of scikit-learn to install in the environment to 0.19.0 and to remove an existing installation of numpy, the `updateMask` parameter would include the following two `paths` values: "config.softwareConfig.pypiPackages.scikit-learn" and "config.softwareConfig.pypiPackages.numpy". The included patch environment would specify the scikit-learn version as follows: { "config":{ "softwareConfig":{ "pypiPackages":{ "scikit-learn":"==0.19.0" } } } } Note that in the above example, any existing PyPI packages other than scikit-learn and numpy will be unaffected. Only one update type may be included in a single request's `updateMask`. For example, one cannot update both the PyPI packages and labels in the same request. However, it is possible to update multiple members of a map field simultaneously in the same request. For example, to set the labels "label1" and "label2" while clearing "label3" (assuming it already exists), one can provide the paths "labels.label1", "labels.label2", and "labels.label3" and populate the patch environment as follows: { "labels":{ "label1":"new-label1-value" "label2":"new-label2-value" } } Note that in the above example, any existing labels that are not included in the `updateMask` will be unaffected. It is also possible to replace an entire map field by providing the map field's path in the `updateMask`. The new value of the field will be that which is provided in the patch environment. For example, to delete all pre-existing user-specified PyPI packages and install botocore at version 1.7.14, the `updateMask` would contain the path "config.softwareConfig.pypiPackages", and the patch environment would be the following: { "config":{ "softwareConfig":{ "pypiPackages":{ "botocore":"==1.7.14" } } } } **Note:** Only the following fields can be updated:

  * `config.softwareConfig.pypiPackages`
  * Replace all custom custom PyPI packages. If a replacement package map is not included in `environment`, all custom PyPI packages are cleared. It is an error to provide both this mask and a mask specifying an individual package.
  * `config.softwareConfig.pypiPackages.`packagename
  * Update the custom PyPI package _packagename_ , preserving other packages. To delete the package, include it in `updateMask`, and omit the mapping for it in `environment.config.softwareConfig.pypiPackages`. It is an error to provide both a mask of this form and the `config.softwareConfig.pypiPackages` mask.
  * `labels`
  * Replace all environment labels. If a replacement labels map is not included in `environment`, all labels are cleared. It is an error to provide both this mask and a mask specifying one or more individual labels.
  * `labels.`labelName
  * Set the label named _labelName_ , while preserving other labels. To delete the label, include it in `updateMask` and omit its mapping in `environment.labels`. It is an error to provide both a mask of this form and the `labels` mask.
  * `config.nodeCount`
  * Horizontally scale the number of nodes in the environment. An integer greater than or equal to 3 must be provided in the `config.nodeCount` field. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.
  * `config.webServerNetworkAccessControl`
  * Replace the environment's current `WebServerNetworkAccessControl`.
  * `config.softwareConfig.airflowConfigOverrides`
  * Replace all Apache Airflow config overrides. If a replacement config overrides map is not included in `environment`, all config overrides are cleared. It is an error to provide both this mask and a mask specifying one or more individual config overrides.
  * `config.softwareConfig.airflowConfigOverrides.`section-name
  * Override the Apache Airflow config property _name_ in the section named _section_ , preserving other properties. To delete the property override, include it in `updateMask` and omit its mapping in `environment.config.softwareConfig.airflowConfigOverrides`. It is an error to provide both a mask of this form and the `config.softwareConfig.airflowConfigOverrides` mask.
  * `config.softwareConfig.envVariables`
  * Replace all environment variables. If a replacement environment variable map is not included in `environment`, all custom environment variables are cleared.
  * `config.softwareConfig.schedulerCount`
  * Horizontally scale the number of schedulers in Airflow. A positive integer not greater than the number of nodes must be provided in the `config.softwareConfig.schedulerCount` field. Supported for Cloud Composer environments in versions composer-1._._ -airflow-2._._.
  * `config.databaseConfig.machineType`
  * Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.
  * `config.webServerConfig.machineType`
  * Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    gcoasv::Environment environment = new gcoasv::Environment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = await environmentsClient.UpdateEnvironmentAsync(name, environment, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceUpdateEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateEnvironmentAsync(string, Environment, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Environment, OperationMetadata>> UpdateEnvironmentAsync(string name, Environment environment, FieldMask updateMask, CancellationToken cancellationToken)

Update an environment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The relative resource name of the environment to update, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}"  
`environment` | `[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)`  
A patch environment. Fields specified by the `updateMask` will be copied from the patch environment into the environment under update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. A comma-separated list of paths, relative to `Environment`, of fields to update. For example, to set the version of scikit-learn to install in the environment to 0.19.0 and to remove an existing installation of numpy, the `updateMask` parameter would include the following two `paths` values: "config.softwareConfig.pypiPackages.scikit-learn" and "config.softwareConfig.pypiPackages.numpy". The included patch environment would specify the scikit-learn version as follows: { "config":{ "softwareConfig":{ "pypiPackages":{ "scikit-learn":"==0.19.0" } } } } Note that in the above example, any existing PyPI packages other than scikit-learn and numpy will be unaffected. Only one update type may be included in a single request's `updateMask`. For example, one cannot update both the PyPI packages and labels in the same request. However, it is possible to update multiple members of a map field simultaneously in the same request. For example, to set the labels "label1" and "label2" while clearing "label3" (assuming it already exists), one can provide the paths "labels.label1", "labels.label2", and "labels.label3" and populate the patch environment as follows: { "labels":{ "label1":"new-label1-value" "label2":"new-label2-value" } } Note that in the above example, any existing labels that are not included in the `updateMask` will be unaffected. It is also possible to replace an entire map field by providing the map field's path in the `updateMask`. The new value of the field will be that which is provided in the patch environment. For example, to delete all pre-existing user-specified PyPI packages and install botocore at version 1.7.14, the `updateMask` would contain the path "config.softwareConfig.pypiPackages", and the patch environment would be the following: { "config":{ "softwareConfig":{ "pypiPackages":{ "botocore":"==1.7.14" } } } } **Note:** Only the following fields can be updated:

  * `config.softwareConfig.pypiPackages`
  * Replace all custom custom PyPI packages. If a replacement package map is not included in `environment`, all custom PyPI packages are cleared. It is an error to provide both this mask and a mask specifying an individual package.
  * `config.softwareConfig.pypiPackages.`packagename
  * Update the custom PyPI package _packagename_ , preserving other packages. To delete the package, include it in `updateMask`, and omit the mapping for it in `environment.config.softwareConfig.pypiPackages`. It is an error to provide both a mask of this form and the `config.softwareConfig.pypiPackages` mask.
  * `labels`
  * Replace all environment labels. If a replacement labels map is not included in `environment`, all labels are cleared. It is an error to provide both this mask and a mask specifying one or more individual labels.
  * `labels.`labelName
  * Set the label named _labelName_ , while preserving other labels. To delete the label, include it in `updateMask` and omit its mapping in `environment.labels`. It is an error to provide both a mask of this form and the `labels` mask.
  * `config.nodeCount`
  * Horizontally scale the number of nodes in the environment. An integer greater than or equal to 3 must be provided in the `config.nodeCount` field. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.
  * `config.webServerNetworkAccessControl`
  * Replace the environment's current `WebServerNetworkAccessControl`.
  * `config.softwareConfig.airflowConfigOverrides`
  * Replace all Apache Airflow config overrides. If a replacement config overrides map is not included in `environment`, all config overrides are cleared. It is an error to provide both this mask and a mask specifying one or more individual config overrides.
  * `config.softwareConfig.airflowConfigOverrides.`section-name
  * Override the Apache Airflow config property _name_ in the section named _section_ , preserving other properties. To delete the property override, include it in `updateMask` and omit its mapping in `environment.config.softwareConfig.airflowConfigOverrides`. It is an error to provide both a mask of this form and the `config.softwareConfig.airflowConfigOverrides` mask.
  * `config.softwareConfig.envVariables`
  * Replace all environment variables. If a replacement environment variable map is not included in `environment`, all custom environment variables are cleared.
  * `config.softwareConfig.schedulerCount`
  * Horizontally scale the number of schedulers in Airflow. A positive integer not greater than the number of nodes must be provided in the `config.softwareConfig.schedulerCount` field. Supported for Cloud Composer environments in versions composer-1._._ -airflow-2._._.
  * `config.databaseConfig.machineType`
  * Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.
  * `config.webServerConfig.machineType`
  * Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. Supported for Cloud Composer environments in versions composer-1._._ -airflow-_._.*.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    gcoasv::Environment environment = new gcoasv::Environment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> response = await environmentsClient.UpdateEnvironmentAsync(name, environment, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcoasv::Environment result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcoasv::Environment, gcoasv::OperationMetadata> retrievedResponse = await environmentsClient.PollOnceUpdateEnvironmentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcoasv::Environment retrievedResult = retrievedResponse.Result;
    }
    

### UpdateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest, CallSettings)
    
    
    public virtual UserWorkloadsConfigMap UpdateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest request, CallSettings callSettings = null)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UpdateUserWorkloadsConfigMapRequest request = new gcoasv::UpdateUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap(),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = environmentsClient.UpdateUserWorkloadsConfigMap(request);
    

### UpdateUserWorkloadsConfigMap(UserWorkloadsConfigMap, CallSettings)
    
    
    public virtual UserWorkloadsConfigMap UpdateUserWorkloadsConfigMap(UserWorkloadsConfigMap userWorkloadsConfigMap, CallSettings callSettings = null)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Optional. User workloads ConfigMap to override.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = environmentsClient.UpdateUserWorkloadsConfigMap(userWorkloadsConfigMap);
    

### UpdateUserWorkloadsConfigMapAsync(UpdateUserWorkloadsConfigMapRequest, CallSettings)
    
    
    public virtual Task<UserWorkloadsConfigMap> UpdateUserWorkloadsConfigMapAsync(UpdateUserWorkloadsConfigMapRequest request, CallSettings callSettings = null)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UpdateUserWorkloadsConfigMapRequest request = new gcoasv::UpdateUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap(),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.UpdateUserWorkloadsConfigMapAsync(request);
    

### UpdateUserWorkloadsConfigMapAsync(UpdateUserWorkloadsConfigMapRequest, CancellationToken)
    
    
    public virtual Task<UserWorkloadsConfigMap> UpdateUserWorkloadsConfigMapAsync(UpdateUserWorkloadsConfigMapRequest request, CancellationToken cancellationToken)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateUserWorkloadsConfigMapRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UpdateUserWorkloadsConfigMapRequest request = new gcoasv::UpdateUserWorkloadsConfigMapRequest
    {
        UserWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap(),
    };
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.UpdateUserWorkloadsConfigMapAsync(request);
    

### UpdateUserWorkloadsConfigMapAsync(UserWorkloadsConfigMap, CallSettings)
    
    
    public virtual Task<UserWorkloadsConfigMap> UpdateUserWorkloadsConfigMapAsync(UserWorkloadsConfigMap userWorkloadsConfigMap, CallSettings callSettings = null)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Optional. User workloads ConfigMap to override.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.UpdateUserWorkloadsConfigMapAsync(userWorkloadsConfigMap);
    

### UpdateUserWorkloadsConfigMapAsync(UserWorkloadsConfigMap, CancellationToken)
    
    
    public virtual Task<UserWorkloadsConfigMap> UpdateUserWorkloadsConfigMapAsync(UserWorkloadsConfigMap userWorkloadsConfigMap, CancellationToken cancellationToken)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`userWorkloadsConfigMap` | `[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)`  
Optional. User workloads ConfigMap to override.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsConfigMap userWorkloadsConfigMap = new gcoasv::UserWorkloadsConfigMap();
    // Make the request
    gcoasv::UserWorkloadsConfigMap response = await environmentsClient.UpdateUserWorkloadsConfigMapAsync(userWorkloadsConfigMap);
    

### UpdateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest, CallSettings)
    
    
    public virtual UserWorkloadsSecret UpdateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest request, CallSettings callSettings = null)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UpdateUserWorkloadsSecretRequest request = new gcoasv::UpdateUserWorkloadsSecretRequest
    {
        UserWorkloadsSecret = new gcoasv::UserWorkloadsSecret(),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = environmentsClient.UpdateUserWorkloadsSecret(request);
    

### UpdateUserWorkloadsSecret(UserWorkloadsSecret, CallSettings)
    
    
    public virtual UserWorkloadsSecret UpdateUserWorkloadsSecret(UserWorkloadsSecret userWorkloadsSecret, CallSettings callSettings = null)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Optional. User workloads Secret to override.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = gcoasv::EnvironmentsClient.Create();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = environmentsClient.UpdateUserWorkloadsSecret(userWorkloadsSecret);
    

### UpdateUserWorkloadsSecretAsync(UpdateUserWorkloadsSecretRequest, CallSettings)
    
    
    public virtual Task<UserWorkloadsSecret> UpdateUserWorkloadsSecretAsync(UpdateUserWorkloadsSecretRequest request, CallSettings callSettings = null)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UpdateUserWorkloadsSecretRequest request = new gcoasv::UpdateUserWorkloadsSecretRequest
    {
        UserWorkloadsSecret = new gcoasv::UserWorkloadsSecret(),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.UpdateUserWorkloadsSecretAsync(request);
    

### UpdateUserWorkloadsSecretAsync(UpdateUserWorkloadsSecretRequest, CancellationToken)
    
    
    public virtual Task<UserWorkloadsSecret> UpdateUserWorkloadsSecretAsync(UpdateUserWorkloadsSecretRequest request, CancellationToken cancellationToken)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateUserWorkloadsSecretRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UpdateUserWorkloadsSecretRequest request = new gcoasv::UpdateUserWorkloadsSecretRequest
    {
        UserWorkloadsSecret = new gcoasv::UserWorkloadsSecret(),
    };
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.UpdateUserWorkloadsSecretAsync(request);
    

### UpdateUserWorkloadsSecretAsync(UserWorkloadsSecret, CallSettings)
    
    
    public virtual Task<UserWorkloadsSecret> UpdateUserWorkloadsSecretAsync(UserWorkloadsSecret userWorkloadsSecret, CallSettings callSettings = null)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Optional. User workloads Secret to override.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.UpdateUserWorkloadsSecretAsync(userWorkloadsSecret);
    

### UpdateUserWorkloadsSecretAsync(UserWorkloadsSecret, CancellationToken)
    
    
    public virtual Task<UserWorkloadsSecret> UpdateUserWorkloadsSecretAsync(UserWorkloadsSecret userWorkloadsSecret, CancellationToken cancellationToken)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`userWorkloadsSecret` | `[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)`  
Optional. User workloads Secret to override.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcoasv::EnvironmentsClient environmentsClient = await gcoasv::EnvironmentsClient.CreateAsync();
    // Initialize request argument(s)
    gcoasv::UserWorkloadsSecret userWorkloadsSecret = new gcoasv::UserWorkloadsSecret();
    // Make the request
    gcoasv::UserWorkloadsSecret response = await environmentsClient.UpdateUserWorkloadsSecretAsync(userWorkloadsSecret);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
