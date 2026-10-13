---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ColumnSpec
title: Class ColumnSpec (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:45.057319+00:00
---

# Class ColumnSpec (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ColumnSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ColumnSpec (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    ColumnSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A representation of a column in a relational table. When listing them, column specs are returned in the same order in which they were given on import . Used by:

  * Tables



## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The resource name of the column specs. Form: `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/tableSpecs/{table_spec_id}/columnSpecs/{column_spec_id}`  
`data_type` |  `[google.cloud.automl_v1beta1.types.DataType](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DataType)`   
The data type of elements stored in the column.   
`display_name` |  `str`   
Output only. The name of the column to show in the interface. The name can be up to 100 characters long and can consist only of ASCII Latin letters A-Z and a-z, ASCII digits 0-9, underscores(\\_), and forward slashes(/), and must start with a letter or a digit.   
`data_stats` |  `[google.cloud.automl_v1beta1.types.DataStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DataStats)`   
Output only. Stats of the series of values in the column. This field may be stale, see the ancestor's Dataset.tables_dataset_metadata.stats_update_time field for the timestamp at which these stats were last updated.   
`top_correlated_columns` |  `MutableSequence[[google.cloud.automl_v1beta1.types.ColumnSpec.CorrelatedColumn](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ColumnSpec.CorrelatedColumn)]`   
Deprecated.   
`etag` |  `str`   
Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.   
  
## Classes 

### CorrelatedColumn
    
    
    CorrelatedColumn(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Identifies the table's column, and its correlation with the column this ColumnSpec describes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
