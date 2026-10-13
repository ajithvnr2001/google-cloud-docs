---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion
title: Google Cloud Dialogflow v2beta1 API - Class GeneratorSuggestion (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:19.312390+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class GeneratorSuggestion (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class GeneratorSuggestion (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class GeneratorSuggestion : IMessage<GeneratorSuggestion>, IEquatable<GeneratorSuggestion>, IDeepCloneable<GeneratorSuggestion>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class GeneratorSuggestion.

Suggestion generated using a Generator.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GeneratorSuggestion

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GeneratorSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GeneratorSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GeneratorSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### GeneratorSuggestion()
    
    
    public GeneratorSuggestion()

### GeneratorSuggestion(GeneratorSuggestion)
    
    
    public GeneratorSuggestion(GeneratorSuggestion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GeneratorSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion)`  
  
  
## Properties 

### AgentCoachingSuggestion
    
    
    public AgentCoachingSuggestion AgentCoachingSuggestion { get; set; }

Optional. Suggestion to coach the agent.

**Property Value**  
---  
**Type** | **Description**  
`[AgentCoachingSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AgentCoachingSuggestion)` |   
  
### FreeFormSuggestion
    
    
    public FreeFormSuggestion FreeFormSuggestion { get; set; }

Optional. Free form suggestion.

**Property Value**  
---  
**Type** | **Description**  
`[FreeFormSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.FreeFormSuggestion)` |   
  
### SuggestionCase
    
    
    public GeneratorSuggestion.SuggestionOneofCase SuggestionCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[GeneratorSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion)[SuggestionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion.SuggestionOneofCase)` |   
  
### SummarySuggestion
    
    
    public SummarySuggestion SummarySuggestion { get; set; }

Optional. Suggested summary.

**Property Value**  
---  
**Type** | **Description**  
`[SummarySuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SummarySuggestion)` |   
  
### ToolCallInfo
    
    
    public RepeatedField<GeneratorSuggestion.Types.ToolCallInfo> ToolCallInfo { get; }

Optional. List of request and response for tool calls executed.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[GeneratorSuggestion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion.Types)[ToolCallInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GeneratorSuggestion.Types.ToolCallInfo)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
