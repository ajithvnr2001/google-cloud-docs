---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetTemplateRequest
title: Model Armor v1 API - Class GetTemplateRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:20.984457+00:00
---

# Model Armor v1 API - Class GetTemplateRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetTemplateRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1 API - Class GetTemplateRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta07 
    
    
    public sealed class GetTemplateRequest : IMessage<GetTemplateRequest>, IEquatable<GetTemplateRequest>, IDeepCloneable<GetTemplateRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1 API class GetTemplateRequest.

Message for getting a Template

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetTemplateRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetTemplateRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetTemplateRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetTemplateRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1)

## Assembly

Google.Cloud.ModelArmor.V1.dll

## Constructors 

### GetTemplateRequest()
    
    
    public GetTemplateRequest()

### GetTemplateRequest(GetTemplateRequest)
    
    
    public GetTemplateRequest(GetTemplateRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetTemplateRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Name of the resource

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TemplateName
    
    
    public TemplateName TemplateName { get; set; }

[TemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.TemplateName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetTemplateRequest#Google_Cloud_ModelArmor_V1_GetTemplateRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.TemplateName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
