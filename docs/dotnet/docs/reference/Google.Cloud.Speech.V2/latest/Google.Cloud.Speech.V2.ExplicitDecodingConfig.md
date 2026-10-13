---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig
title: Cloud Speech-to-Text v2 API - Class ExplicitDecodingConfig (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:04.978729+00:00
---

# Cloud Speech-to-Text v2 API - Class ExplicitDecodingConfig (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Speech-to-Text v2 API - Class ExplicitDecodingConfig (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.7.0/Google.Cloud.Speech.V2.ExplicitDecodingConfig)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.6.0/Google.Cloud.Speech.V2.ExplicitDecodingConfig)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.5.0/Google.Cloud.Speech.V2.ExplicitDecodingConfig)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.4.0/Google.Cloud.Speech.V2.ExplicitDecodingConfig)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.3.0/Google.Cloud.Speech.V2.ExplicitDecodingConfig)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.2.0/Google.Cloud.Speech.V2.ExplicitDecodingConfig)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.1.0/Google.Cloud.Speech.V2.ExplicitDecodingConfig)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.0.0/Google.Cloud.Speech.V2.ExplicitDecodingConfig)


    
    
    public sealed class ExplicitDecodingConfig : IMessage<ExplicitDecodingConfig>, IEquatable<ExplicitDecodingConfig>, IDeepCloneable<ExplicitDecodingConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Speech-to-Text v2 API class ExplicitDecodingConfig.

Explicitly specified decoding parameters.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExplicitDecodingConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ExplicitDecodingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExplicitDecodingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ExplicitDecodingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2)

## Assembly

Google.Cloud.Speech.V2.dll

## Constructors 

### ExplicitDecodingConfig()
    
    
    public ExplicitDecodingConfig()

### ExplicitDecodingConfig(ExplicitDecodingConfig)
    
    
    public ExplicitDecodingConfig(ExplicitDecodingConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ExplicitDecodingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig)`  
  
  
## Properties 

### AudioChannelCount
    
    
    public int AudioChannelCount { get; set; }

Optional. Number of channels present in the audio data sent for recognition. Note that this field is marked as OPTIONAL for backward compatibility reasons. It is (and has always been) effectively REQUIRED.

The maximum allowed value is 8.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Encoding
    
    
    public ExplicitDecodingConfig.Types.AudioEncoding Encoding { get; set; }

Required. Encoding of the audio data sent for recognition.

**Property Value**  
---  
**Type** | **Description**  
`[ExplicitDecodingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig.Types)[AudioEncoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.ExplicitDecodingConfig.Types.AudioEncoding)` |   
  
### SampleRateHertz
    
    
    public int SampleRateHertz { get; set; }

Optional. Sample rate in Hertz of the audio data sent for recognition. Valid values are: 8000-48000, and 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that's not possible, use the native sample rate of the audio source (instead of resampling). Note that this field is marked as OPTIONAL for backward compatibility reasons. It is (and has always been) effectively REQUIRED.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
