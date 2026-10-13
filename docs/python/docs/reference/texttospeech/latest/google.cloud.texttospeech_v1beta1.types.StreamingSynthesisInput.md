---
url: https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.StreamingSynthesisInput
title: Class StreamingSynthesisInput (2.38.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:44.770431+00:00
---

# Class StreamingSynthesisInput (2.38.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.StreamingSynthesisInput

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamingSynthesisInput (2.38.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.38.0 (latest)  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.0  2.19.0  2.18.0  2.17.2  2.16.5  2.15.1  2.14.2  2.13.0  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.5.0 
    
    
    StreamingSynthesisInput(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Input to be synthesized.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`text` |  `str`   
The raw text to be synthesized. It is recommended that each input contains complete, terminating sentences, which results in better prosody in the output audio. This field is a member of `oneof`_ `input_source`.   
`markup` |  `str`   
Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices. This field is a member of `oneof`_ `input_source`.   
`multi_speaker_markup` |  `[google.cloud.texttospeech_v1beta1.types.MultiSpeakerMarkup](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.MultiSpeakerMarkup)`   
Multi-speaker markup for Gemini TTS. This field may not be used with any other voices. This field is a member of `oneof`_ `input_source`.   
`prompt` |  `str`   
This is system instruction supported only for controllable voice models. This field is a member of `oneof`_ `_prompt`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
