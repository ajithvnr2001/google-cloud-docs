---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.DnsThreatDetectorService.DnsThreatDetectorServiceBase
title: Network Security v1beta1 API - Class DnsThreatDetectorService.DnsThreatDetectorServiceBase (2.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:54.500533+00:00
---

# Network Security v1beta1 API - Class DnsThreatDetectorService.DnsThreatDetectorServiceBase (2.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.DnsThreatDetectorService.DnsThreatDetectorServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1beta1 API - Class DnsThreatDetectorService.DnsThreatDetectorServiceBase (2.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.DnsThreatDetectorService.DnsThreatDetectorServiceBase)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/2.0.0-beta07/Google.Cloud.NetworkSecurity.V1Beta1.DnsThreatDetectorService.DnsThreatDetectorServiceBase)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/1.0.0-beta02/Google.Cloud.NetworkSecurity.V1Beta1.DnsThreatDetectorService.DnsThreatDetectorServiceBase)


    
    
    [BindServiceMethod(typeof(DnsThreatDetectorService), "BindService")]
    public abstract class DnsThreatDetectorService.DnsThreatDetectorServiceBase

Reference documentation and code samples for the Network Security v1beta1 API class DnsThreatDetectorService.DnsThreatDetectorServiceBase.

Base class for server-side implementations of DnsThreatDetectorService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DnsThreatDetectorService.DnsThreatDetectorServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkSecurity.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1)

## Assembly

Google.Cloud.NetworkSecurity.V1Beta1.dll

## Methods 

### CreateDnsThreatDetector(CreateDnsThreatDetectorRequest, ServerCallContext)
    
    
    public virtual Task<DnsThreatDetector> CreateDnsThreatDetector(CreateDnsThreatDetectorRequest request, ServerCallContext context)

Creates a new DnsThreatDetector in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDnsThreatDetectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateDnsThreatDetectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DnsThreatDetector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.DnsThreatDetector)` | The response to send back to the client (wrapped by a task).  
  
### DeleteDnsThreatDetector(DeleteDnsThreatDetectorRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteDnsThreatDetector(DeleteDnsThreatDetectorRequest request, ServerCallContext context)

Deletes a single DnsThreatDetector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDnsThreatDetectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.DeleteDnsThreatDetectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetDnsThreatDetector(GetDnsThreatDetectorRequest, ServerCallContext)
    
    
    public virtual Task<DnsThreatDetector> GetDnsThreatDetector(GetDnsThreatDetectorRequest request, ServerCallContext context)

Gets the details of a single DnsThreatDetector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDnsThreatDetectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.GetDnsThreatDetectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DnsThreatDetector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.DnsThreatDetector)` | The response to send back to the client (wrapped by a task).  
  
### ListDnsThreatDetectors(ListDnsThreatDetectorsRequest, ServerCallContext)
    
    
    public virtual Task<ListDnsThreatDetectorsResponse> ListDnsThreatDetectors(ListDnsThreatDetectorsRequest request, ServerCallContext context)

Lists DnsThreatDetectors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDnsThreatDetectorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ListDnsThreatDetectorsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListDnsThreatDetectorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ListDnsThreatDetectorsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateDnsThreatDetector(UpdateDnsThreatDetectorRequest, ServerCallContext)
    
    
    public virtual Task<DnsThreatDetector> UpdateDnsThreatDetector(UpdateDnsThreatDetectorRequest request, ServerCallContext context)

Updates a single DnsThreatDetector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDnsThreatDetectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.UpdateDnsThreatDetectorRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DnsThreatDetector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.DnsThreatDetector)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
