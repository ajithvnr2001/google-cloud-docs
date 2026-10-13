---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfigOrBuilder
title: Interface TranslateSpeechConfigOrBuilder (0.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:08.927496+00:00
---

# Interface TranslateSpeechConfigOrBuilder (0.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TranslateSpeechConfigOrBuilder (0.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.105.0 (latest)  0.101.0  0.100.0  0.99.0  0.97.0  0.94.0  0.93.0  0.91.0  0.89.0  0.88.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.70.0  0.69.0  0.68.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.6  0.7.10 
    
    
    public interface TranslateSpeechConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAudioEncoding()
    
    
    public abstract String getAudioEncoding()

Required. Encoding of audio data. Supported formats:

  * `linear16`

Uncompressed 16-bit signed little-endian samples (Linear PCM).

  * `flac`

`flac` (Free Lossless Audio Codec) is the recommended encoding because it is lossless--therefore recognition is not compromised--and requires only about half the bandwidth of `linear16`.

  * `mulaw`

8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.

  * `amr`

Adaptive Multi-Rate Narrowband codec. `sample_rate_hertz` must be 8000.

  * `amr-wb`

Adaptive Multi-Rate Wideband codec. `sample_rate_hertz` must be 16000.

  * `ogg-opus`

Opus encoded audio frames in [Ogg](https://wikipedia.org/wiki/Ogg) container. `sample_rate_hertz` must be one of 8000, 12000, 16000, 24000, or 48000.

  * `mp3`

MP3 audio. Support all standard MP3 bitrates (which range from 32-320 kbps). When using this encoding, `sample_rate_hertz` has to match the sample rate of the file being used.




`string audio_encoding = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The audioEncoding.  
  
### getAudioEncodingBytes()
    
    
    public abstract ByteString getAudioEncodingBytes()

Required. Encoding of audio data. Supported formats:

  * `linear16`

Uncompressed 16-bit signed little-endian samples (Linear PCM).

  * `flac`

`flac` (Free Lossless Audio Codec) is the recommended encoding because it is lossless--therefore recognition is not compromised--and requires only about half the bandwidth of `linear16`.

  * `mulaw`

8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.

  * `amr`

Adaptive Multi-Rate Narrowband codec. `sample_rate_hertz` must be 8000.

  * `amr-wb`

Adaptive Multi-Rate Wideband codec. `sample_rate_hertz` must be 16000.

  * `ogg-opus`

Opus encoded audio frames in [Ogg](https://wikipedia.org/wiki/Ogg) container. `sample_rate_hertz` must be one of 8000, 12000, 16000, 24000, or 48000.

  * `mp3`

MP3 audio. Support all standard MP3 bitrates (which range from 32-320 kbps). When using this encoding, `sample_rate_hertz` has to match the sample rate of the file being used.




`string audio_encoding = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for audioEncoding.  
  
### getModel()
    
    
    public abstract String getModel()

Optional. `google-provided-model/video` and `google-provided-model/enhanced-phone-call` are premium models. `google-provided-model/phone-call` is not premium model.

`string model = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The model.  
  
### getModelBytes()
    
    
    public abstract ByteString getModelBytes()

Optional. `google-provided-model/video` and `google-provided-model/enhanced-phone-call` are premium models. `google-provided-model/phone-call` is not premium model.

`string model = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for model.  
  
### getSampleRateHertz()
    
    
    public abstract int getSampleRateHertz()

Optional. Sample rate in Hertz of the audio data. Valid values are: 8000-48000. 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that's not possible, use the native sample rate of the audio source (instead of re-sampling).

`int32 sample_rate_hertz = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sampleRateHertz.  
  
### getSourceLanguageCode()
    
    
    public abstract String getSourceLanguageCode()

Required. Source language code (BCP-47) of the input audio.

`string source_language_code = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceLanguageCode.  
  
### getSourceLanguageCodeBytes()
    
    
    public abstract ByteString getSourceLanguageCodeBytes()

Required. Source language code (BCP-47) of the input audio.

`string source_language_code = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceLanguageCode.  
  
### getTargetLanguageCode()
    
    
    public abstract String getTargetLanguageCode()

Required. Target language code (BCP-47) of the output.

`string target_language_code = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetLanguageCode.  
  
### getTargetLanguageCodeBytes()
    
    
    public abstract ByteString getTargetLanguageCodeBytes()

Required. Target language code (BCP-47) of the output.

`string target_language_code = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetLanguageCode.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
