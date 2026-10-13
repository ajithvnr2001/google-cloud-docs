---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CompletionService.CompletionServiceBase
title: Discovery Engine v1beta API - Class CompletionService.CompletionServiceBase (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:25.444798+00:00
---

# Discovery Engine v1beta API - Class CompletionService.CompletionServiceBase (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CompletionService.CompletionServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class CompletionService.CompletionServiceBase (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    [BindServiceMethod(typeof(CompletionService), "BindService")]
    public abstract class CompletionService.CompletionServiceBase

Reference documentation and code samples for the Discovery Engine v1beta API class CompletionService.CompletionServiceBase.

Base class for server-side implementations of CompletionService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CompletionService.CompletionServiceBase

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

### AdvancedCompleteQuery(AdvancedCompleteQueryRequest, ServerCallContext)
    
    
    public virtual Task<AdvancedCompleteQueryResponse> AdvancedCompleteQuery(AdvancedCompleteQueryRequest request, ServerCallContext context)

Completes the user input with advanced keyword suggestions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AdvancedCompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AdvancedCompleteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryResponse)` | The response to send back to the client (wrapped by a task).  
  
### CompleteQuery(CompleteQueryRequest, ServerCallContext)
    
    
    public virtual Task<CompleteQueryResponse> CompleteQuery(CompleteQueryRequest request, ServerCallContext context)

Completes the specified user input with keyword suggestions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CompleteQueryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompleteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CompleteQueryResponse)` | The response to send back to the client (wrapped by a task).  
  
### ImportCompletionSuggestions(ImportCompletionSuggestionsRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ImportCompletionSuggestions(ImportCompletionSuggestionsRequest request, ServerCallContext context)

Imports [CompletionSuggestion][google.cloud.discoveryengine.v1beta.CompletionSuggestion]s for a DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportCompletionSuggestionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ImportSuggestionDenyListEntries(ImportSuggestionDenyListEntriesRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ImportSuggestionDenyListEntries(ImportSuggestionDenyListEntriesRequest request, ServerCallContext context)

Imports all [SuggestionDenyListEntry][google.cloud.discoveryengine.v1beta.SuggestionDenyListEntry] for a DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportSuggestionDenyListEntriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### PurgeCompletionSuggestions(PurgeCompletionSuggestionsRequest, ServerCallContext)
    
    
    public virtual Task<Operation> PurgeCompletionSuggestions(PurgeCompletionSuggestionsRequest request, ServerCallContext context)

Permanently deletes all [CompletionSuggestion][google.cloud.discoveryengine.v1beta.CompletionSuggestion]s for a DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeCompletionSuggestionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### PurgeSuggestionDenyListEntries(PurgeSuggestionDenyListEntriesRequest, ServerCallContext)
    
    
    public virtual Task<Operation> PurgeSuggestionDenyListEntries(PurgeSuggestionDenyListEntriesRequest request, ServerCallContext context)

Permanently deletes all [SuggestionDenyListEntry][google.cloud.discoveryengine.v1beta.SuggestionDenyListEntry] for a DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeSuggestionDenyListEntriesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### RemoveSuggestion(RemoveSuggestionRequest, ServerCallContext)
    
    
    public virtual Task<RemoveSuggestionResponse> RemoveSuggestion(RemoveSuggestionRequest request, ServerCallContext context)

Removes the search history suggestion in an engine for a user. This will remove the suggestion from being returned in the [AdvancedCompleteQueryResponse.recent_search_suggestions][google.cloud.discoveryengine.v1beta.AdvancedCompleteQueryResponse.recent_search_suggestions] for this user. If the user searches the same suggestion again, the new history will override and suggest this suggestion again.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveSuggestionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RemoveSuggestionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveSuggestionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.RemoveSuggestionResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
