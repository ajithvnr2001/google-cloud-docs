---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template.TemplateMetadata
title: Class TemplateMetadata (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:04.330798+00:00
---

# Class TemplateMetadata (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template.TemplateMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TemplateMetadata (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
    TemplateMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing TemplateMetadata

## Attributes  
  
---  
**Name** | **Description**  
`ignore_partial_invocation_failures` |  `bool`   
Optional. If true, partial detector failures should be ignored.   
`custom_prompt_safety_error_code` |  `int`   
Optional. Indicates the custom error code set by the user to be returned to the end user by the service extension if the prompt trips Model Armor filters.   
`custom_prompt_safety_error_message` |  `str`   
Optional. Indicates the custom error message set by the user to be returned to the end user if the prompt trips Model Armor filters.   
`custom_llm_response_safety_error_code` |  `int`   
Optional. Indicates the custom error code set by the user to be returned to the end user if the LLM response trips Model Armor filters.   
`custom_llm_response_safety_error_message` |  `str`   
Optional. Indicates the custom error message set by the user to be returned to the end user if the LLM response trips Model Armor filters.   
`log_template_operations` |  `bool`   
Optional. If true, log template crud operations.   
`log_sanitize_operations` |  `bool`   
Optional. If true, log sanitize operations.   
`enforcement_type` |  `[google.cloud.modelarmor_v1.types.Template.TemplateMetadata.EnforcementType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template.TemplateMetadata.EnforcementType)`   
Optional. Enforcement type for Model Armor filters.   
`multi_language_detection` |  `[google.cloud.modelarmor_v1.types.Template.TemplateMetadata.MultiLanguageDetection](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template.TemplateMetadata.MultiLanguageDetection)`   
Optional. Metadata for multi language detection.   
`modalities` |  `MutableSequence[[google.cloud.modelarmor_v1.types.Modality](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Modality)]`   
Optional. Specifies the modalities to scan. If empty, only text modality will be scanned.   
  
## Classes 

### EnforcementType
    
    
    EnforcementType(value)

Enforcement type for Model Armor filters.

### MultiLanguageDetection
    
    
    MultiLanguageDetection(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata to enable multi language detection via template.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
