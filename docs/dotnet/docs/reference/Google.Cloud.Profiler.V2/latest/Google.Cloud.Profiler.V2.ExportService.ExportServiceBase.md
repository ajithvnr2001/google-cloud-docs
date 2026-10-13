---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase
title: Cloud Profiler v2 API - Class ExportService.ExportServiceBase (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:21.142554+00:00
---

# Cloud Profiler v2 API - Class ExportService.ExportServiceBase (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Profiler v2 API - Class ExportService.ExportServiceBase (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.6.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.5.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.4.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.3.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.2.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.1.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/2.0.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.2.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.1.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/1.0.0/Google.Cloud.Profiler.V2.ExportService.ExportServiceBase)


    
    
    [BindServiceMethod(typeof(ExportService), "BindService")]
    public abstract class ExportService.ExportServiceBase

Reference documentation and code samples for the Cloud Profiler v2 API class ExportService.ExportServiceBase.

Base class for server-side implementations of ExportService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExportService.ExportServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Profiler.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2)

## Assembly

Google.Cloud.Profiler.V2.dll

## Methods 

### ListProfiles(ListProfilesRequest, ServerCallContext)
    
    
    public virtual Task<ListProfilesResponse> ListProfiles(ListProfilesRequest request, ServerCallContext context)

Lists profiles which have been collected so far and for which the caller has permission to view.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Profiler.V2/latest/Google.Cloud.Profiler.V2.ListProfilesResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
