---
url: https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DocumentSchema
title: Class DocumentSchema (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:26.609414+00:00
---

# Class DocumentSchema (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DocumentSchema

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DocumentSchema (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.1  2.35.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.3  2.28.0  2.27.1  2.26.0  2.25.0  2.24.2  2.23.0  2.22.0  2.21.1  2.20.2  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.3  1.5.1  1.4.2  1.3.0  1.2.1  1.1.0  1.0.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DocumentSchema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The schema defines the output of the processed document by a processor.

## Attributes  
  
---  
**Name** | **Description**  
`display_name` |  `str`   
Display name to show users.   
`description` |  `str`   
Description of the schema.   
`entity_types` |  `MutableSequence[[google.cloud.documentai_v1beta3.types.DocumentSchema.EntityType](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DocumentSchema.EntityType)]`   
Entity types of the schema.   
`metadata` |  `[google.cloud.documentai_v1beta3.types.DocumentSchema.Metadata](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DocumentSchema.Metadata)`   
Metadata of the schema.   
`document_prompt` |  `str`   
Optional. Document level prompt provided by the user. This custom text is injected into the AI model's prompt to provide extra, document-wide guidance for processing.   
  
## Classes 

### EntityType
    
    
    EntityType(mapping=None, *, ignore_unknown_fields=False, **kwargs)

EntityType is the wrapper of a label of the corresponding model with detailed attributes and limitations for entity-based processors. Multiple types can also compose a dependency tree to represent nested types.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### Metadata
    
    
    Metadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata for global schema behavior.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
