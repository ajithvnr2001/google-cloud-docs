---
url: https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.CreateTagTemplateRequest
title: Class CreateTagTemplateRequest (3.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:48.480649+00:00
---

# Class CreateTagTemplateRequest (3.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.CreateTagTemplateRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateTagTemplateRequest (3.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.32.0 (latest)  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.1  3.25.1  3.24.1  3.23.0  3.22.0  3.21.1  3.20.1  3.19.1  3.18.3  3.17.2  3.16.0  3.15.1  3.14.0  3.13.1  3.12.0  3.11.1  3.10.0  3.9.3  3.8.1  3.7.1  3.6.2  3.5.0  3.4.3  3.3.2  3.2.1  3.1.1  3.0.0  2.0.2  1.0.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    CreateTagTemplateRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for CreateTagTemplate.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The name of the project and the template location `region `__.   
`tag_template_id` |  `str`   
Required. The ID of the tag template to create. The ID must contain only lowercase letters (a-z), numbers (0-9), or underscores (\\_), and must start with a letter or underscore. The maximum size is 64 bytes when encoded in UTF-8.   
`tag_template` |  `[google.cloud.datacatalog_v1.types.TagTemplate](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.TagTemplate)`   
Required. The tag template to create.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
