---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec
title: Discovery Engine v1beta API - Class AnswerQueryRequest.Types.AnswerGenerationSpec (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:47.240883+00:00
---

# Discovery Engine v1beta API - Class AnswerQueryRequest.Types.AnswerGenerationSpec (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class AnswerQueryRequest.Types.AnswerGenerationSpec (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class AnswerQueryRequest.Types.AnswerGenerationSpec : IMessage<AnswerQueryRequest.Types.AnswerGenerationSpec>, IEquatable<AnswerQueryRequest.Types.AnswerGenerationSpec>, IDeepCloneable<AnswerQueryRequest.Types.AnswerGenerationSpec>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class AnswerQueryRequest.Types.AnswerGenerationSpec.

Answer generation specification.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnswerQueryRequest.Types.AnswerGenerationSpec

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### AnswerGenerationSpec()
    
    
    public AnswerGenerationSpec()

### AnswerGenerationSpec(AnswerGenerationSpec)
    
    
    public AnswerGenerationSpec(AnswerQueryRequest.Types.AnswerGenerationSpec other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec)`  
  
  
## Properties 

### AnswerLanguageCode
    
    
    public string AnswerLanguageCode { get; set; }

Language code for Answer. Use language tags defined by [BCP47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). Note: This is an experimental feature.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasIgnoreLowRelevantContent
    
    
    public bool HasIgnoreLowRelevantContent { get; }

Gets whether the "ignore_low_relevant_content" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IgnoreAdversarialQuery
    
    
    public bool IgnoreAdversarialQuery { get; set; }

Specifies whether to filter out adversarial queries. The default value is `false`.

Google employs search-query classification to detect adversarial queries. No answer is returned if the search query is classified as an adversarial query. For example, a user might ask a question regarding negative comments about the company or submit a query designed to generate unsafe, policy-violating output. If this field is set to `true`, we skip generating answers for adversarial queries and return fallback messages instead.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IgnoreJailBreakingQuery
    
    
    public bool IgnoreJailBreakingQuery { get; set; }

Optional. Specifies whether to filter out jail-breaking queries. The default value is `false`.

Google employs search-query classification to detect jail-breaking queries. No summary is returned if the search query is classified as a jail-breaking query. A user might add instructions to the query to change the tone, style, language, content of the answer, or ask the model to act as a different entity, e.g. "Reply in the tone of a competing company's CEO". If this field is set to `true`, we skip generating summaries for jail-breaking queries and return fallback messages instead.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IgnoreLowRelevantContent
    
    
    public bool IgnoreLowRelevantContent { get; set; }

Specifies whether to filter out queries that have low relevance.

If this field is set to `false`, all search results are used regardless of relevance to generate answers. If set to `true` or unset, the behavior will be determined automatically by the service.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IgnoreNonAnswerSeekingQuery
    
    
    public bool IgnoreNonAnswerSeekingQuery { get; set; }

Specifies whether to filter out queries that are not answer-seeking. The default value is `false`.

Google employs search-query classification to detect answer-seeking queries. No answer is returned if the search query is classified as a non-answer seeking query. If this field is set to `true`, we skip generating answers for non-answer seeking queries and return fallback messages instead.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IncludeCitations
    
    
    public bool IncludeCitations { get; set; }

Specifies whether to include citation metadata in the answer. The default value is `false`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ModelSpec
    
    
    public AnswerQueryRequest.Types.AnswerGenerationSpec.Types.ModelSpec ModelSpec { get; set; }

Answer generation model specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec.Types)[ModelSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec.Types.ModelSpec)` |   
  
### MultimodalSpec
    
    
    public AnswerQueryRequest.Types.AnswerGenerationSpec.Types.MultimodalSpec MultimodalSpec { get; set; }

Optional. Multimodal specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec.Types)[MultimodalSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec.Types.MultimodalSpec)` |   
  
### PromptSpec
    
    
    public AnswerQueryRequest.Types.AnswerGenerationSpec.Types.PromptSpec PromptSpec { get; set; }

Answer generation prompt specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types)[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec.Types)[PromptSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerQueryRequest.Types.AnswerGenerationSpec.Types.PromptSpec)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
