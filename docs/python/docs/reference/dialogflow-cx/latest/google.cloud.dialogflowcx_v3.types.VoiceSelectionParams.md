---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.VoiceSelectionParams
title: Class VoiceSelectionParams (2.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:56.170966+00:00
---

# Class VoiceSelectionParams (2.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.VoiceSelectionParams

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class VoiceSelectionParams (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.1.0  2.0.0  1.43.0  1.42.0  1.41.1  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.1  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.5  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.2  1.2.0  1.1.1  1.0.0  0.8.2  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    VoiceSelectionParams(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Description of which voice to use for speech synthesis.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as language_code and ssml_gender. For the list of available voices, please refer to `Supported voices and languages   
`ssml_gender` |  `[google.cloud.dialogflowcx_v3.types.SsmlVoiceGender](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SsmlVoiceGender)`   
Optional. The preferred gender of the voice. If not set, the service will choose a voice based on the other parameters such as language_code and name. Note that this is only a preference, not requirement. If a voice of the appropriate gender is not available, the synthesizer substitutes a voice with a different gender rather than failing the request.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
