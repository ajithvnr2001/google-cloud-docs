---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream
title: Live Stream v1 API - Class TextStream (1.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:55.615028+00:00
---

# Live Stream v1 API - Class TextStream (1.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Live Stream v1 API - Class TextStream (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.11.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.10.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.9.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.8.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.7.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.6.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.5.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.4.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.3.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.2.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.1.0/Google.Cloud.Video.LiveStream.V1.TextStream)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/1.0.0/Google.Cloud.Video.LiveStream.V1.TextStream)


    
    
    public sealed class TextStream : IMessage<TextStream>, IEquatable<TextStream>, IDeepCloneable<TextStream>, IBufferMessage, IMessage

Reference documentation and code samples for the Live Stream v1 API class TextStream.

Encoding of a text stream. For example, closed captions or subtitles.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TextStream

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TextStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TextStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TextStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1)

## Assembly

Google.Cloud.Video.LiveStream.V1.dll

## Constructors 

### TextStream()
    
    
    public TextStream()

### TextStream(TextStream)
    
    
    public TextStream(TextStream other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TextStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream)`  
  
  
## Properties 

### Codec
    
    
    public string Codec { get; set; }

Required. The codec for this text stream.

Supported text codecs:

  * `cea608`
  * `cea708`
  * `webvtt`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. The name for this particular text stream that will be added to the HLS/DASH manifest.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

Optional. The BCP-47 language code, such as `en-US` or `sr-Latn`. For more information, see <https://www.unicode.org/reports/tr35/#Unicode_locale_identifier>.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Mapping
    
    
    public RepeatedField<TextStream.Types.TextMapping> Mapping { get; }

Optional. The mapping for the input streams and text tracks.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[TextStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream.Types)[TextMapping](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.TextStream.Types.TextMapping)` |   
  
### OutputCeaChannel
    
    
    public string OutputCeaChannel { get; set; }

Optional. The channel of the closed caption in the output stream. This field should only be set when textstream is used for partner distribution. Must be one of `CC1`, `CC2`, `CC3`, and `CC4`, if the [codec][google.cloud.video.livestream.v1.TextStream.codec] is `cea608`; Must be one between `SERVICE1` and `SERVICE63`, if the [codec][google.cloud.video.livestream.v1.TextStream.codec] is `cea708`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
