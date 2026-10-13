---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorType
title: Cloud TPU v1 API - Class AcceleratorType (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:14.569884+00:00
---

# Cloud TPU v1 API - Class AcceleratorType (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud TPU v1 API - Class AcceleratorType (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorType)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/2.4.0/Google.Cloud.Tpu.V1.AcceleratorType)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/2.3.0/Google.Cloud.Tpu.V1.AcceleratorType)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/2.2.0/Google.Cloud.Tpu.V1.AcceleratorType)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/2.1.0/Google.Cloud.Tpu.V1.AcceleratorType)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/2.0.0/Google.Cloud.Tpu.V1.AcceleratorType)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/1.1.0/Google.Cloud.Tpu.V1.AcceleratorType)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/1.0.0/Google.Cloud.Tpu.V1.AcceleratorType)


    
    
    public sealed class AcceleratorType : IMessage<AcceleratorType>, IEquatable<AcceleratorType>, IDeepCloneable<AcceleratorType>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud TPU v1 API class AcceleratorType.

A accelerator type that a Node can be configured with.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AcceleratorType

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorType), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorType), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorType), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tpu.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1)

## Assembly

Google.Cloud.Tpu.V1.dll

## Constructors 

### AcceleratorType()
    
    
    public AcceleratorType()

### AcceleratorType(AcceleratorType)
    
    
    public AcceleratorType(AcceleratorType other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorType)`  
  
  
## Properties 

### AcceleratorTypeName
    
    
    public AcceleratorTypeName AcceleratorTypeName { get; set; }

[AcceleratorTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorTypeName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorType#Google_Cloud_Tpu_V1_AcceleratorType_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AcceleratorTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tpu.V1/latest/Google.Cloud.Tpu.V1.AcceleratorTypeName)` |   
  
### Name
    
    
    public string Name { get; set; }

The resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public string Type { get; set; }

the accelerator type.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
