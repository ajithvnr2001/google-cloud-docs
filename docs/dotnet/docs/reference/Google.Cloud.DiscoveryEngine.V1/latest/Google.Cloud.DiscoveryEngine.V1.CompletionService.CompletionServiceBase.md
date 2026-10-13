---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CompletionService.CompletionServiceBase
title: Discovery Engine v1 API - Class CompletionService.CompletionServiceBase (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:18.748111+00:00
---

# Discovery Engine v1 API - Class CompletionService.CompletionServiceBase (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CompletionService.CompletionServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class CompletionService.CompletionServiceBase (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    [BindServiceMethod(typeof(CompletionService), "BindService")]
    public abstract class CompletionService.CompletionServiceBase

Reference documentation and code samples for the Discovery Engine v1 API class CompletionService.CompletionServiceBase.

Base class for server-side implementations of CompletionService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CompletionService.CompletionServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Methods 

### CompleteQuery(CompleteQueryRequest, ServerCallContext)
    
    
    public virtual Task<CompleteQueryResponse> CompleteQuery(CompleteQueryRequest request, ServerCallContext context)

Completes the specified user input with keyword suggestions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CompleteQueryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompleteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CompleteQueryResponse)` | The response to send back to the client (wrapped by a task).  
  
### ImportCompletionSuggestions(ImportCompletionSuggestionsRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ImportCompletionSuggestions(ImportCompletionSuggestionsRequest request, ServerCallContext context)

Imports [CompletionSuggestion][google.cloud.discoveryengine.v1.CompletionSuggestion]s for a DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportCompletionSuggestionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ImportSuggestionDenyListEntries(ImportSuggestionDenyListEntriesRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ImportSuggestionDenyListEntries(ImportSuggestionDenyListEntriesRequest request, ServerCallContext context)

Imports all [SuggestionDenyListEntry][google.cloud.discoveryengine.v1.SuggestionDenyListEntry] for a DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportSuggestionDenyListEntriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### PurgeCompletionSuggestions(PurgeCompletionSuggestionsRequest, ServerCallContext)
    
    
    public virtual Task<Operation> PurgeCompletionSuggestions(PurgeCompletionSuggestionsRequest request, ServerCallContext context)

Permanently deletes all [CompletionSuggestion][google.cloud.discoveryengine.v1.CompletionSuggestion]s for a DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeCompletionSuggestionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### PurgeSuggestionDenyListEntries(PurgeSuggestionDenyListEntriesRequest, ServerCallContext)
    
    
    public virtual Task<Operation> PurgeSuggestionDenyListEntries(PurgeSuggestionDenyListEntriesRequest request, ServerCallContext context)

Permanently deletes all [SuggestionDenyListEntry][google.cloud.discoveryengine.v1.SuggestionDenyListEntry] for a DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeSuggestionDenyListEntriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
