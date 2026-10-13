---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SampleQueryService.SampleQueryServiceBase
title: Discovery Engine v1beta API - Class SampleQueryService.SampleQueryServiceBase (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:53.842358+00:00
---

# Discovery Engine v1beta API - Class SampleQueryService.SampleQueryServiceBase (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SampleQueryService.SampleQueryServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class SampleQueryService.SampleQueryServiceBase (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    [BindServiceMethod(typeof(SampleQueryService), "BindService")]
    public abstract class SampleQueryService.SampleQueryServiceBase

Reference documentation and code samples for the Discovery Engine v1beta API class SampleQueryService.SampleQueryServiceBase.

Base class for server-side implementations of SampleQueryService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SampleQueryService.SampleQueryServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Methods 

### CreateSampleQuery(CreateSampleQueryRequest, ServerCallContext)
    
    
    public virtual Task<SampleQuery> CreateSampleQuery(CreateSampleQueryRequest request, ServerCallContext context)

Creates a [SampleQuery][google.cloud.discoveryengine.v1beta.SampleQuery]

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSampleQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateSampleQueryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SampleQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SampleQuery)` | The response to send back to the client (wrapped by a task).  
  
### DeleteSampleQuery(DeleteSampleQueryRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteSampleQuery(DeleteSampleQueryRequest request, ServerCallContext context)

Deletes a [SampleQuery][google.cloud.discoveryengine.v1beta.SampleQuery].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSampleQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteSampleQueryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetSampleQuery(GetSampleQueryRequest, ServerCallContext)
    
    
    public virtual Task<SampleQuery> GetSampleQuery(GetSampleQueryRequest request, ServerCallContext context)

Gets a [SampleQuery][google.cloud.discoveryengine.v1beta.SampleQuery].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSampleQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetSampleQueryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SampleQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SampleQuery)` | The response to send back to the client (wrapped by a task).  
  
### ImportSampleQueries(ImportSampleQueriesRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ImportSampleQueries(ImportSampleQueriesRequest request, ServerCallContext context)

Bulk import of multiple [SampleQuery][google.cloud.discoveryengine.v1beta.SampleQuery]s. Sample queries that already exist may be deleted.

Note: It is possible for a subset of the [SampleQuery][google.cloud.discoveryengine.v1beta.SampleQuery]s to be successfully imported.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportSampleQueriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportSampleQueriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ListSampleQueries(ListSampleQueriesRequest, ServerCallContext)
    
    
    public virtual Task<ListSampleQueriesResponse> ListSampleQueries(ListSampleQueriesRequest request, ServerCallContext context)

Gets a list of [SampleQuery][google.cloud.discoveryengine.v1beta.SampleQuery]s.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSampleQueriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListSampleQueriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListSampleQueriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListSampleQueriesResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateSampleQuery(UpdateSampleQueryRequest, ServerCallContext)
    
    
    public virtual Task<SampleQuery> UpdateSampleQuery(UpdateSampleQueryRequest request, ServerCallContext context)

Updates a [SampleQuery][google.cloud.discoveryengine.v1beta.SampleQuery].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSampleQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateSampleQueryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SampleQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SampleQuery)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
