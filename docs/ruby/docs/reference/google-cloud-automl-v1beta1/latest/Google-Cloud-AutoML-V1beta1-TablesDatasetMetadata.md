---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-TablesDatasetMetadata/
title: Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata (v0.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:34.658176+00:00
---

# Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata (v0.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-TablesDatasetMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata (v0.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.1  0.13.1  0.12.0  0.11.1  0.10.2  0.9.0  0.8.0  0.7.0  0.6.1  0.5.5 

Reference documentation and code samples for the Cloud AutoML V1beta1 API class Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata.

Metadata for a dataset used for AutoML Tables.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ml_use_column_spec_id
    
    
    def ml_use_column_spec_id() -> ::String

**Returns**

  * (::String) — column_spec_id of the primary table column which specifies a possible ML use of the row, i.e. the column will be used to split the rows into TRAIN, VALIDATE and TEST sets. Required type: STRING. This column, if set, must either have all of `TRAIN`, `VALIDATE`, `TEST` among its values, or only have `TEST`, `UNASSIGNED` values. In the latter case the rows with `UNASSIGNED` value will be assigned by AutoML. Note that if a given ml use distribution makes it impossible to create a "good" model, that call will error describing the issue. If both this column_spec_id and primary table's time_column_spec_id are not set, then all rows are treated as `UNASSIGNED`. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 



### #ml_use_column_spec_id=
    
    
    def ml_use_column_spec_id=(value) -> ::String

**Parameter**

  * **value** (::String) — column_spec_id of the primary table column which specifies a possible ML use of the row, i.e. the column will be used to split the rows into TRAIN, VALIDATE and TEST sets. Required type: STRING. This column, if set, must either have all of `TRAIN`, `VALIDATE`, `TEST` among its values, or only have `TEST`, `UNASSIGNED` values. In the latter case the rows with `UNASSIGNED` value will be assigned by AutoML. Note that if a given ml use distribution makes it impossible to create a "good" model, that call will error describing the issue. If both this column_spec_id and primary table's time_column_spec_id are not set, then all rows are treated as `UNASSIGNED`. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 



**Returns**

  * (::String) — column_spec_id of the primary table column which specifies a possible ML use of the row, i.e. the column will be used to split the rows into TRAIN, VALIDATE and TEST sets. Required type: STRING. This column, if set, must either have all of `TRAIN`, `VALIDATE`, `TEST` among its values, or only have `TEST`, `UNASSIGNED` values. In the latter case the rows with `UNASSIGNED` value will be assigned by AutoML. Note that if a given ml use distribution makes it impossible to create a "good" model, that call will error describing the issue. If both this column_spec_id and primary table's time_column_spec_id are not set, then all rows are treated as `UNASSIGNED`. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 



### #primary_table_spec_id
    
    
    def primary_table_spec_id() -> ::String

**Returns**

  * (::String) — Output only. The table_spec_id of the primary table of this dataset. 



### #primary_table_spec_id=
    
    
    def primary_table_spec_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. The table_spec_id of the primary table of this dataset. 



**Returns**

  * (::String) — Output only. The table_spec_id of the primary table of this dataset. 



### #stats_update_time
    
    
    def stats_update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. The most recent timestamp when target_column_correlations field and all descendant ColumnSpec.data_stats and ColumnSpec.top_correlated_columns fields were last (re-)generated. Any changes that happened to the dataset afterwards are not reflected in these fields values. The regeneration happens in the background on a best effort basis. 



### #stats_update_time=
    
    
    def stats_update_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. The most recent timestamp when target_column_correlations field and all descendant ColumnSpec.data_stats and ColumnSpec.top_correlated_columns fields were last (re-)generated. Any changes that happened to the dataset afterwards are not reflected in these fields values. The regeneration happens in the background on a best effort basis. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. The most recent timestamp when target_column_correlations field and all descendant ColumnSpec.data_stats and ColumnSpec.top_correlated_columns fields were last (re-)generated. Any changes that happened to the dataset afterwards are not reflected in these fields values. The regeneration happens in the background on a best effort basis. 



### #target_column_correlations
    
    
    def target_column_correlations() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::AutoML::V1beta1::CorrelationStats}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::AutoML::V1beta1::CorrelationStats}) — Output only. Correlations between

