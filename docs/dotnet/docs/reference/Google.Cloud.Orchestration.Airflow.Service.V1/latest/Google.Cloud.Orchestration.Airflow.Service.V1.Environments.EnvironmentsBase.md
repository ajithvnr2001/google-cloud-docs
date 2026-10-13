---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase
title: Cloud Composer v1 API - Class Environments.EnvironmentsBase (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:20.675357+00:00
---

# Cloud Composer v1 API - Class Environments.EnvironmentsBase (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Composer v1 API - Class Environments.EnvironmentsBase (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.9.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.8.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.7.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.6.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.5.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.4.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.3.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.2.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.1.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/2.0.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/1.0.0/Google.Cloud.Orchestration.Airflow.Service.V1.Environments.EnvironmentsBase)


    
    
    [BindServiceMethod(typeof(Environments), "BindService")]
    public abstract class Environments.EnvironmentsBase

Reference documentation and code samples for the Cloud Composer v1 API class Environments.EnvironmentsBase.

Base class for server-side implementations of Environments

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Environments.EnvironmentsBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Orchestration.Airflow.Service.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1)

## Assembly

Google.Cloud.Orchestration.Airflow.Service.V1.dll

## Methods 

### CheckUpgrade(CheckUpgradeRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CheckUpgrade(CheckUpgradeRequest request, ServerCallContext context)

Check if an upgrade operation on the environment will succeed.

In case of problems detailed info can be found in the returned Operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckUpgradeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CheckUpgradeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateEnvironment(CreateEnvironmentRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateEnvironment(CreateEnvironmentRequest request, ServerCallContext context)

Create a new environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateEnvironmentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest, ServerCallContext)
    
    
    public virtual Task<UserWorkloadsConfigMap> CreateUserWorkloadsConfigMap(CreateUserWorkloadsConfigMapRequest request, ServerCallContext context)

Creates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateUserWorkloadsConfigMapRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The response to send back to the client (wrapped by a task).  
  
### CreateUserWorkloadsSecret(CreateUserWorkloadsSecretRequest, ServerCallContext)
    
    
    public virtual Task<UserWorkloadsSecret> CreateUserWorkloadsSecret(CreateUserWorkloadsSecretRequest request, ServerCallContext context)

Creates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.CreateUserWorkloadsSecretRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The response to send back to the client (wrapped by a task).  
  
### DatabaseFailover(DatabaseFailoverRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DatabaseFailover(DatabaseFailoverRequest request, ServerCallContext context)

Triggers database failover (only for highly resilient environments).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DatabaseFailoverRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DatabaseFailoverRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteEnvironment(DeleteEnvironmentRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteEnvironment(DeleteEnvironmentRequest request, ServerCallContext context)

Delete an environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteEnvironmentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteUserWorkloadsConfigMap(DeleteUserWorkloadsConfigMapRequest request, ServerCallContext context)

Deletes a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteUserWorkloadsConfigMapRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteUserWorkloadsSecret(DeleteUserWorkloadsSecretRequest request, ServerCallContext context)

Deletes a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.DeleteUserWorkloadsSecretRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### ExecuteAirflowCommand(ExecuteAirflowCommandRequest, ServerCallContext)
    
    
    public virtual Task<ExecuteAirflowCommandResponse> ExecuteAirflowCommand(ExecuteAirflowCommandRequest request, ServerCallContext context)

Executes Airflow CLI command.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ExecuteAirflowCommandRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ExecuteAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ExecuteAirflowCommandResponse)` | The response to send back to the client (wrapped by a task).  
  
### FetchDatabaseProperties(FetchDatabasePropertiesRequest, ServerCallContext)
    
    
    public virtual Task<FetchDatabasePropertiesResponse> FetchDatabaseProperties(FetchDatabasePropertiesRequest request, ServerCallContext context)

Fetches database properties.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchDatabasePropertiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.FetchDatabasePropertiesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FetchDatabasePropertiesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.FetchDatabasePropertiesResponse)` | The response to send back to the client (wrapped by a task).  
  
### GetEnvironment(GetEnvironmentRequest, ServerCallContext)
    
    
    public virtual Task<Environment> GetEnvironment(GetEnvironmentRequest request, ServerCallContext context)

