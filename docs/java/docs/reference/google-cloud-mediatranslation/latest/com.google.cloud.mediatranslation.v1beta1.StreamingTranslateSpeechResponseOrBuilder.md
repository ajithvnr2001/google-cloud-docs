---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponseOrBuilder
title: Interface StreamingTranslateSpeechResponseOrBuilder (0.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:08.453179+00:00
---

# Interface StreamingTranslateSpeechResponseOrBuilder (0.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StreamingTranslateSpeechResponseOrBuilder (0.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.105.0 (latest)  0.101.0  0.100.0  0.99.0  0.97.0  0.94.0  0.93.0  0.91.0  0.89.0  0.88.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.70.0  0.69.0  0.68.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.6  0.7.10 
    
    
    public interface StreamingTranslateSpeechResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getError()
    
    
    public abstract Status getError()

Output only. If set, returns a google.rpc.Status message that specifies the error for the operation.

`.google.rpc.Status error = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

Output only. If set, returns a google.rpc.Status message that specifies the error for the operation.

`.google.rpc.Status error = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getResult()
    
    
    public abstract StreamingTranslateSpeechResult getResult()

Output only. The translation result that is currently being processed (is_final could be true or false).

` .google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamingTranslateSpeechResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult)` | The result.  
  
### getResultOrBuilder()
    
    
    public abstract StreamingTranslateSpeechResultOrBuilder getResultOrBuilder()

Output only. The translation result that is currently being processed (is_final could be true or false).

` .google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamingTranslateSpeechResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResultOrBuilder)` |   
  
### getSpeechEventType()
    
    
    public abstract StreamingTranslateSpeechResponse.SpeechEventType getSpeechEventType()

Output only. Indicates the type of speech event.

` .google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse.SpeechEventType speech_event_type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[StreamingTranslateSpeechResponse.SpeechEventType](https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse.SpeechEventType)` | The speechEventType.  
  
### getSpeechEventTypeValue()
    
    
    public abstract int getSpeechEventTypeValue()

Output only. Indicates the type of speech event.

` .google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse.SpeechEventType speech_event_type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for speechEventType.  
  
### hasError()
    
    
    public abstract boolean hasError()

Output only. If set, returns a google.rpc.Status message that specifies the error for the operation.

`.google.rpc.Status error = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasResult()
    
    
    public abstract boolean hasResult()

Output only. The translation result that is currently being processed (is_final could be true or false).

` .google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the result field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
