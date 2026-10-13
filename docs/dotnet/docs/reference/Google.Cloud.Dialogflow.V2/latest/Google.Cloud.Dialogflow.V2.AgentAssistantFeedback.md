---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback
title: Google Cloud Dialogflow v2 API - Class AgentAssistantFeedback (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:54.091421+00:00
---

# Google Cloud Dialogflow v2 API - Class AgentAssistantFeedback (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class AgentAssistantFeedback (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class AgentAssistantFeedback : IMessage<AgentAssistantFeedback>, IEquatable<AgentAssistantFeedback>, IDeepCloneable<AgentAssistantFeedback>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class AgentAssistantFeedback.

Detail feedback of Agent Assist result.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AgentAssistantFeedback

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### AgentAssistantFeedback()
    
    
    public AgentAssistantFeedback()

### AgentAssistantFeedback(AgentAssistantFeedback)
    
    
    public AgentAssistantFeedback(AgentAssistantFeedback other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback)`  
  
  
## Properties 

### AnswerRelevance
    
    
    public AgentAssistantFeedback.Types.AnswerRelevance AnswerRelevance { get; set; }

Optional. Whether or not the suggested answer is relevant.

For example:

  * Query: "Can I change my mailing address?"
  * Suggested document says: "Items must be returned/exchanged within 60 days of the purchase date."
  * [answer_relevance][google.cloud.dialogflow.v2.AgentAssistantFeedback.answer_relevance]: [AnswerRelevance.IRRELEVANT][google.cloud.dialogflow.v2.AgentAssistantFeedback.AnswerRelevance.IRRELEVANT]



**Property Value**  
---  
**Type** | **Description**  
`[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types)[AnswerRelevance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types.AnswerRelevance)` |   
  
### CompanionFeedback
    
    
    public AgentAssistantFeedback.Types.CompanionFeedback CompanionFeedback { get; set; }

Optional. Feedback for companion agent.

**Property Value**  
---  
**Type** | **Description**  
`[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types)[CompanionFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types.CompanionFeedback)` |   
  
### DocumentCorrectness
    
    
    public AgentAssistantFeedback.Types.DocumentCorrectness DocumentCorrectness { get; set; }

Optional. Whether or not the information in the document is correct.

For example:

  * Query: "Can I return the package in 2 days once received?"
  * Suggested document says: "Items must be returned/exchanged within 60 days of the purchase date."
  * Ground truth: "No return or exchange is allowed."
  * [document_correctness][google.cloud.dialogflow.v2.AgentAssistantFeedback.document_correctness]: [INCORRECT][google.cloud.dialogflow.v2.AgentAssistantFeedback.DocumentCorrectness.INCORRECT]



**Property Value**  
---  
**Type** | **Description**  
`[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types)[DocumentCorrectness](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types.DocumentCorrectness)` |   
  
### DocumentEfficiency
    
    
    public AgentAssistantFeedback.Types.DocumentEfficiency DocumentEfficiency { get; set; }

Optional. Whether or not the suggested document is efficient. For example, if the document is poorly written, hard to understand, hard to use or too long to find useful information, [document_efficiency][google.cloud.dialogflow.v2.AgentAssistantFeedback.document_efficiency] is [DocumentEfficiency.INEFFICIENT][google.cloud.dialogflow.v2.AgentAssistantFeedback.DocumentEfficiency.INEFFICIENT].

**Property Value**  
---  
**Type** | **Description**  
`[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types)[DocumentEfficiency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types.DocumentEfficiency)` |   
  
### KnowledgeAssistFeedback
    
    
    public AgentAssistantFeedback.Types.KnowledgeAssistFeedback KnowledgeAssistFeedback { get; set; }

Optional. Feedback for knowledge assist.

**Property Value**  
---  
**Type** | **Description**  
`[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types)[KnowledgeAssistFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types.KnowledgeAssistFeedback)` |   
  
### KnowledgeSearchFeedback
    
    
    public AgentAssistantFeedback.Types.KnowledgeSearchFeedback KnowledgeSearchFeedback { get; set; }

Optional. Feedback for knowledge search.

**Property Value**  
---  
**Type** | **Description**  
`[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types)[KnowledgeSearchFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types.KnowledgeSearchFeedback)` |   
  
### SummarizationFeedback
    
    
    public AgentAssistantFeedback.Types.SummarizationFeedback SummarizationFeedback { get; set; }

Optional. Feedback for conversation summarization.

**Property Value**  
---  
**Type** | **Description**  
`[AgentAssistantFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types)[SummarizationFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantFeedback.Types.SummarizationFeedback)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
