---
url: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.UpdatePhraseSetRequest
title: Class UpdatePhraseSetRequest (2.41.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:47.196633+00:00
---

# Class UpdatePhraseSetRequest (2.41.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.UpdatePhraseSetRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdatePhraseSetRequest (2.41.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.41.0 (latest)  2.40.0  2.39.0  2.38.0  2.37.0  2.36.1  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.1  2.25.1  2.24.1  2.23.0  2.22.0  2.21.1  2.20.1  2.19.0  2.18.0  2.17.3  2.16.2  2.15.1  2.14.1  2.13.1  2.12.0  2.11.1  2.10.0  2.9.3  2.8.0  2.7.0  2.6.0  2.5.1  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.4  1.2.0  1.1.0 
    
    
    UpdatePhraseSetRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message sent by the client for the `UpdatePhraseSet` method.

## Attributes  
  
---  
**Name** | **Description**  
`phrase_set` |  `[google.cloud.speech_v1.types.PhraseSet](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.PhraseSet)`   
Required. The phrase set to update. The phrase set's `name` field is used to identify the set to be updated. Format: `projects/{project}/locations/{location}/phraseSets/{phrase_set}` Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a `regional endpoint   
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to be updated.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
