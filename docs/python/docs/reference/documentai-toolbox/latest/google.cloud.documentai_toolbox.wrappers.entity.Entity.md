---
url: https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.Entity
title: Class Entity (0.17.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:36.021854+00:00
---

# Class Entity (0.17.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.Entity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Entity (0.17.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.4 (latest)  0.17.3  0.16.0  0.15.2  0.14.2-a0  0.13.5-a0  0.12.2-a0  0.11.2-a0  0.10.3-a0  0.9.1-a0  0.8.0-a0  0.7.0-a0  0.6.0-a0  0.5.0-a0  0.4.1-a0  0.3.0-a0  0.2.1-a0  0.1.1-a0 
    
    
    Entity(
        documentai_object: google.cloud.documentai_v1.types.document.Document.Entity,
        page_offset: dataclasses.InitVar[typing.Optional[int]] = 0,
    )

Represents a wrapped `documentai.Document.Entity`.

## Attributes  
  
---  
**Name** | **Description**  
`documentai_object :noindex:` |  `google.cloud.documentai.Document.Entity`   
Required. The original `google.cloud.documentai.Document.Entity` object.   
`page_offset :noindex:` |  `InitVar[int]`   
Optional. The start page of the shard containing the `documentai.Document.Entity` in the context of the full `documentai.Document`. `page_refs.page` is relative to the shard, not the full `documentai.Document`.   
`type_ :noindex:` |  `str`   
Required. Entity type from a schema e.g. "Address".   
`mention_text :noindex:` |  `str`   
Optional. Text value in the document e.g. "1600 Amphitheatre Pkwy". Only populated for Extraction processors.   
`normalized_text :noindex:` |  `str`   
Optional. Normalized text value in the document e.g. "1970-01-01". Only populated for Extraction processors.   
`start_page :noindex:` |  `int`   
Optional. `Page` containing the `Entity` for Extraction processors or the first page of the subdocument for Splitter processors.   
`end_page :noindex:` |  `int`   
Optional. Last page of the subdocument for Splitter processors.   
  
## Methods 

### crop_image
    
    
    crop_image(
        documentai_page: google.cloud.documentai_v1.types.document.Document.Page,
    ) -> typing.Optional[PIL.Image.Image]

Return image cropped from page image for detected entity.

**Parameter**  
---  
**Name** | **Description**  
`documentai_page` |  `documentai.Document`   
Required. The `Document.Page` containing the `Entity`.  
**Returns**  
---  
**Type** | **Description**  
`PIL.Image.Image` | Image from `Document.Entity`. Returns `None` if there is no image.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
