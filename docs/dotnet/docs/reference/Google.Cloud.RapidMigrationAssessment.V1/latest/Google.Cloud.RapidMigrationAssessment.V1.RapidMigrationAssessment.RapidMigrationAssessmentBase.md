---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessment.RapidMigrationAssessmentBase
title: Rapid Migration Assessment v1 API - Class RapidMigrationAssessment.RapidMigrationAssessmentBase (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:41.330581+00:00
---

# Rapid Migration Assessment v1 API - Class RapidMigrationAssessment.RapidMigrationAssessmentBase (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessment.RapidMigrationAssessmentBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Rapid Migration Assessment v1 API - Class RapidMigrationAssessment.RapidMigrationAssessmentBase (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessment.RapidMigrationAssessmentBase)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/1.2.0/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessment.RapidMigrationAssessmentBase)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/1.1.0/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessment.RapidMigrationAssessmentBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/1.0.0/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessment.RapidMigrationAssessmentBase)


    
    
    [BindServiceMethod(typeof(RapidMigrationAssessment), "BindService")]
    public abstract class RapidMigrationAssessment.RapidMigrationAssessmentBase

Reference documentation and code samples for the Rapid Migration Assessment v1 API class RapidMigrationAssessment.RapidMigrationAssessmentBase.

Base class for server-side implementations of RapidMigrationAssessment

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RapidMigrationAssessment.RapidMigrationAssessmentBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RapidMigrationAssessment.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1)

## Assembly

Google.Cloud.RapidMigrationAssessment.V1.dll

## Methods 

### CreateAnnotation(CreateAnnotationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateAnnotation(CreateAnnotationRequest request, ServerCallContext context)

Creates an Annotation

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.CreateAnnotationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateCollector(CreateCollectorRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateCollector(CreateCollectorRequest request, ServerCallContext context)

Create a Collector to manage the on-prem appliance which collects information about Customer assets.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCollectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.CreateCollectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteCollector(DeleteCollectorRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteCollector(DeleteCollectorRequest request, ServerCallContext context)

Deletes a single Collector - changes state of collector to "Deleting". Background jobs does final deletion through producer API.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCollectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.DeleteCollectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetAnnotation(GetAnnotationRequest, ServerCallContext)
    
    
    public virtual Task<Annotation> GetAnnotation(GetAnnotationRequest request, ServerCallContext context)

Gets details of a single Annotation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.GetAnnotationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.Annotation)` | The response to send back to the client (wrapped by a task).  
  
### GetCollector(GetCollectorRequest, ServerCallContext)
    
    
    public virtual Task<Collector> GetCollector(GetCollectorRequest request, ServerCallContext context)

Gets details of a single Collector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCollectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.GetCollectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.Collector)` | The response to send back to the client (wrapped by a task).  
  
### ListCollectors(ListCollectorsRequest, ServerCallContext)
    
    
    public virtual Task<ListCollectorsResponse> ListCollectors(ListCollectorsRequest request, ServerCallContext context)

Lists Collectors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCollectorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.ListCollectorsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListCollectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.ListCollectorsResponse)` | The response to send back to the client (wrapped by a task).  
  
### PauseCollector(PauseCollectorRequest, ServerCallContext)
    
    
    public virtual Task<Operation> PauseCollector(PauseCollectorRequest request, ServerCallContext context)

Pauses the given collector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseCollectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.PauseCollectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### RegisterCollector(RegisterCollectorRequest, ServerCallContext)
    
    
    public virtual Task<Operation> RegisterCollector(RegisterCollectorRequest request, ServerCallContext context)

Registers the given collector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RegisterCollectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RegisterCollectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ResumeCollector(ResumeCollectorRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ResumeCollector(ResumeCollectorRequest request, ServerCallContext context)

Resumes the given collector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeCollectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.ResumeCollectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateCollector(UpdateCollectorRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateCollector(UpdateCollectorRequest request, ServerCallContext context)

Updates the parameters of a single Collector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCollectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.UpdateCollectorRequest)`  
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
