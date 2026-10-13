---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.types.Field
title: Class Field (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:52.208120+00:00
---

# Class Field (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.types.Field

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Field (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    Field(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A field in a schema.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Optional. The name of the field.   
`type_` |  `str`   
Optional. The type of the field.   
`description` |  `str`   
Optional. A brief description of the field.   
`mode` |  `str`   
Optional. The mode of the field (e.g., NULLABLE, REPEATED).   
`synonyms` |  `MutableSequence[str]`   
Optional. A list of alternative names or synonyms that can be used to refer to this field. For example: ["id", "customerid", "cust_id"]. Currently only used for BigQuery data sources.   
`tags` |  `MutableSequence[str]`   
Optional. A list of tags or keywords associated with the field, used for categorization. For example: ["identifier", "customer", "pii"]. Currently only used for BigQuery data sources.   
`display_name` |  `str`   
Optional. Field display_name (same as label in   
`subfields` |  `MutableSequence[google.cloud.geminidataanalytics_v1beta.types.Field]`   
Optional. Recursive property for nested schema structures.   
`category` |  `str`   
Optional. Field category, not required, currently only useful for Looker.   
`value_format` |  `str`   
Optional. Looker only. Value format of the field. Ref: https://cloud.google.com/looker/docs/reference/param-field-value-format   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
