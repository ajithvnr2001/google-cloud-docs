---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionFeaturesOrBuilder
title: Interface RecognitionFeaturesOrBuilder (4.94.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:00.007198+00:00
---

# Interface RecognitionFeaturesOrBuilder (4.94.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionFeaturesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RecognitionFeaturesOrBuilder (4.94.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.94.0 (latest)  4.90.0  4.89.0  4.88.0  4.86.0  4.83.0  4.82.0  4.80.0  4.78.0  4.77.0  4.75.0  4.73.0  4.71.0  4.70.0  4.69.0  4.68.0  4.67.0  4.65.0  4.63.0  4.62.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.44.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.0.0  2.6.1  2.5.9  2.4.0  2.3.0  2.2.15 
    
    
    public interface RecognitionFeaturesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCustomPromptConfig()
    
    
    public abstract CustomPromptConfig getCustomPromptConfig()

Optional. Configuration to enable custom prompt for chirp3.

` .google.cloud.speech.v2.CustomPromptConfig custom_prompt_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomPromptConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomPromptConfig)` | The customPromptConfig.  
  
### getCustomPromptConfigOrBuilder()
    
    
    public abstract CustomPromptConfigOrBuilder getCustomPromptConfigOrBuilder()

Optional. Configuration to enable custom prompt for chirp3.

` .google.cloud.speech.v2.CustomPromptConfig custom_prompt_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomPromptConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomPromptConfigOrBuilder)` |   
  
### getDiarizationConfig()
    
    
    public abstract SpeakerDiarizationConfig getDiarizationConfig()

Configuration to enable speaker diarization. To enable diarization, set this field to an empty SpeakerDiarizationConfig message.

`.google.cloud.speech.v2.SpeakerDiarizationConfig diarization_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[SpeakerDiarizationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeakerDiarizationConfig)` | The diarizationConfig.  
  
### getDiarizationConfigOrBuilder()
    
    
    public abstract SpeakerDiarizationConfigOrBuilder getDiarizationConfigOrBuilder()

Configuration to enable speaker diarization. To enable diarization, set this field to an empty SpeakerDiarizationConfig message.

`.google.cloud.speech.v2.SpeakerDiarizationConfig diarization_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[SpeakerDiarizationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeakerDiarizationConfigOrBuilder)` |   
  
### getEnableAutomaticPunctuation()
    
    
    public abstract boolean getEnableAutomaticPunctuation()

If `true`, adds punctuation to recognition result hypotheses. This feature is only available in select languages. The default `false` value does not add punctuation to result hypotheses.

`bool enable_automatic_punctuation = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableAutomaticPunctuation.  
  
### getEnableSpokenEmojis()
    
    
    public abstract boolean getEnableSpokenEmojis()

The spoken emoji behavior for the call. If `true`, adds spoken emoji formatting for the request. This will replace spoken emojis with the corresponding Unicode symbols in the final transcript. If `false`, spoken emojis are not replaced.

`bool enable_spoken_emojis = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableSpokenEmojis.  
  
### getEnableSpokenPunctuation()
    
    
    public abstract boolean getEnableSpokenPunctuation()

The spoken punctuation behavior for the call. If `true`, replaces spoken punctuation with the corresponding symbols in the request. For example, "how are you question mark" becomes "how are you?". See <https://cloud.google.com/speech-to-text/docs/spoken-punctuation> for support. If `false`, spoken punctuation is not replaced.

`bool enable_spoken_punctuation = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableSpokenPunctuation.  
  
### getEnableWordConfidence()
    
    
    public abstract boolean getEnableWordConfidence()

If `true`, the top result includes a list of words and the confidence for those words. If `false`, no word-level confidence information is returned. The default is `false`.

`bool enable_word_confidence = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableWordConfidence.  
  
### getEnableWordTimeOffsets()
    
    
    public abstract boolean getEnableWordTimeOffsets()

If `true`, the top result includes a list of words and the start and end time offsets (timestamps) for those words. If `false`, no word-level time offset information is returned. The default is `false`.

`bool enable_word_time_offsets = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableWordTimeOffsets.  
  
### getMaxAlternatives()
    
    
    public abstract int getMaxAlternatives()

Maximum number of recognition hypotheses to be returned. The server may return fewer than `max_alternatives`. Valid values are `0`-`30`. A value of `0` or `1` will return a maximum of one. If omitted, will return a maximum of one.

`int32 max_alternatives = 16;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxAlternatives.  
  
### getMultiChannelMode()
    
    
    public abstract RecognitionFeatures.MultiChannelMode getMultiChannelMode()

Mode for recognizing multi-channel audio.

`.google.cloud.speech.v2.RecognitionFeatures.MultiChannelMode multi_channel_mode = 17; `

**Returns**  
---  
**Type** | **Description**  
`[RecognitionFeatures.MultiChannelMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionFeatures.MultiChannelMode)` | The multiChannelMode.  
  
### getMultiChannelModeValue()
    
    
    public abstract int getMultiChannelModeValue()

Mode for recognizing multi-channel audio.

`.google.cloud.speech.v2.RecognitionFeatures.MultiChannelMode multi_channel_mode = 17; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for multiChannelMode.  
  
### getProfanityFilter()
    
    
    public abstract boolean getProfanityFilter()

If set to `true`, the server will attempt to filter out profanities, replacing all but the initial character in each filtered word with asterisks, for instance, "f***". If set to `false` or omitted, profanities won't be filtered out.

`bool profanity_filter = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The profanityFilter.  
  
### hasCustomPromptConfig()
    
    
    public abstract boolean hasCustomPromptConfig()

Optional. Configuration to enable custom prompt for chirp3.

` .google.cloud.speech.v2.CustomPromptConfig custom_prompt_config = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customPromptConfig field is set.  
  
### hasDiarizationConfig()
    
    
    public abstract boolean hasDiarizationConfig()

Configuration to enable speaker diarization. To enable diarization, set this field to an empty SpeakerDiarizationConfig message.

`.google.cloud.speech.v2.SpeakerDiarizationConfig diarization_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diarizationConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
