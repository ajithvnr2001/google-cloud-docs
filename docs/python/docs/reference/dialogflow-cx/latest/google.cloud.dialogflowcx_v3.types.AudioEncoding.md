---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AudioEncoding
title: Class AudioEncoding (2.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:03.384565+00:00
---

# Class AudioEncoding (2.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AudioEncoding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AudioEncoding (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.1.0  2.0.0  1.43.0  1.42.0  1.41.1  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.1  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.5  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.2  1.2.0  1.1.1  1.0.0  0.8.2  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    AudioEncoding(value)

Audio encoding of the audio content sent in the conversational query request. Refer to the `Cloud Speech API documentation <https://cloud.google.com/speech-to-text/docs/basics>`__ for more details.

## Enums  
  
---  
**Name** | **Description**  
`AUDIO_ENCODING_UNSPECIFIED` | Not specified.  
`AUDIO_ENCODING_LINEAR_16` | Uncompressed 16-bit signed little-endian samples (Linear PCM). LINT: LEGACY_NAMES  
`AUDIO_ENCODING_FLAC` | ```FLAC``   
`AUDIO_ENCODING_MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`AUDIO_ENCODING_AMR` | Adaptive Multi-Rate Narrowband codec. `sample_rate_hertz` must be 8000.  
`AUDIO_ENCODING_AMR_WB` | Adaptive Multi-Rate Wideband codec. `sample_rate_hertz` must be 16000.  
`AUDIO_ENCODING_OGG_OPUS` | Opus encoded audio frames in Ogg container (`OggOpus   
`AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE` | Although the use of lossy encodings is not recommended, if a very low bitrate encoding is required, `OGG_OPUS` is highly preferred over Speex encoding. The `Speex   
`AUDIO_ENCODING_ALAW` | 8-bit samples that compand 13-bit audio samples using G.711 PCMU/a-law.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