[TablesDatasetMetadata.target_column_spec_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-TablesDatasetMetadata#Google__Cloud__AutoML__V1beta1__TablesDatasetMetadata_target_column_spec_id_instance_ "Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata#target_column_spec_id \(method\)"), and other columns of the

[TablesDatasetMetadataprimary_table](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-TablesDatasetMetadata#Google__Cloud__AutoML__V1beta1__TablesDatasetMetadata_primary_table_spec_id_instance_ "Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata#primary_table_spec_id \(method\)"). Only set if the target column is set. Mapping from other column spec id to its CorrelationStats with the target column. This field may be stale, see the stats_update_time field for for the timestamp at which these stats were last updated. 




### #target_column_correlations=
    
    
    def target_column_correlations=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::AutoML::V1beta1::CorrelationStats}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::AutoML::V1beta1::CorrelationStats}) — Output only. Correlations between

[TablesDatasetMetadata.target_column_spec_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-TablesDatasetMetadata#Google__Cloud__AutoML__V1beta1__TablesDatasetMetadata_target_column_spec_id_instance_ "Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata#target_column_spec_id \(method\)"), and other columns of the

[TablesDatasetMetadataprimary_table](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-TablesDatasetMetadata#Google__Cloud__AutoML__V1beta1__TablesDatasetMetadata_primary_table_spec_id_instance_ "Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata#primary_table_spec_id \(method\)"). Only set if the target column is set. Mapping from other column spec id to its CorrelationStats with the target column. This field may be stale, see the stats_update_time field for for the timestamp at which these stats were last updated. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::AutoML::V1beta1::CorrelationStats}) — Output only. Correlations between

[TablesDatasetMetadata.target_column_spec_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-TablesDatasetMetadata#Google__Cloud__AutoML__V1beta1__TablesDatasetMetadata_target_column_spec_id_instance_ "Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata#target_column_spec_id \(method\)"), and other columns of the

[TablesDatasetMetadataprimary_table](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-TablesDatasetMetadata#Google__Cloud__AutoML__V1beta1__TablesDatasetMetadata_primary_table_spec_id_instance_ "Google::Cloud::AutoML::V1beta1::TablesDatasetMetadata#primary_table_spec_id \(method\)"). Only set if the target column is set. Mapping from other column spec id to its CorrelationStats with the target column. This field may be stale, see the stats_update_time field for for the timestamp at which these stats were last updated. 




### #target_column_spec_id
    
    
    def target_column_spec_id() -> ::String

**Returns**

  * (::String) — column_spec_id of the primary table's column that should be used as the training & prediction target. This column must be non-nullable and have one of following data types (otherwise model creation will error):

    * CATEGORY

    * FLOAT64

If the type is CATEGORY , only up to 100 unique values may exist in that column across all rows.

NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 




### #target_column_spec_id=
    
    
    def target_column_spec_id=(value) -> ::String

**Parameter**

  * **value** (::String) — column_spec_id of the primary table's column that should be used as the training & prediction target. This column must be non-nullable and have one of following data types (otherwise model creation will error):

    * CATEGORY

    * FLOAT64

If the type is CATEGORY , only up to 100 unique values may exist in that column across all rows.

NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 




**Returns**

  * (::String) — column_spec_id of the primary table's column that should be used as the training & prediction target. This column must be non-nullable and have one of following data types (otherwise model creation will error):

    * CATEGORY

    * FLOAT64

If the type is CATEGORY , only up to 100 unique values may exist in that column across all rows.

NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 




### #weight_column_spec_id
    
    
    def weight_column_spec_id() -> ::String

**Returns**

  * (::String) — column_spec_id of the primary table's column that should be used as the weight column, i.e. the higher the value the more important the row will be during model training. Required type: FLOAT64. Allowed values: 0 to 10000, inclusive on both ends; 0 means the row is ignored for training. If not set all rows are assumed to have equal weight of 1. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 



### #weight_column_spec_id=
    
    
    def weight_column_spec_id=(value) -> ::String

**Parameter**

  * **value** (::String) — column_spec_id of the primary table's column that should be used as the weight column, i.e. the higher the value the more important the row will be during model training. Required type: FLOAT64. Allowed values: 0 to 10000, inclusive on both ends; 0 means the row is ignored for training. If not set all rows are assumed to have equal weight of 1. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 



**Returns**

  * (::String) — column_spec_id of the primary table's column that should be used as the weight column, i.e. the higher the value the more important the row will be during model training. Required type: FLOAT64. Allowed values: 0 to 10000, inclusive on both ends; 0 means the row is ignored for training. If not set all rows are assumed to have equal weight of 1. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
