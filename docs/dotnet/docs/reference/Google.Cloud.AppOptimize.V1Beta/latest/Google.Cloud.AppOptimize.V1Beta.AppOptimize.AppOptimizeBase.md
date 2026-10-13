---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimize.AppOptimizeBase
title: App Optimize v1beta API - Class AppOptimize.AppOptimizeBase (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:59.351674+00:00
---

# App Optimize v1beta API - Class AppOptimize.AppOptimizeBase (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimize.AppOptimizeBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Optimize v1beta API - Class AppOptimize.AppOptimizeBase (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    [BindServiceMethod(typeof(AppOptimize), "BindService")]
    public abstract class AppOptimize.AppOptimizeBase

Reference documentation and code samples for the App Optimize v1beta API class AppOptimize.AppOptimizeBase.

Base class for server-side implementations of AppOptimize

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AppOptimize.AppOptimizeBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AppOptimize.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta)

## Assembly

Google.Cloud.AppOptimize.V1Beta.dll

## Methods 

### CreateReport(CreateReportRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateReport(CreateReportRequest request, ServerCallContext context)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.CreateReportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteReport(DeleteReportRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteReport(DeleteReportRequest request, ServerCallContext context)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.DeleteReportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetReport(GetReportRequest, ServerCallContext)
    
    
    public virtual Task<Report> GetReport(GetReportRequest request, ServerCallContext context)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.GetReportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | The response to send back to the client (wrapped by a task).  
  
### ListReports(ListReportsRequest, ServerCallContext)
    
    
    public virtual Task<ListReportsResponse> ListReports(ListReportsRequest request, ServerCallContext context)

Lists reports within a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ReadReport(ReadReportRequest, ServerCallContext)
    
    
    public virtual Task<ReadReportResponse> ReadReport(ReadReportRequest request, ServerCallContext context)

Reads data within a specified report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadReportResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
