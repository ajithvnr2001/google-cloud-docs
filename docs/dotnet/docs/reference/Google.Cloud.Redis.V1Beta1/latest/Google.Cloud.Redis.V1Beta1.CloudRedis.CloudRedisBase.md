---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisBase
title: Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedis.CloudRedisBase (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:57.815534+00:00
---

# Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedis.CloudRedisBase (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedis.CloudRedisBase (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisBase)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/3.0.0-beta05/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisBase)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/2.0.0-beta09/Google.Cloud.Redis.V1Beta1.CloudRedis.CloudRedisBase)


    
    
    [BindServiceMethod(typeof(CloudRedis), "BindService")]
    public abstract class CloudRedis.CloudRedisBase

Reference documentation and code samples for the Google Cloud Memorystore for Redis v1beta1 API class CloudRedis.CloudRedisBase.

Base class for server-side implementations of CloudRedis

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudRedis.CloudRedisBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1)

## Assembly

Google.Cloud.Redis.V1Beta1.dll

## Methods 

### CreateInstance(CreateInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateInstance(CreateInstanceRequest request, ServerCallContext context)

Creates a Redis instance based on the specified tier and memory size.

By default, the instance is accessible from the project's [default network](https://cloud.google.com/vpc/docs/vpc).

The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis instance will be fully functional. The completed longrunning.Operation will contain the new instance object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CreateInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteInstance(DeleteInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteInstance(DeleteInstanceRequest request, ServerCallContext context)

Deletes a specific Redis instance. Instance stops serving and data is deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.DeleteInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportInstance(ExportInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportInstance(ExportInstanceRequest request, ServerCallContext context)

Export Redis instance data into a Redis RDB format file in Cloud Storage.

Redis will continue serving during this operation.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ExportInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### FailoverInstance(FailoverInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> FailoverInstance(FailoverInstanceRequest request, ServerCallContext context)

Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.FailoverInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetInstance(GetInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Instance> GetInstance(GetInstanceRequest request, ServerCallContext context)

Gets the details of a specific Redis instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)` | The response to send back to the client (wrapped by a task).  
  
### GetInstanceAuthString(GetInstanceAuthStringRequest, ServerCallContext)
    
    
    public virtual Task<InstanceAuthString> GetInstanceAuthString(GetInstanceAuthStringRequest request, ServerCallContext context)

Gets the AUTH string for a Redis instance. If AUTH is not enabled for the instance the response will be empty. This information is not included in the details returned to GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceAuthStringRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.GetInstanceAuthStringRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceAuthString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceAuthString)` | The response to send back to the client (wrapped by a task).  
  
### ImportInstance(ImportInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ImportInstance(ImportInstanceRequest request, ServerCallContext context)

Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.

Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ImportInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ListInstances(ListInstancesRequest, ServerCallContext)
    
    
    public virtual Task<ListInstancesResponse> ListInstances(ListInstancesRequest request, ServerCallContext context)

Lists all Redis instances owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesResponse)` | The response to send back to the client (wrapped by a task).  
  
### RescheduleMaintenance(RescheduleMaintenanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> RescheduleMaintenance(RescheduleMaintenanceRequest request, ServerCallContext context)

Reschedule maintenance for a given instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.RescheduleMaintenanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateInstance(UpdateInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateInstance(UpdateInstanceRequest request, ServerCallContext context)

Updates the metadata and configuration of a specific Redis instance.

Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpdateInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpgradeInstance(UpgradeInstanceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpgradeInstance(UpgradeInstanceRequest request, ServerCallContext context)

Upgrades Redis instance to the newer Redis version specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.UpgradeInstanceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
