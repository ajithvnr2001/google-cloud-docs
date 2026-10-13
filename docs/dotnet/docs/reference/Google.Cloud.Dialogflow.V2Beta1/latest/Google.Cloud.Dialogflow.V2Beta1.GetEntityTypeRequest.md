---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetEntityTypeRequest
title: Google Cloud Dialogflow v2beta1 API - Class GetEntityTypeRequest (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:56.391405+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class GetEntityTypeRequest (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetEntityTypeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class GetEntityTypeRequest (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class GetEntityTypeRequest : IMessage<GetEntityTypeRequest>, IEquatable<GetEntityTypeRequest>, IDeepCloneable<GetEntityTypeRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class GetEntityTypeRequest.

The request message for [EntityTypes.GetEntityType][google.cloud.dialogflow.v2beta1.EntityTypes.GetEntityType].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetEntityTypeRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetEntityTypeRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetEntityTypeRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetEntityTypeRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### GetEntityTypeRequest()
    
    
    public GetEntityTypeRequest()

### GetEntityTypeRequest(GetEntityTypeRequest)
    
    
    public GetEntityTypeRequest(GetEntityTypeRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetEntityTypeRequest)`  
  
  
## Properties 

### EntityTypeName
    
    
    public EntityTypeName EntityTypeName { get; set; }

[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.EntityTypeName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetEntityTypeRequest#Google_Cloud_Dialogflow_V2Beta1_GetEntityTypeRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.EntityTypeName)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the entity type. Supported formats:

  * `projects/<Project ID>/agent/entityTypes/<Entity Type ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/entityTypes/<Entity Type ID>`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
