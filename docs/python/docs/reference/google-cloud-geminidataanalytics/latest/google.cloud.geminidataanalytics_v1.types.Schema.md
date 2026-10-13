---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Schema
title: Class Schema (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:02.100605+00:00
---

# Class Schema (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Schema

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Schema (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    Schema(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The schema of a Datasource or QueryResult instance.

## Attributes  
  
---  
**Name** | **Description**  
`fields` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.Field](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Field)]`   
Optional. The fields in the schema.   
`description` |  `str`   
Optional. A textual description of the table's content and purpose. For example: "Contains information about customer orders in our e-commerce store." Currently only used for BigQuery data sources.   
`synonyms` |  `MutableSequence[str]`   
Optional. A list of alternative names or synonyms that can be used to refer to the table. For example: ["sales", "orders", "purchases"]. Currently only used for BigQuery data sources.   
`tags` |  `MutableSequence[str]`   
Optional. A list of tags or keywords associated with the table, used for categorization. For example: ["transaction", "revenue", "customer_data"]. Currently only used for BigQuery data sources.   
`display_name` |  `str`   
Optional. Table display_name (same as label in cloud/data_analytics/anarres/data/looker/proto/model_explore.proto), not required, currently only Looker has this field.   
`filters` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.DataFilter](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DataFilter)]`   
Optional. The filters on the datasource's underlying data. Currently only used for Looker data sources.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
