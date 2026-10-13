---
url: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.StreamingRecognitionConfig
title: Class StreamingRecognitionConfig (2.41.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:37.988056+00:00
---

# Class StreamingRecognitionConfig (2.41.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.StreamingRecognitionConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamingRecognitionConfig (2.41.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.41.0 (latest)  2.40.0  2.39.0  2.38.0  2.37.0  2.36.1  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.1  2.25.1  2.24.1  2.23.0  2.22.0  2.21.1  2.20.1  2.19.0  2.18.0  2.17.3  2.16.2  2.15.1  2.14.1  2.13.1  2.12.0  2.11.1  2.10.0  2.9.3  2.8.0  2.7.0  2.6.0  2.5.1  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.4  1.2.0  1.1.0 
    
    
    StreamingRecognitionConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Provides configuration information for the StreamingRecognize request.

## Attributes  
  
---  
**Name** | **Description**  
`config` |  `[google.cloud.speech_v2.types.RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.RecognitionConfig)`   
Required. Features and audio metadata to use for the Automatic Speech Recognition. This field in combination with the config_mask field can be used to override parts of the default_recognition_config of the Recognizer resource.   
`config_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields in config that override the values in the default_recognition_config of the recognizer during this recognition request. If no mask is provided, all non-default valued fields in config override the values in the Recognizer for this recognition request. If a mask is provided, only the fields listed in the mask override the config in the Recognizer for this recognition request. If a wildcard (`*`) is provided, config completely overrides and replaces the config in the recognizer for this recognition request.   
`streaming_features` |  `[google.cloud.speech_v2.types.StreamingRecognitionFeatures](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v2.types.StreamingRecognitionFeatures)`   
Speech recognition features to enable specific to streaming audio recognition requests.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
