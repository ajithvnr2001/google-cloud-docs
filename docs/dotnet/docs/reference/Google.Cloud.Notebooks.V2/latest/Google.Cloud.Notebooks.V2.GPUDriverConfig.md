---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.GPUDriverConfig
title: Vertex AI Notebooks v2 API - Class GPUDriverConfig (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:04.032888+00:00
---

# Vertex AI Notebooks v2 API - Class GPUDriverConfig (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.GPUDriverConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI Notebooks v2 API - Class GPUDriverConfig (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.GPUDriverConfig)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/1.2.0/Google.Cloud.Notebooks.V2.GPUDriverConfig)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/1.1.0/Google.Cloud.Notebooks.V2.GPUDriverConfig)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/1.0.0/Google.Cloud.Notebooks.V2.GPUDriverConfig)


    
    
    public sealed class GPUDriverConfig : IMessage<GPUDriverConfig>, IEquatable<GPUDriverConfig>, IDeepCloneable<GPUDriverConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI Notebooks v2 API class GPUDriverConfig.

A GPU driver configuration

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GPUDriverConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GPUDriverConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.GPUDriverConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GPUDriverConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.GPUDriverConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GPUDriverConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.GPUDriverConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Notebooks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2)

## Assembly

Google.Cloud.Notebooks.V2.dll

## Constructors 

### GPUDriverConfig()
    
    
    public GPUDriverConfig()

### GPUDriverConfig(GPUDriverConfig)
    
    
    public GPUDriverConfig(GPUDriverConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GPUDriverConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.GPUDriverConfig)`  
  
  
## Properties 

### CustomGpuDriverPath
    
    
    public string CustomGpuDriverPath { get; set; }

Optional. Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnableGpuDriver
    
    
    public bool EnableGpuDriver { get; set; }

Optional. Whether the end user authorizes Google Cloud to install GPU driver on this VM instance. If this field is empty or set to false, the GPU driver won't be installed. Only applicable to instances with GPUs.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
