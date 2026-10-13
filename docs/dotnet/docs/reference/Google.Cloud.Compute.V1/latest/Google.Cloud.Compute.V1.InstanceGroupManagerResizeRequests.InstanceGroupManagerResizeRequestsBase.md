---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequests.InstanceGroupManagerResizeRequestsBase
title: Compute Engine v1 API - Class InstanceGroupManagerResizeRequests.InstanceGroupManagerResizeRequestsBase (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:41.226546+00:00
---

# Compute Engine v1 API - Class InstanceGroupManagerResizeRequests.InstanceGroupManagerResizeRequestsBase (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequests.InstanceGroupManagerResizeRequestsBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class InstanceGroupManagerResizeRequests.InstanceGroupManagerResizeRequestsBase (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    [BindServiceMethod(typeof(InstanceGroupManagerResizeRequests), "BindService")]
    public abstract class InstanceGroupManagerResizeRequests.InstanceGroupManagerResizeRequestsBase

Reference documentation and code samples for the Compute Engine v1 API class InstanceGroupManagerResizeRequests.InstanceGroupManagerResizeRequestsBase.

Base class for server-side implementations of InstanceGroupManagerResizeRequests

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InstanceGroupManagerResizeRequests.InstanceGroupManagerResizeRequestsBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Methods 

### Cancel(CancelInstanceGroupManagerResizeRequestRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Cancel(CancelInstanceGroupManagerResizeRequestRequest request, ServerCallContext context)

Cancels the specified resize request and removes it from the queue. Cancelled resize request does no longer wait for the resources to be provisioned. Cancel is only possible for requests that are accepted in the queue.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CancelInstanceGroupManagerResizeRequestRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### Delete(DeleteInstanceGroupManagerResizeRequestRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Delete(DeleteInstanceGroupManagerResizeRequestRequest request, ServerCallContext context)

Deletes the specified, inactive resize request. Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteInstanceGroupManagerResizeRequestRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### Get(GetInstanceGroupManagerResizeRequestRequest, ServerCallContext)
    
    
    public virtual Task<InstanceGroupManagerResizeRequest> Get(GetInstanceGroupManagerResizeRequestRequest request, ServerCallContext context)

Returns all of the details about the specified resize request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetInstanceGroupManagerResizeRequestRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceGroupManagerResizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequest)` | The response to send back to the client (wrapped by a task).  
  
### Insert(InsertInstanceGroupManagerResizeRequestRequest, ServerCallContext)
    
    
    public virtual Task<Operation> Insert(InsertInstanceGroupManagerResizeRequestRequest request, ServerCallContext context)

Creates a new resize request that starts provisioning VMs immediately or queues VM creation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertInstanceGroupManagerResizeRequestRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### List(ListInstanceGroupManagerResizeRequestsRequest, ServerCallContext)
    
    
    public virtual Task<InstanceGroupManagerResizeRequestsListResponse> List(ListInstanceGroupManagerResizeRequestsRequest request, ServerCallContext context)

Retrieves a list of resize requests that are contained in the managed instance group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstanceGroupManagerResizeRequestsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListInstanceGroupManagerResizeRequestsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[InstanceGroupManagerResizeRequestsListResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequestsListResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
