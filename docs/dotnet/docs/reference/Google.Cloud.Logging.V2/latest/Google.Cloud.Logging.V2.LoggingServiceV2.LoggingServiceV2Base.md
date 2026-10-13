---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base
title: Google Cloud Logging v2 API - Class LoggingServiceV2.LoggingServiceV2Base (4.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:17.899967+00:00
---

# Google Cloud Logging v2 API - Class LoggingServiceV2.LoggingServiceV2Base (4.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Logging v2 API - Class LoggingServiceV2.LoggingServiceV2Base (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 4.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 4.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.4.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 4.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.3.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 4.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.2.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 4.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.1.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 4.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.0.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.6.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.5.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.4.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.3.0/Google.Cloud.Logging.V2.LoggingServiceV2.LoggingServiceV2Base)


    
    
    [BindServiceMethod(typeof(LoggingServiceV2), "BindService")]
    public abstract class LoggingServiceV2.LoggingServiceV2Base

Reference documentation and code samples for the Google Cloud Logging v2 API class LoggingServiceV2.LoggingServiceV2Base.

Base class for server-side implementations of LoggingServiceV2

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LoggingServiceV2.LoggingServiceV2Base

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Logging.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2)

## Assembly

Google.Cloud.Logging.V2.dll

## Methods 

### DeleteLog(DeleteLogRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteLog(DeleteLogRequest request, ServerCallContext context)

Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteLogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.DeleteLogRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### ListLogEntries(ListLogEntriesRequest, ServerCallContext)
    
    
    public virtual Task<ListLogEntriesResponse> ListLogEntries(ListLogEntriesRequest request, ServerCallContext context)

Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see [Exporting Logs](https://cloud.google.com/logging/docs/export).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLogEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.ListLogEntriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListLogEntriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.ListLogEntriesResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListLogs(ListLogsRequest, ServerCallContext)
    
    
    public virtual Task<ListLogsResponse> ListLogs(ListLogsRequest request, ServerCallContext context)

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.ListLogsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListLogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.ListLogsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListMonitoredResourceDescriptors(ListMonitoredResourceDescriptorsRequest, ServerCallContext)
    
    
    public virtual Task<ListMonitoredResourceDescriptorsResponse> ListMonitoredResourceDescriptors(ListMonitoredResourceDescriptorsRequest request, ServerCallContext context)

Lists the descriptors for monitored resource types used by Logging.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.ListMonitoredResourceDescriptorsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListMonitoredResourceDescriptorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.ListMonitoredResourceDescriptorsResponse)` | The response to send back to the client (wrapped by a task).  
  
### TailLogEntries(IAsyncStreamReader<TailLogEntriesRequest>, IServerStreamWriter<TailLogEntriesResponse>, ServerCallContext)
    
    
    public virtual Task TailLogEntries(IAsyncStreamReader<TailLogEntriesRequest> requestStream, IServerStreamWriter<TailLogEntriesResponse> responseStream, ServerCallContext context)

Streaming read of log entries as they are ingested. Until the stream is terminated, it will continue reading logs.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[TailLogEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.TailLogEntriesRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[TailLogEntriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.TailLogEntriesResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### WriteLogEntries(WriteLogEntriesRequest, ServerCallContext)
    
    
    public virtual Task<WriteLogEntriesResponse> WriteLogEntries(WriteLogEntriesRequest request, ServerCallContext context)

Writes log entries to Logging. This API method is the only way to send log entries to Logging. This method is used, directly or indirectly, by the Logging agent (fluentd) and all logging libraries configured to use Logging. A single request may contain log entries for a maximum of 1000 different resources (projects, organizations, billing accounts or folders)

**Parameters**  
---  
**Name** | **Description**  
`request` | `[WriteLogEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.WriteLogEntriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[WriteLogEntriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.WriteLogEntriesResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
