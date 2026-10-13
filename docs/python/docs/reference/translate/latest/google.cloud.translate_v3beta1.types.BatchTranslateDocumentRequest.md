---
url: https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.BatchTranslateDocumentRequest
title: Class BatchTranslateDocumentRequest (3.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:39.316712+00:00
---

# Class BatchTranslateDocumentRequest (3.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.BatchTranslateDocumentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BatchTranslateDocumentRequest (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.1  3.20.3  3.19.0  3.18.0  3.17.0  3.15.5  3.14.0  3.13.0  3.12.1  3.11.3  3.10.1  3.9.0  3.8.4  3.7.4  3.6.1  3.5.0  3.4.1  3.3.2  3.2.1  3.1.0  3.0.2  2.0.4  1.7.2  1.6.0 
    
    
    BatchTranslateDocumentRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The BatchTranslateDocument request.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Location to make a regional call. Format: `projects/{project-number-or-id}/locations/{location-id}`. The `global` location is not supported for batch translation. Only AutoML Translation models or glossaries within the same region (have the same location-id) can be used, otherwise an INVALID_ARGUMENT (400) error is returned.   
`source_language_code` |  `str`   
Required. The BCP-47 language code of the input document if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in `Language Support   
`target_language_codes` |  `MutableSequence[str]`   
Required. The BCP-47 language code to use for translation of the input document. Specify up to 10 language codes here. Supported language codes are listed in `Language Support   
`input_configs` |  `MutableSequence[[google.cloud.translate_v3beta1.types.BatchDocumentInputConfig](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.BatchDocumentInputConfig)]`   
Required. Input configurations. The total number of files matched should be <= 100.="" the="" total="" content="" size="" to="" translate="" should="" be=""><= 100m="" unicode="" codepoints.="" the="" files="" must="" use="" utf-8="" encoding.="">  
`output_config` |  `[google.cloud.translate_v3beta1.types.BatchDocumentOutputConfig](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.BatchDocumentOutputConfig)`   
Required. Output configuration. If 2 input configs match to the same file (that is, same input path), we don't generate output for duplicate inputs.   
`models` |  `MutableMapping[str, str]`   
Optional. The models to use for translation. Map's key is target language code. Map's value is the model name. Value can be a built-in general model, or an AutoML Translation model. The value format depends on model type: \- AutoML Translation models: `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}` \- General (built-in) models: `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`, If the map is empty or a specific model is not requested for a language pair, then default google model (nmt) is used.   
`glossaries` |  `MutableMapping[str, [google.cloud.translate_v3beta1.types.TranslateTextGlossaryConfig](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.TranslateTextGlossaryConfig)]`   
Optional. Glossaries to be applied. It's keyed by target language code.   
`format_conversions` |  `MutableMapping[str, str]`   
Optional. File format conversion map to be applied to all input files. Map's key is the original mime_type. Map's value is the target mime_type of translated documents. Supported file format conversion includes: \- `application/pdf` to `application/vnd.openxmlformats-officedocument.wordprocessingml.document` If nothing specified, output files will be in the same format as the original file.   
`customized_attribution` |  `str`   
Optional. This flag is to support user customized attribution. If not provided, the default is `Machine Translated by Google`. Customized attribution should follow rules in https://cloud.google.com/translate/attribution#attribution_and_logos   
`enable_shadow_removal_native_pdf` |  `bool`   
Optional. If true, use the text removal server to remove the shadow text on background image for native pdf translation. Shadow removal feature can only be enabled when is_translate_native_pdf_only: false && pdf_native_only: false   
`enable_rotation_correction` |  `bool`   
Optional. If true, enable auto rotation correction in DVS.   
`pdf_native_only` |  `bool`   
Optional. If true, only native pdf pages will be translated.   
  
## Classes 

### FormatConversionsEntry
    
    
    FormatConversionsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### GlossariesEntry
    
    
    GlossariesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### ModelsEntry
    
    
    ModelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
