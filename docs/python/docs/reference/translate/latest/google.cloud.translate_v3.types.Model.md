---
url: https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.Model
title: Class Model (3.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:55.309035+00:00
---

# Class Model (3.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.Model

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Model (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.1  3.20.3  3.19.0  3.18.0  3.17.0  3.15.5  3.14.0  3.13.0  3.12.1  3.11.3  3.10.1  3.9.0  3.8.4  3.7.4  3.6.1  3.5.0  3.4.1  3.3.2  3.2.1  3.1.0  3.0.2  2.0.4  1.7.2  1.6.0 
    
    
    Model(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A trained translation model.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The resource name of the model, in form of `projects/{project-number-or-id}/locations/{location_id}/models/{model_id}`  
`display_name` |  `str`   
The name of the model to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (\\_), and ASCII digits 0-9.   
`dataset` |  `str`   
The dataset from which the model is trained, in form of `projects/{project-number-or-id}/locations/{location_id}/datasets/{dataset_id}`  
`source_language_code` |  `str`   
Output only. The BCP-47 language code of the source language.   
`target_language_code` |  `str`   
Output only. The BCP-47 language code of the target language.   
`train_example_count` |  `int`   
Output only. Number of examples (sentence pairs) used to train the model.   
`validate_example_count` |  `int`   
Output only. Number of examples (sentence pairs) used to validate the model.   
`test_example_count` |  `int`   
Output only. Number of examples (sentence pairs) used to test the model.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when the model resource was created, which is also when the training started.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this model was last updated.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
