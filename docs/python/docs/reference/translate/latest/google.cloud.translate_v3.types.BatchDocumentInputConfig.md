---
url: https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.BatchDocumentInputConfig
title: Class BatchDocumentInputConfig (3.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:54.273387+00:00
---

# Class BatchDocumentInputConfig (3.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.BatchDocumentInputConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BatchDocumentInputConfig (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.1  3.20.3  3.19.0  3.18.0  3.17.0  3.15.5  3.14.0  3.13.0  3.12.1  3.11.3  3.10.1  3.9.0  3.8.4  3.7.4  3.6.1  3.5.0  3.4.1  3.3.2  3.2.1  3.1.0  3.0.2  2.0.4  1.7.2  1.6.0 
    
    
    BatchDocumentInputConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Input configuration for BatchTranslateDocument request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attribute  
  
---  
**Name** | **Description**  
`gcs_source` |  `[google.cloud.translate_v3.types.GcsSource](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.GcsSource)`   
Google Cloud Storage location for the source input. This can be a single file (for example, `gs://translation-test/input.docx`) or a wildcard (for example, `gs://translation-test/*`). File mime type is determined based on extension. Supported mime type includes: \- `pdf`, application/pdf \- `docx`, application/vnd.openxmlformats-officedocument.wordprocessingml.document \- `pptx`, application/vnd.openxmlformats-officedocument.presentationml.presentation \- `xlsx`, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet The max file size to support for `.docx`, `.pptx` and `.xlsx` is 100MB. The max file size to support for `.pdf` is 1GB and the max page limit is 1000 pages. The max file size to support for all input documents is 1GB. This field is a member of `oneof`_ `source`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
