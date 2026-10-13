---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1
title: Package com.google.cloud.mediatranslation.v1beta1 (0.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:05.128224+00:00
---

# Package com.google.cloud.mediatranslation.v1beta1 (0.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.mediatranslation.v1beta1 (0.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.105.0 (latest)  0.101.0  0.100.0  0.99.0  0.97.0  0.94.0  0.93.0  0.91.0  0.89.0  0.88.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.70.0  0.69.0  0.68.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.6  0.7.10 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-mediatranslation/google-cloud-mediatranslation/src/main/java/com/google/cloud/mediatranslation/v1beta1)  
---  
  
## Prerelease Implications

This package is a prerelease version! Use with caution.

Prerelease versions are considered unstable as they may be shut down and/or subject to breaking changes when upgrading. Use them only for testing or if you specifically need their experimental features.

## Client Classes

Client classes are the main entry point to using a package. They contain several variations of Java methods for each of the API's methods. 

Client |  Description  
---|---  
[com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceClient](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceClient) |  Service Description: Provides translation from/to media types. This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceSettings](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceSettings) |  Settings class to configure an instance of SpeechTranslationServiceClient. The default instance has everything set to sensible defaults:   
  
## Classes

Class |  Description  
---|---  
[com.google.cloud.mediatranslation.v1beta1.MediaTranslationProto](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.MediaTranslationProto) |   
[com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceGrpc](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceGrpc) |  Provides translation from/to media types.   
[com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceGrpc.SpeechTranslationServiceImplBase](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceGrpc.SpeechTranslationServiceImplBase) |  Base class for the server implementation of the service SpeechTranslationService. Provides translation from/to media types.  
[com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceSettings.Builder) |  Builder for SpeechTranslationServiceSettings.  
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechConfig](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechConfig) |  Config used for streaming translation.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechConfig.Builder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechConfig.Builder) |  Config used for streaming translation.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequest](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequest) |  The top-level message sent by the client for the `StreamingTranslateSpeech` method. Multiple `StreamingTranslateSpeechRequest` messages are sent. The first message must contain a `streaming_config` message and must not contain  
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequest.Builder) |  The top-level message sent by the client for the `StreamingTranslateSpeech` method. Multiple `StreamingTranslateSpeechRequest` messages are sent. The first message must contain a `streaming_config` message and must not contain  
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse) |  A streaming speech translation response corresponding to a portion of the audio currently processed.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse.Builder) |  A streaming speech translation response corresponding to a portion of the audio currently processed.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult) |  A streaming speech translation result corresponding to a portion of the audio that is currently being processed.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.Builder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.Builder) |  A streaming speech translation result corresponding to a portion of the audio that is currently being processed.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.TextTranslationResult](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.TextTranslationResult) |  Text translation result.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.TextTranslationResult.Builder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.TextTranslationResult.Builder) |  Text translation result.   
[com.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfig](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfig) |  Provides information to the speech translation that specifies how to process the request.   
[com.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfig.Builder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfig.Builder) |  Provides information to the speech translation that specifies how to process the request.   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceGrpc.AsyncService](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.SpeechTranslationServiceGrpc.AsyncService) |  Provides translation from/to media types.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechConfigOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechConfigOrBuilder) |   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequestOrBuilder) |   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponseOrBuilder) |   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.TextTranslationResultOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.TextTranslationResultOrBuilder) |   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResultOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResultOrBuilder) |   
[com.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfigOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfigOrBuilder) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequest.StreamingRequestCase](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequest.StreamingRequestCase) |   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse.SpeechEventType](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse.SpeechEventType) |  Indicates the type of speech event.   
[com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.ResultCase](https://cloud.google.com/java/docs/reference/google-cloud-mediatranslation/latest/com.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.ResultCase) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
