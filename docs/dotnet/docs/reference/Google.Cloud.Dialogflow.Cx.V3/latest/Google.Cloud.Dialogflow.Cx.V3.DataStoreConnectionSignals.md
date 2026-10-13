---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals
title: Dialogflow v3 API - Class DataStoreConnectionSignals (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:03.202675+00:00
---

# Dialogflow v3 API - Class DataStoreConnectionSignals (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class DataStoreConnectionSignals (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class DataStoreConnectionSignals : IMessage<DataStoreConnectionSignals>, IEquatable<DataStoreConnectionSignals>, IDeepCloneable<DataStoreConnectionSignals>, IBufferMessage, IMessage

Reference documentation and code samples for the Dialogflow v3 API class DataStoreConnectionSignals.

Data store connection feature output signals. Might be only partially field if processing stop before the final answer. Reasons for this can be, but are not limited to: empty UCS search results, positive RAI check outcome, grounding failure, ...

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataStoreConnectionSignals

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Constructors 

### DataStoreConnectionSignals()
    
    
    public DataStoreConnectionSignals()

### DataStoreConnectionSignals(DataStoreConnectionSignals)
    
    
    public DataStoreConnectionSignals(DataStoreConnectionSignals other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)`  
  
  
## Properties 

### Answer
    
    
    public string Answer { get; set; }

Optional. The final compiled answer.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AnswerGenerationModelCallSignals
    
    
    public DataStoreConnectionSignals.Types.AnswerGenerationModelCallSignals AnswerGenerationModelCallSignals { get; set; }

Optional. Diagnostic info related to the answer generation model call.

**Property Value**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types)[AnswerGenerationModelCallSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.AnswerGenerationModelCallSignals)` |   
  
### AnswerParts
    
    
    public RepeatedField<DataStoreConnectionSignals.Types.AnswerPart> AnswerParts { get; }

Optional. Answer parts with relevant citations. Concatenation of texts should add up the `answer` (not counting whitespaces).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types)[AnswerPart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.AnswerPart)` |   
  
### CitedSnippets
    
    
    public RepeatedField<DataStoreConnectionSignals.Types.CitedSnippet> CitedSnippets { get; }

Optional. Snippets cited by the answer generation model from the most to least relevant.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types)[CitedSnippet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.CitedSnippet)` |   
  
### GroundingSignals
    
    
    public DataStoreConnectionSignals.Types.GroundingSignals GroundingSignals { get; set; }

Optional. Grounding signals.

**Property Value**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types)[GroundingSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.GroundingSignals)` |   
  
### RewriterModelCallSignals
    
    
    public DataStoreConnectionSignals.Types.RewriterModelCallSignals RewriterModelCallSignals { get; set; }

Optional. Diagnostic info related to the rewriter model call.

**Property Value**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types)[RewriterModelCallSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.RewriterModelCallSignals)` |   
  
### RewrittenQuery
    
    
    public string RewrittenQuery { get; set; }

Optional. Rewritten string query used for search.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SafetySignals
    
    
    public DataStoreConnectionSignals.Types.SafetySignals SafetySignals { get; set; }

Optional. Safety check result.

**Property Value**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types)[SafetySignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.SafetySignals)` |   
  
### SearchSnippets
    
    
    public RepeatedField<DataStoreConnectionSignals.Types.SearchSnippet> SearchSnippets { get; }

Optional. Search snippets included in the answer generation prompt.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types)[SearchSnippet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.SearchSnippet)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
