---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Lineage.LineageBase
title: Data Lineage v1 API - Class Lineage.LineageBase (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:35.351173+00:00
---

# Data Lineage v1 API - Class Lineage.LineageBase (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Lineage.LineageBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Lineage v1 API - Class Lineage.LineageBase (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    [BindServiceMethod(typeof(Lineage), "BindService")]
    public abstract class Lineage.LineageBase

Reference documentation and code samples for the Data Lineage v1 API class Lineage.LineageBase.

Base class for server-side implementations of Lineage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Lineage.LineageBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1)

## Assembly

Google.Cloud.DataCatalog.Lineage.V1.dll

## Methods 

### BatchSearchLinkProcesses(BatchSearchLinkProcessesRequest, ServerCallContext)
    
    
    public virtual Task<BatchSearchLinkProcessesResponse> BatchSearchLinkProcesses(BatchSearchLinkProcessesRequest request, ServerCallContext context)

Retrieve information about LineageProcesses associated with specific links. LineageProcesses are transformation pipelines that result in data flowing from **source** to **target** assets. Links between assets represent this operation.

If you have specific link names, you can use this method to verify which LineageProcesses contribute to creating those links. See the [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks] method for more information on how to retrieve link name.

You can retrieve the LineageProcess information in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.BatchSearchLinkProcessesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchSearchLinkProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.BatchSearchLinkProcessesResponse)` | The response to send back to the client (wrapped by a task).  
  
### CreateLineageEvent(CreateLineageEventRequest, ServerCallContext)
    
    
    public virtual Task<LineageEvent> CreateLineageEvent(CreateLineageEventRequest request, ServerCallContext context)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | The response to send back to the client (wrapped by a task).  
  
### CreateProcess(CreateProcessRequest, ServerCallContext)
    
    
    public virtual Task<Process> CreateProcess(CreateProcessRequest request, ServerCallContext context)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateProcessRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The response to send back to the client (wrapped by a task).  
  
### CreateRun(CreateRunRequest, ServerCallContext)
    
    
    public virtual Task<Run> CreateRun(CreateRunRequest request, ServerCallContext context)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateRunRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The response to send back to the client (wrapped by a task).  
  
### DeleteLineageEvent(DeleteLineageEventRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteLineageEvent(DeleteLineageEventRequest request, ServerCallContext context)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteLineageEventRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteProcess(DeleteProcessRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteProcess(DeleteProcessRequest request, ServerCallContext context)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteProcessRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteRun(DeleteRunRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteRun(DeleteRunRequest request, ServerCallContext context)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteRunRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetLineageEvent(GetLineageEventRequest, ServerCallContext)
    
    
    public virtual Task<LineageEvent> GetLineageEvent(GetLineageEventRequest request, ServerCallContext context)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetLineageEventRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | The response to send back to the client (wrapped by a task).  
  
### GetProcess(GetProcessRequest, ServerCallContext)
    
    
    public virtual Task<Process> GetProcess(GetProcessRequest request, ServerCallContext context)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetProcessRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The response to send back to the client (wrapped by a task).  
  
### GetRun(GetRunRequest, ServerCallContext)
    
    
    public virtual Task<Run> GetRun(GetRunRequest request, ServerCallContext context)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetRunRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The response to send back to the client (wrapped by a task).  
  
### ListLineageEvents(ListLineageEventsRequest, ServerCallContext)
    
    
    public virtual Task<ListLineageEventsResponse> ListLineageEvents(ListLineageEventsRequest request, ServerCallContext context)

Lists lineage events in the given project and location. The list order is not defined.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLineageEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListLineageEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListProcesses(ListProcessesRequest, ServerCallContext)
    
    
    public virtual Task<ListProcessesResponse> ListProcesses(ListProcessesRequest request, ServerCallContext context)

List processes in the given project and location. List order is descending by insertion time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListRuns(ListRunsRequest, ServerCallContext)
    
    
    public virtual Task<ListRunsResponse> ListRuns(ListRunsRequest request, ServerCallContext context)

Lists runs in the given project and location. List order is descending by `start_time`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRunsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ProcessOpenLineageRunEvent(ProcessOpenLineageRunEventRequest, ServerCallContext)
    
    
    public virtual Task<ProcessOpenLineageRunEventResponse> ProcessOpenLineageRunEvent(ProcessOpenLineageRunEventRequest request, ServerCallContext context)

Creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProcessOpenLineageRunEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse)` | The response to send back to the client (wrapped by a task).  
  
### SearchLineageStreaming(SearchLineageStreamingRequest, IServerStreamWriter<SearchLineageStreamingResponse>, ServerCallContext)
    
    
    public virtual Task SearchLineageStreaming(SearchLineageStreamingRequest request, IServerStreamWriter<SearchLineageStreamingResponse> responseStream, ServerCallContext context)

Retrieves a streaming response of lineage links connected to the requested assets by performing a breadth-first search in the given direction. Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them. This method retrieves links from all valid locations provided in the request. This method supports Column-Level Lineage (CLL) along with wildcard support to retrieve all CLL for an Entity FQN.

Following permissions are required to retrieve links:

  * `datalineage.events.get` permission for the project where the link is stored for entity-level lineage.
  * `datalineage.events.getFields` permission for the project where the link is stored for column-level lineage.



This method also returns processes that created the links if explicitly requested by setting [max_process_per_link](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.limits.max_process_per_link) is non-zero and full process details are requested via `links.processes.process` in the [FieldMask](https://developers.google.com/workspace/docs/api/how-tos/field-masks#read_with_a_field_mask).

Permission required to retrieve processes:

  * `datalineage.processes.get` permission for the project where the process is stored.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)`  
The request received from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[SearchLineageStreamingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### SearchLinks(SearchLinksRequest, ServerCallContext)
    
    
    public virtual Task<SearchLinksResponse> SearchLinks(SearchLinksRequest request, ServerCallContext context)

Retrieve a list of links connected to a specific asset. Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them.

You can retrieve links in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchLinksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchLinksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateProcess(UpdateProcessRequest, ServerCallContext)
    
    
    public virtual Task<Process> UpdateProcess(UpdateProcessRequest request, ServerCallContext context)

Updates a process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.UpdateProcessRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The response to send back to the client (wrapped by a task).  
  
### UpdateRun(UpdateRunRequest, ServerCallContext)
    
    
    public virtual Task<Run> UpdateRun(UpdateRunRequest request, ServerCallContext context)

Updates a run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.UpdateRunRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
