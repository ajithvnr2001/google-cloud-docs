---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate
title: Vertex AI v1beta1 API - Class Candidate (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:45.476597+00:00
---

# Vertex AI v1beta1 API - Class Candidate (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class Candidate (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class Candidate : IMessage<Candidate>, IEquatable<Candidate>, IDeepCloneable<Candidate>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class Candidate.

A response candidate generated from the model.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Candidate

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Candidate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Candidate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Candidate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### Candidate()
    
    
    public Candidate()

### Candidate(Candidate)
    
    
    public Candidate(Candidate other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Candidate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate)`  
  
  
## Properties 

### AvgLogprobs
    
    
    public double AvgLogprobs { get; set; }

Output only. Average log probability score of the candidate.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### CitationMetadata
    
    
    public CitationMetadata CitationMetadata { get; set; }

Output only. Source attribution of the generated content.

**Property Value**  
---  
**Type** | **Description**  
`[CitationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CitationMetadata)` |   
  
### Content
    
    
    public Content Content { get; set; }

Output only. Content parts of the candidate.

**Property Value**  
---  
**Type** | **Description**  
`[Content](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Content)` |   
  
### FinishMessage
    
    
    public string FinishMessage { get; set; }

Output only. Describes the reason the mode stopped generating tokens in more detail. This is only filled when `finish_reason` is set.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FinishReason
    
    
    public Candidate.Types.FinishReason FinishReason { get; set; }

Output only. The reason why the model stopped generating tokens. If empty, the model has not stopped generating the tokens.

**Property Value**  
---  
**Type** | **Description**  
`[Candidate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate.Types)[FinishReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Candidate.Types.FinishReason)` |   
  
### GroundingMetadata
    
    
    public GroundingMetadata GroundingMetadata { get; set; }

Output only. Metadata specifies sources used to ground generated content.

**Property Value**  
---  
**Type** | **Description**  
`[GroundingMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GroundingMetadata)` |   
  
### HasFinishMessage
    
    
    public bool HasFinishMessage { get; }

Gets whether the "finish_message" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Index
    
    
    public int Index { get; set; }

Output only. Index of the candidate.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LogprobsResult
    
    
    public LogprobsResult LogprobsResult { get; set; }

Output only. Log-likelihood scores for the response tokens and top tokens

**Property Value**  
---  
**Type** | **Description**  
`[LogprobsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.LogprobsResult)` |   
  
### SafetyRatings
    
    
    public RepeatedField<SafetyRating> SafetyRatings { get; }

Output only. List of ratings for the safety of a response candidate.

There is at most one rating per category.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SafetyRating](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SafetyRating)` |   
  
### UrlContextMetadata
    
    
    public UrlContextMetadata UrlContextMetadata { get; set; }

Output only. Metadata related to url context retrieval tool.

**Property Value**  
---  
**Type** | **Description**  
`[UrlContextMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UrlContextMetadata)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
