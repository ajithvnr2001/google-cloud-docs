---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference
title: Google Cloud Dialogflow v2beta1 API - Class Conversation.Types.ContextReference (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:21.238735+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class Conversation.Types.ContextReference (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class Conversation.Types.ContextReference (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class Conversation.Types.ContextReference : IMessage<Conversation.Types.ContextReference>, IEquatable<Conversation.Types.ContextReference>, IDeepCloneable<Conversation.Types.ContextReference>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class Conversation.Types.ContextReference.

Represents a piece of ingested context information.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Conversation.Types.ContextReference

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### ContextReference()
    
    
    public ContextReference()

### ContextReference(ContextReference)
    
    
    public ContextReference(Conversation.Types.ContextReference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)`  
  
  
## Properties 

### ContextContents
    
    
    public RepeatedField<Conversation.Types.ContextReference.Types.ContextContent> ContextContents { get; }

Required. The list of content updates for a context reference.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference.Types)[ContextContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference.Types.ContextContent)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time the context reference was first created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

Optional. The language of the information ingested, defaults to "en-US" if not set.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateMode
    
    
    public Conversation.Types.ContextReference.Types.UpdateMode UpdateMode { get; set; }

Required. The mode in which context reference contents are updated.

**Property Value**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference.Types)[UpdateMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference.Types.UpdateMode)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
