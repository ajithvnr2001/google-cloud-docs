---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship
title: Class SchemaRelationship (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:50.351324+00:00
---

# Class SchemaRelationship (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SchemaRelationship (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    SchemaRelationship(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The relationship between two tables, including referencing and referenced columns. This is a derived context retrieved from Dataplex Dataset Insights.

## Attributes  
  
---  
**Name** | **Description**  
`left_schema_paths` |  `[google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship.SchemaPaths](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship.SchemaPaths)`   
An ordered list of fields for the join from the first table. The size of this list must be the same as `right_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `right_schema_paths` list.   
`right_schema_paths` |  `[google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship.SchemaPaths](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship.SchemaPaths)`   
An ordered list of fields for the join from the second table. The size of this list must be the same as `left_schema_paths`. Each field at index i in this list must correspond to a field at the same index in the `left_schema_paths` list.   
`sources` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship.Source](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship.Source)]`   
Optional. Sources which generated the schema relation edge.   
`confidence_score` |  `float`   
Optional. A confidence score for the suggested relationship. Manually added edges have the highest confidence score.   
  
## Classes 

### SchemaPaths
    
    
    SchemaPaths(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents an ordered set of paths within the table schema.

### Source
    
    
    Source(value)

Source which generated the schema relation edge.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
