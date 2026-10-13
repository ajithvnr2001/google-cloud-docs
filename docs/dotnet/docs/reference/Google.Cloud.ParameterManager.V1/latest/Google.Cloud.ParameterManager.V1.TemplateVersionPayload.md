---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.TemplateVersionPayload
title: Parameter Manager v1 API - Class TemplateVersionPayload (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:03.216501+00:00
---

# Parameter Manager v1 API - Class TemplateVersionPayload (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.TemplateVersionPayload

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Parameter Manager v1 API - Class TemplateVersionPayload (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class TemplateVersionPayload : IMessage<TemplateVersionPayload>, IEquatable<TemplateVersionPayload>, IDeepCloneable<TemplateVersionPayload>, IBufferMessage, IMessage

Reference documentation and code samples for the Parameter Manager v1 API class TemplateVersionPayload.

Message for storing a TemplateVersion resource's payload data

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TemplateVersionPayload

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TemplateVersionPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.TemplateVersionPayload), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TemplateVersionPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.TemplateVersionPayload), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TemplateVersionPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.TemplateVersionPayload), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1)

## Assembly

Google.Cloud.ParameterManager.V1.dll

## Constructors 

### TemplateVersionPayload()
    
    
    public TemplateVersionPayload()

### TemplateVersionPayload(TemplateVersionPayload)
    
    
    public TemplateVersionPayload(TemplateVersionPayload other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TemplateVersionPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.TemplateVersionPayload)`  
  
  
## Properties 

### Data
    
    
    public ByteString Data { get; set; }

Required. bytes data for storing payload.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
