---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportCompletionSuggestionsMetadata
title: Discovery Engine v1beta API - Class ImportCompletionSuggestionsMetadata (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:28.460644+00:00
---

# Discovery Engine v1beta API - Class ImportCompletionSuggestionsMetadata (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportCompletionSuggestionsMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class ImportCompletionSuggestionsMetadata (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class ImportCompletionSuggestionsMetadata : IMessage<ImportCompletionSuggestionsMetadata>, IEquatable<ImportCompletionSuggestionsMetadata>, IDeepCloneable<ImportCompletionSuggestionsMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class ImportCompletionSuggestionsMetadata.

Metadata related to the progress of the ImportCompletionSuggestions operation. This will be returned by the google.longrunning.Operation.metadata field.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImportCompletionSuggestionsMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportCompletionSuggestionsMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportCompletionSuggestionsMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportCompletionSuggestionsMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### ImportCompletionSuggestionsMetadata()
    
    
    public ImportCompletionSuggestionsMetadata()

### ImportCompletionSuggestionsMetadata(ImportCompletionSuggestionsMetadata)
    
    
    public ImportCompletionSuggestionsMetadata(ImportCompletionSuggestionsMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportCompletionSuggestionsMetadata)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Operation create time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### FailureCount
    
    
    public long FailureCount { get; set; }

Count of [CompletionSuggestion][google.cloud.discoveryengine.v1beta.CompletionSuggestion]s that failed to be imported.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### SuccessCount
    
    
    public long SuccessCount { get; set; }

Count of [CompletionSuggestion][google.cloud.discoveryengine.v1beta.CompletionSuggestion]s successfully imported.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Operation last update time. If the operation is done, this is also the finish time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
