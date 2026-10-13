---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.DetectedAttribute
title: Google Cloud Video Intelligence v1 API - Class DetectedAttribute (3.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:57.254146+00:00
---

# Google Cloud Video Intelligence v1 API - Class DetectedAttribute (3.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.DetectedAttribute

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Video Intelligence v1 API - Class DetectedAttribute (3.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.4.0/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.3.0/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.2.0/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.1.0/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.0.0/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/2.3.0/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/2.2.0/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)


    
    
    public sealed class DetectedAttribute : IMessage<DetectedAttribute>, IEquatable<DetectedAttribute>, IDeepCloneable<DetectedAttribute>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Video Intelligence v1 API class DetectedAttribute.

A generic detected attribute represented by name in string format.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DetectedAttribute

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DetectedAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.DetectedAttribute), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DetectedAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.DetectedAttribute), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DetectedAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.DetectedAttribute), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VideoIntelligence.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1)

## Assembly

Google.Cloud.VideoIntelligence.V1.dll

## Constructors 

### DetectedAttribute()
    
    
    public DetectedAttribute()

### DetectedAttribute(DetectedAttribute)
    
    
    public DetectedAttribute(DetectedAttribute other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DetectedAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.DetectedAttribute)`  
  
  
## Properties 

### Confidence
    
    
    public float Confidence { get; set; }

Detected attribute confidence. Range [0, 1].

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### Name
    
    
    public string Name { get; set; }

The name of the attribute, for example, glasses, dark_glasses, mouth_open. A full list of supported type names will be provided in the document.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Value
    
    
    public string Value { get; set; }

Text value of the detection result. For example, the value for "HairColor" can be "black", "blonde", etc.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
