---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.AgentContextReference
title: Data Analytics API with Gemini v1beta API - Class AgentContextReference (1.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:49.241997+00:00
---

# Data Analytics API with Gemini v1beta API - Class AgentContextReference (1.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.AgentContextReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1beta API - Class AgentContextReference (1.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta12 (latest)  1.0.0-beta11 
    
    
    public sealed class AgentContextReference : IMessage<AgentContextReference>, IEquatable<AgentContextReference>, IDeepCloneable<AgentContextReference>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1beta API class AgentContextReference.

Message representing a reference to Agent Context.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AgentContextReference

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AgentContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.AgentContextReference), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AgentContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.AgentContextReference), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AgentContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.AgentContextReference), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1Beta.dll

## Constructors 

### AgentContextReference()
    
    
    public AgentContextReference()

### AgentContextReference(AgentContextReference)
    
    
    public AgentContextReference(AgentContextReference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AgentContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.AgentContextReference)`  
  
  
## Properties 

### ContextSetId
    
    
    public string ContextSetId { get; set; }

Required. Context set ID to retrieve.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