Get an existing environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetEnvironmentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.Environment)` | The response to send back to the client (wrapped by a task).  
  
### GetUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest, ServerCallContext)
    
    
    public virtual Task<UserWorkloadsConfigMap> GetUserWorkloadsConfigMap(GetUserWorkloadsConfigMapRequest request, ServerCallContext context)

Gets an existing user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetUserWorkloadsConfigMapRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The response to send back to the client (wrapped by a task).  
  
### GetUserWorkloadsSecret(GetUserWorkloadsSecretRequest, ServerCallContext)
    
    
    public virtual Task<UserWorkloadsSecret> GetUserWorkloadsSecret(GetUserWorkloadsSecretRequest request, ServerCallContext context)

Gets an existing user workloads Secret. Values of the "data" field in the response are cleared.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.GetUserWorkloadsSecretRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The response to send back to the client (wrapped by a task).  
  
### ListEnvironments(ListEnvironmentsRequest, ServerCallContext)
    
    
    public virtual Task<ListEnvironmentsResponse> ListEnvironments(ListEnvironmentsRequest request, ServerCallContext context)

List environments.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEnvironmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListEnvironmentsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListEnvironmentsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest, ServerCallContext)
    
    
    public virtual Task<ListUserWorkloadsConfigMapsResponse> ListUserWorkloadsConfigMaps(ListUserWorkloadsConfigMapsRequest request, ServerCallContext context)

Lists user workloads ConfigMaps.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsConfigMapsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest, ServerCallContext)
    
    
    public virtual Task<ListUserWorkloadsSecretsResponse> ListUserWorkloadsSecrets(ListUserWorkloadsSecretsRequest request, ServerCallContext context)

Lists user workloads Secrets.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListUserWorkloadsSecretsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListWorkloads(ListWorkloadsRequest, ServerCallContext)
    
    
    public virtual Task<ListWorkloadsResponse> ListWorkloads(ListWorkloadsRequest request, ServerCallContext context)

Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component.

This method is supported for Cloud Composer environments in versions composer-2._._ -airflow-_._.* and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListWorkloadsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.ListWorkloadsResponse)` | The response to send back to the client (wrapped by a task).  
  
### LoadSnapshot(LoadSnapshotRequest, ServerCallContext)
    
    
    public virtual Task<Operation> LoadSnapshot(LoadSnapshotRequest request, ServerCallContext context)

Loads a snapshot of a Cloud Composer environment.

As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LoadSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.LoadSnapshotRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### PollAirflowCommand(PollAirflowCommandRequest, ServerCallContext)
    
    
    public virtual Task<PollAirflowCommandResponse> PollAirflowCommand(PollAirflowCommandRequest request, ServerCallContext context)

Polls Airflow CLI command execution and fetches logs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PollAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.PollAirflowCommandRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PollAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.PollAirflowCommandResponse)` | The response to send back to the client (wrapped by a task).  
  
### SaveSnapshot(SaveSnapshotRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SaveSnapshot(SaveSnapshotRequest request, ServerCallContext context)

Creates a snapshots of a Cloud Composer environment.

As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SaveSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.SaveSnapshotRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### StopAirflowCommand(StopAirflowCommandRequest, ServerCallContext)
    
    
    public virtual Task<StopAirflowCommandResponse> StopAirflowCommand(StopAirflowCommandRequest request, ServerCallContext context)

Stops Airflow CLI command execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopAirflowCommandRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.StopAirflowCommandRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopAirflowCommandResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.StopAirflowCommandResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateEnvironment(UpdateEnvironmentRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateEnvironment(UpdateEnvironmentRequest request, ServerCallContext context)

Update an environment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateEnvironmentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest, ServerCallContext)
    
    
    public virtual Task<UserWorkloadsConfigMap> UpdateUserWorkloadsConfigMap(UpdateUserWorkloadsConfigMapRequest request, ServerCallContext context)

Updates a user workloads ConfigMap.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateUserWorkloadsConfigMapRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsConfigMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsConfigMap)` | The response to send back to the client (wrapped by a task).  
  
### UpdateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest, ServerCallContext)
    
    
    public virtual Task<UserWorkloadsSecret> UpdateUserWorkloadsSecret(UpdateUserWorkloadsSecretRequest request, ServerCallContext context)

Updates a user workloads Secret.

This method is supported for Cloud Composer environments in versions composer-3-airflow-_._._-build._ and newer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UpdateUserWorkloadsSecretRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[UserWorkloadsSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Orchestration.Airflow.Service.V1/latest/Google.Cloud.Orchestration.Airflow.Service.V1.UserWorkloadsSecret)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
