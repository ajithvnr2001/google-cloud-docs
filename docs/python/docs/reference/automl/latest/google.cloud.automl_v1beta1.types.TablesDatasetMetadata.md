---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TablesDatasetMetadata
title: Class TablesDatasetMetadata (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:01.187821+00:00
---

# Class TablesDatasetMetadata (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TablesDatasetMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TablesDatasetMetadata (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    TablesDatasetMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata for a dataset used for AutoML Tables.

## Attributes  
  
---  
**Name** | **Description**  
`primary_table_spec_id` |  `str`   
Output only. The table_spec_id of the primary table of this dataset.   
`target_column_spec_id` |  `str`   
column_spec_id of the primary table's column that should be used as the training & prediction target. This column must be non-nullable and have one of following data types (otherwise model creation will error): \- CATEGORY \- FLOAT64 If the type is CATEGORY , only up to 100 unique values may exist in that column across all rows. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset.   
`weight_column_spec_id` |  `str`   
column_spec_id of the primary table's column that should be used as the weight column, i.e. the higher the value the more important the row will be during model training. Required type: FLOAT64. Allowed values: 0 to 10000, inclusive on both ends; 0 means the row is ignored for training. If not set all rows are assumed to have equal weight of 1. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset.   
`ml_use_column_spec_id` |  `str`   
column_spec_id of the primary table column which specifies a possible ML use of the row, i.e. the column will be used to split the rows into TRAIN, VALIDATE and TEST sets. Required type: STRING. This column, if set, must either have all of `TRAIN`, `VALIDATE`, `TEST` among its values, or only have `TEST`, `UNASSIGNED` values. In the latter case the rows with `UNASSIGNED` value will be assigned by AutoML. Note that if a given ml use distribution makes it impossible to create a "good" model, that call will error describing the issue. If both this column_spec_id and primary table's time_column_spec_id are not set, then all rows are treated as `UNASSIGNED`. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset.   
`target_column_correlations` |  `MutableMapping[str, [google.cloud.automl_v1beta1.types.CorrelationStats](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CorrelationStats)]`   
Output only. Correlations between TablesDatasetMetadata.target_column_spec_id, and other columns of the TablesDatasetMetadataprimary_table. Only set if the target column is set. Mapping from other column spec id to its CorrelationStats with the target column. This field may be stale, see the stats_update_time field for for the timestamp at which these stats were last updated.   
`stats_update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The most recent timestamp when target_column_correlations field and all descendant ColumnSpec.data_stats and ColumnSpec.top_correlated_columns fields were last (re-)generated. Any changes that happened to the dataset afterwards are not reflected in these fields values. The regeneration happens in the background on a best effort basis.   
  
## Classes 

### TargetColumnCorrelationsEntry
    
    
    TargetColumnCorrelationsEntry(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

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

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
