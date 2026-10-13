---
url: https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeConfig
title: Class StreamingSynthesizeConfig (2.38.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:05.974092+00:00
---

# Class StreamingSynthesizeConfig (2.38.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamingSynthesizeConfig (2.38.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.38.0 (latest)  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.0  2.19.0  2.18.0  2.17.2  2.16.5  2.15.1  2.14.2  2.13.0  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.5.0 
    
    
    StreamingSynthesizeConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Provides configuration information for the StreamingSynthesize request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`voice` |  `[google.cloud.texttospeech_v1.types.VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceSelectionParams)`   
Required. The desired voice of the synthesized audio.   
`streaming_audio_config` |  `[google.cloud.texttospeech_v1.types.StreamingAudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingAudioConfig)`   
Optional. The configuration of the synthesized audio.   
`custom_pronunciations` |  `[google.cloud.texttospeech_v1.types.CustomPronunciations](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.CustomPronunciations)`   
Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations. The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported. In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag.   
`advanced_voice_options` |  `[google.cloud.texttospeech_v1.types.AdvancedVoiceOptions](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AdvancedVoiceOptions)`   
Optional. Advanced voice options. This field is a member of `oneof`_ `_advanced_voice_options`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
