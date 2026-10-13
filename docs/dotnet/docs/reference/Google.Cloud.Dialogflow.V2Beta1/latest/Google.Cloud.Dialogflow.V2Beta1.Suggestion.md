---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion
title: Google Cloud Dialogflow v2beta1 API - Class Suggestion (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:48.493548+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class Suggestion (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class Suggestion (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    [Obsolete]
    public sealed class Suggestion : IMessage<Suggestion>, IEquatable<Suggestion>, IDeepCloneable<Suggestion>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class Suggestion.

Represents a suggestion for a human agent.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Suggestion

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Suggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Suggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Suggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### Suggestion()
    
    
    public Suggestion()

### Suggestion(Suggestion)
    
    
    public Suggestion(Suggestion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Suggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion)`  
  
  
## Properties 

### Articles
    
    
    public RepeatedField<Suggestion.Types.Article> Articles { get; }

Output only. Articles ordered by score in descending order.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Suggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion.Types)[Article](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion.Types.Article)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time the suggestion was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### FaqAnswers
    
    
    public RepeatedField<Suggestion.Types.FaqAnswer> FaqAnswers { get; }

Output only. Answers extracted from FAQ documents.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Suggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion.Types)[FaqAnswer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Suggestion.Types.FaqAnswer)` |   
  
### LatestMessage
    
    
    public string LatestMessage { get; set; }

Output only. Latest message used as context to compile this suggestion.

Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The name of this suggestion. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/*/suggestions/<Suggestion ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
