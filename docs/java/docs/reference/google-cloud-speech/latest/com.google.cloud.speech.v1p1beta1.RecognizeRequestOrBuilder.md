---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1p1beta1.RecognizeRequestOrBuilder
title: Interface RecognizeRequestOrBuilder (4.94.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:58.883494+00:00
---

# Interface RecognizeRequestOrBuilder (4.94.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1p1beta1.RecognizeRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RecognizeRequestOrBuilder (4.94.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.94.0 (latest)  4.90.0  4.89.0  4.88.0  4.86.0  4.83.0  4.82.0  4.80.0  4.78.0  4.77.0  4.75.0  4.73.0  4.71.0  4.70.0  4.69.0  4.68.0  4.67.0  4.65.0  4.63.0  4.62.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.44.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.0.0  2.6.1  2.5.9  2.4.0  2.3.0  2.2.15 
    
    
    public interface RecognizeRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAudio()
    
    
    public abstract RecognitionAudio getAudio()

Required. The audio data to be recognized.

` .google.cloud.speech.v1p1beta1.RecognitionAudio audio = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1p1beta1.RecognitionAudio)` | The audio.  
  
### getAudioOrBuilder()
    
    
    public abstract RecognitionAudioOrBuilder getAudioOrBuilder()

Required. The audio data to be recognized.

` .google.cloud.speech.v1p1beta1.RecognitionAudio audio = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[RecognitionAudioOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1p1beta1.RecognitionAudioOrBuilder)` |   
  
### getConfig()
    
    
    public abstract RecognitionConfig getConfig()

Required. Provides information to the recognizer that specifies how to process the request.

` .google.cloud.speech.v1p1beta1.RecognitionConfig config = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1p1beta1.RecognitionConfig)` | The config.  
  
### getConfigOrBuilder()
    
    
    public abstract RecognitionConfigOrBuilder getConfigOrBuilder()

Required. Provides information to the recognizer that specifies how to process the request.

` .google.cloud.speech.v1p1beta1.RecognitionConfig config = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[RecognitionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1p1beta1.RecognitionConfigOrBuilder)` |   
  
### hasAudio()
    
    
    public abstract boolean hasAudio()

Required. The audio data to be recognized.

` .google.cloud.speech.v1p1beta1.RecognitionAudio audio = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the audio field is set.  
  
### hasConfig()
    
    
    public abstract boolean hasConfig()

Required. Provides information to the recognizer that specifies how to process the request.

` .google.cloud.speech.v1p1beta1.RecognitionConfig config = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the config field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
