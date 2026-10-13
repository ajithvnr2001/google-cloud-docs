---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig
title: Class ParsingConfig (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:36.669925+00:00
---

# Class ParsingConfig (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ParsingConfig (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    ParsingConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Related configurations applied to a specific type of document parser.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`digital_parsing_config` |  `[google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.DigitalParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.DigitalParsingConfig)`   
Configurations applied to digital parser. This field is a member of `oneof`_ `type_dedicated_config`.   
`ocr_parsing_config` |  `[google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.OcrParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.OcrParsingConfig)`   
Configurations applied to OCR parser. Currently it only applies to PDFs. This field is a member of `oneof`_ `type_dedicated_config`.   
`layout_parsing_config` |  `[google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.LayoutParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.LayoutParsingConfig)`   
Configurations applied to layout parser. This field is a member of `oneof`_ `type_dedicated_config`.   
  
## Classes 

### DigitalParsingConfig
    
    
    DigitalParsingConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The digital parsing configurations for documents.

### LayoutParsingConfig
    
    
    LayoutParsingConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The layout parsing configurations for documents.

### OcrParsingConfig
    
    
    OcrParsingConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The OCR parsing configurations for documents.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
