---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::InputDataConfig (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:50.324003+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::InputDataConfig (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::InputDataConfig (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::InputDataConfig.

Specifies Vertex AI owned input data to be used for training, and possibly evaluating, the Model.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotation_schema_uri
    
    
    def annotation_schema_uri() -> ::String

**Returns**

  * (::String) — Applicable only to custom training with Datasets that have DataItems and Annotations.

Cloud Storage URI that points to a YAML file describing the annotation schema. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/ , note that the chosen schema must be consistent with [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Dataset#Google__Cloud__AIPlatform__V1__Dataset_metadata_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Dataset#metadata_schema_uri \(method\)") of the Dataset specified by [dataset_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_dataset_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#dataset_id \(method\)").

Only Annotations that both match this schema and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on.

When used in conjunction with [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)"), the Annotations used for training are filtered by both [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)") and [annotation_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotation_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotation_schema_uri \(method\)"). 




### #annotation_schema_uri=
    
    
    def annotation_schema_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Applicable only to custom training with Datasets that have DataItems and Annotations.

Cloud Storage URI that points to a YAML file describing the annotation schema. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/ , note that the chosen schema must be consistent with [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Dataset#Google__Cloud__AIPlatform__V1__Dataset_metadata_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Dataset#metadata_schema_uri \(method\)") of the Dataset specified by [dataset_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_dataset_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#dataset_id \(method\)").

Only Annotations that both match this schema and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on.

When used in conjunction with [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)"), the Annotations used for training are filtered by both [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)") and [annotation_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotation_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotation_schema_uri \(method\)"). 




**Returns**

  * (::String) — Applicable only to custom training with Datasets that have DataItems and Annotations.

Cloud Storage URI that points to a YAML file describing the annotation schema. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/ , note that the chosen schema must be consistent with [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Dataset#Google__Cloud__AIPlatform__V1__Dataset_metadata_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Dataset#metadata_schema_uri \(method\)") of the Dataset specified by [dataset_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_dataset_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#dataset_id \(method\)").

Only Annotations that both match this schema and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on.

When used in conjunction with [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)"), the Annotations used for training are filtered by both [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)") and [annotation_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotation_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotation_schema_uri \(method\)"). 




### #annotations_filter
    
    
    def annotations_filter() -> ::String

**Returns**

  * (::String) — Applicable only to Datasets that have DataItems and Annotations.

A filter on Annotations of the Dataset. Only Annotations that both match this filter and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on (for the auto-assigned that role is decided by Vertex AI). A filter with same syntax as the one used in [ListAnnotations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DatasetService-Client#Google__Cloud__AIPlatform__V1__DatasetService__Client_list_annotations_instance_ "Google::Cloud::AIPlatform::V1::DatasetService::Client#list_annotations \(method\)") may be used, but note here it filters across all Annotations of the Dataset, and not just within a single DataItem. 




### #annotations_filter=
    
    
    def annotations_filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Applicable only to Datasets that have DataItems and Annotations.

A filter on Annotations of the Dataset. Only Annotations that both match this filter and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on (for the auto-assigned that role is decided by Vertex AI). A filter with same syntax as the one used in [ListAnnotations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DatasetService-Client#Google__Cloud__AIPlatform__V1__DatasetService__Client_list_annotations_instance_ "Google::Cloud::AIPlatform::V1::DatasetService::Client#list_annotations \(method\)") may be used, but note here it filters across all Annotations of the Dataset, and not just within a single DataItem. 




**Returns**

  * (::String) — Applicable only to Datasets that have DataItems and Annotations.

A filter on Annotations of the Dataset. Only Annotations that both match this filter and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on (for the auto-assigned that role is decided by Vertex AI). A filter with same syntax as the one used in [ListAnnotations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DatasetService-Client#Google__Cloud__AIPlatform__V1__DatasetService__Client_list_annotations_instance_ "Google::Cloud::AIPlatform::V1::DatasetService::Client#list_annotations \(method\)") may be used, but note here it filters across all Annotations of the Dataset, and not just within a single DataItem. 




### #bigquery_destination
    
    
    def bigquery_destination() -> ::Google::Cloud::AIPlatform::V1::BigQueryDestination

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BigQueryDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BigQueryDestination)) — Only applicable to custom training with tabular Dataset with BigQuery source.

The BigQuery project location where the training data is to be written to. In the given project a new dataset is created with name `dataset_<dataset-id>_<annotation-type>_<timestamp-of-training-call>` where timestamp is in YYYY_MM_DDThh_mm_ss_sssZ format. All training input data is written into that dataset. In the dataset three tables are created, `training`, `validation` and `test`.

    * AIP_DATA_FORMAT = "bigquery".
    * AIP_TRAINING_DATA_URI = "bigquery_destination.dataset_

    * AIP_VALIDATION_DATA_URI = "bigquery_destination.dataset_

    * AIP_TEST_DATA_URI = "bigquery_destination.dataset_

Note: The following fields are mutually exclusive: `bigquery_destination`, `gcs_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bigquery_destination=
    
    
    def bigquery_destination=(value) -> ::Google::Cloud::AIPlatform::V1::BigQueryDestination

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::BigQueryDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BigQueryDestination)) — Only applicable to custom training with tabular Dataset with BigQuery source.

The BigQuery project location where the training data is to be written to. In the given project a new dataset is created with name `dataset_<dataset-id>_<annotation-type>_<timestamp-of-training-call>` where timestamp is in YYYY_MM_DDThh_mm_ss_sssZ format. All training input data is written into that dataset. In the dataset three tables are created, `training`, `validation` and `test`.

    * AIP_DATA_FORMAT = "bigquery".
    * AIP_TRAINING_DATA_URI = "bigquery_destination.dataset_

    * AIP_VALIDATION_DATA_URI = "bigquery_destination.dataset_

    * AIP_TEST_DATA_URI = "bigquery_destination.dataset_

Note: The following fields are mutually exclusive: `bigquery_destination`, `gcs_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BigQueryDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BigQueryDestination)) — Only applicable to custom training with tabular Dataset with BigQuery source.

The BigQuery project location where the training data is to be written to. In the given project a new dataset is created with name `dataset_<dataset-id>_<annotation-type>_<timestamp-of-training-call>` where timestamp is in YYYY_MM_DDThh_mm_ss_sssZ format. All training input data is written into that dataset. In the dataset three tables are created, `training`, `validation` and `test`.

    * AIP_DATA_FORMAT = "bigquery".
    * AIP_TRAINING_DATA_URI = "bigquery_destination.dataset_

    * AIP_VALIDATION_DATA_URI = "bigquery_destination.dataset_

    * AIP_TEST_DATA_URI = "bigquery_destination.dataset_

Note: The following fields are mutually exclusive: `bigquery_destination`, `gcs_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dataset_id
    
    
    def dataset_id() -> ::String

**Returns**

  * (::String) — Required. The ID of the Dataset in the same Project and Location which data will be used to train the Model. The Dataset must use schema compatible with Model being trained, and what is compatible should be described in the used TrainingPipeline's [training_task_definition] [google.cloud.aiplatform.v1.TrainingPipeline.training_task_definition]. For tabular Datasets, all their data is exported to training, to pick and choose from. 



### #dataset_id=
    
    
    def dataset_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of the Dataset in the same Project and Location which data will be used to train the Model. The Dataset must use schema compatible with Model being trained, and what is compatible should be described in the used TrainingPipeline's [training_task_definition] [google.cloud.aiplatform.v1.TrainingPipeline.training_task_definition]. For tabular Datasets, all their data is exported to training, to pick and choose from. 



**Returns**

  * (::String) — Required. The ID of the Dataset in the same Project and Location which data will be used to train the Model. The Dataset must use schema compatible with Model being trained, and what is compatible should be described in the used TrainingPipeline's [training_task_definition] [google.cloud.aiplatform.v1.TrainingPipeline.training_task_definition]. For tabular Datasets, all their data is exported to training, to pick and choose from. 



### #filter_split
    
    
    def filter_split() -> ::Google::Cloud::AIPlatform::V1::FilterSplit

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FilterSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FilterSplit)) — Split based on the provided filters for each set.

Note: The following fields are mutually exclusive: `filter_split`, `fraction_split`, `predefined_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #filter_split=
    
    
    def filter_split=(value) -> ::Google::Cloud::AIPlatform::V1::FilterSplit

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::FilterSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FilterSplit)) — Split based on the provided filters for each set.

Note: The following fields are mutually exclusive: `filter_split`, `fraction_split`, `predefined_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FilterSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FilterSplit)) — Split based on the provided filters for each set.

Note: The following fields are mutually exclusive: `filter_split`, `fraction_split`, `predefined_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #fraction_split
    
    
    def fraction_split() -> ::Google::Cloud::AIPlatform::V1::FractionSplit

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FractionSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FractionSplit)) — Split based on fractions defining the size of each set.

Note: The following fields are mutually exclusive: `fraction_split`, `filter_split`, `predefined_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #fraction_split=
    
    
    def fraction_split=(value) -> ::Google::Cloud::AIPlatform::V1::FractionSplit

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::FractionSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FractionSplit)) — Split based on fractions defining the size of each set.

Note: The following fields are mutually exclusive: `fraction_split`, `filter_split`, `predefined_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FractionSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FractionSplit)) — Split based on fractions defining the size of each set.

Note: The following fields are mutually exclusive: `fraction_split`, `filter_split`, `predefined_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_destination
    
    
    def gcs_destination() -> ::Google::Cloud::AIPlatform::V1::GcsDestination

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::GcsDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GcsDestination)) — The Cloud Storage location where the training data is to be written to. In the given directory a new directory is created with name: `dataset-<dataset-id>-<annotation-type>-<timestamp-of-training-call>` where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. All training input data is written into that directory.

The Vertex AI environment variables representing Cloud Storage data URIs are represented in the Cloud Storage wildcard format to support sharded data. e.g.: "gs://.../training-*.jsonl"

    * AIP_DATA_FORMAT = "jsonl" for non-tabular data, "csv" for tabular data
    * AIP_TRAINING_DATA_URI = "gcs_destination/dataset-

    * AIP_VALIDATION_DATA_URI = "gcs_destination/dataset-

    * AIP_TEST_DATA_URI = "gcs_destination/dataset-

Note: The following fields are mutually exclusive: `gcs_destination`, `bigquery_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_destination=
    
    
    def gcs_destination=(value) -> ::Google::Cloud::AIPlatform::V1::GcsDestination

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::GcsDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GcsDestination)) — The Cloud Storage location where the training data is to be written to. In the given directory a new directory is created with name: `dataset-<dataset-id>-<annotation-type>-<timestamp-of-training-call>` where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. All training input data is written into that directory.

The Vertex AI environment variables representing Cloud Storage data URIs are represented in the Cloud Storage wildcard format to support sharded data. e.g.: "gs://.../training-*.jsonl"

    * AIP_DATA_FORMAT = "jsonl" for non-tabular data, "csv" for tabular data
    * AIP_TRAINING_DATA_URI = "gcs_destination/dataset-

    * AIP_VALIDATION_DATA_URI = "gcs_destination/dataset-

    * AIP_TEST_DATA_URI = "gcs_destination/dataset-

Note: The following fields are mutually exclusive: `gcs_destination`, `bigquery_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::GcsDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GcsDestination)) — The Cloud Storage location where the training data is to be written to. In the given directory a new directory is created with name: `dataset-<dataset-id>-<annotation-type>-<timestamp-of-training-call>` where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. All training input data is written into that directory.

The Vertex AI environment variables representing Cloud Storage data URIs are represented in the Cloud Storage wildcard format to support sharded data. e.g.: "gs://.../training-*.jsonl"

    * AIP_DATA_FORMAT = "jsonl" for non-tabular data, "csv" for tabular data
    * AIP_TRAINING_DATA_URI = "gcs_destination/dataset-

    * AIP_VALIDATION_DATA_URI = "gcs_destination/dataset-

    * AIP_TEST_DATA_URI = "gcs_destination/dataset-

Note: The following fields are mutually exclusive: `gcs_destination`, `bigquery_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #persist_ml_use_assignment
    
    
    def persist_ml_use_assignment() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to persist the ML use assignment to data item system labels. 



### #persist_ml_use_assignment=
    
    
    def persist_ml_use_assignment=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to persist the ML use assignment to data item system labels. 



**Returns**

  * (::Boolean) — Whether to persist the ML use assignment to data item system labels. 



### #predefined_split
    
    
    def predefined_split() -> ::Google::Cloud::AIPlatform::V1::PredefinedSplit

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::PredefinedSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredefinedSplit)) — Supported only for tabular Datasets.

Split based on a predefined key.

Note: The following fields are mutually exclusive: `predefined_split`, `fraction_split`, `filter_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #predefined_split=
    
    
    def predefined_split=(value) -> ::Google::Cloud::AIPlatform::V1::PredefinedSplit

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::PredefinedSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredefinedSplit)) — Supported only for tabular Datasets.

Split based on a predefined key.

Note: The following fields are mutually exclusive: `predefined_split`, `fraction_split`, `filter_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::PredefinedSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredefinedSplit)) — Supported only for tabular Datasets.

Split based on a predefined key.

Note: The following fields are mutually exclusive: `predefined_split`, `fraction_split`, `filter_split`, `timestamp_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #saved_query_id
    
    
    def saved_query_id() -> ::String

**Returns**

  * (::String) — Only applicable to Datasets that have SavedQueries.

The ID of a SavedQuery (annotation set) under the Dataset specified by [dataset_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_dataset_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#dataset_id \(method\)") used for filtering Annotations for training.

Only Annotations that are associated with this SavedQuery are used in respectively training. When used in conjunction with [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)"), the Annotations used for training are filtered by both [saved_query_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_saved_query_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#saved_query_id \(method\)") and [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)").

Only one of [saved_query_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_saved_query_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#saved_query_id \(method\)") and [annotation_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotation_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotation_schema_uri \(method\)") should be specified as both of them represent the same thing: problem type. 




### #saved_query_id=
    
    
    def saved_query_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Only applicable to Datasets that have SavedQueries.

The ID of a SavedQuery (annotation set) under the Dataset specified by [dataset_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_dataset_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#dataset_id \(method\)") used for filtering Annotations for training.

Only Annotations that are associated with this SavedQuery are used in respectively training. When used in conjunction with [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)"), the Annotations used for training are filtered by both [saved_query_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_saved_query_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#saved_query_id \(method\)") and [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)").

Only one of [saved_query_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_saved_query_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#saved_query_id \(method\)") and [annotation_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotation_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotation_schema_uri \(method\)") should be specified as both of them represent the same thing: problem type. 




**Returns**

  * (::String) — Only applicable to Datasets that have SavedQueries.

The ID of a SavedQuery (annotation set) under the Dataset specified by [dataset_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_dataset_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#dataset_id \(method\)") used for filtering Annotations for training.

Only Annotations that are associated with this SavedQuery are used in respectively training. When used in conjunction with [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)"), the Annotations used for training are filtered by both [saved_query_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_saved_query_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#saved_query_id \(method\)") and [annotations_filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotations_filter_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotations_filter \(method\)").

Only one of [saved_query_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_saved_query_id_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#saved_query_id \(method\)") and [annotation_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-InputDataConfig#Google__Cloud__AIPlatform__V1__InputDataConfig_annotation_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::InputDataConfig#annotation_schema_uri \(method\)") should be specified as both of them represent the same thing: problem type. 




### #stratified_split
    
    
    def stratified_split() -> ::Google::Cloud::AIPlatform::V1::StratifiedSplit

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::StratifiedSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-StratifiedSplit)) — Supported only for tabular Datasets.

Split based on the distribution of the specified column.

Note: The following fields are mutually exclusive: `stratified_split`, `fraction_split`, `filter_split`, `predefined_split`, `timestamp_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #stratified_split=
    
    
    def stratified_split=(value) -> ::Google::Cloud::AIPlatform::V1::StratifiedSplit

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::StratifiedSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-StratifiedSplit)) — Supported only for tabular Datasets.

Split based on the distribution of the specified column.

Note: The following fields are mutually exclusive: `stratified_split`, `fraction_split`, `filter_split`, `predefined_split`, `timestamp_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::StratifiedSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-StratifiedSplit)) — Supported only for tabular Datasets.

Split based on the distribution of the specified column.

Note: The following fields are mutually exclusive: `stratified_split`, `fraction_split`, `filter_split`, `predefined_split`, `timestamp_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #timestamp_split
    
    
    def timestamp_split() -> ::Google::Cloud::AIPlatform::V1::TimestampSplit

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::TimestampSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TimestampSplit)) — Supported only for tabular Datasets.

Split based on the timestamp of the input data pieces.

Note: The following fields are mutually exclusive: `timestamp_split`, `fraction_split`, `filter_split`, `predefined_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #timestamp_split=
    
    
    def timestamp_split=(value) -> ::Google::Cloud::AIPlatform::V1::TimestampSplit

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::TimestampSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TimestampSplit)) — Supported only for tabular Datasets.

Split based on the timestamp of the input data pieces.

Note: The following fields are mutually exclusive: `timestamp_split`, `fraction_split`, `filter_split`, `predefined_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::TimestampSplit](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TimestampSplit)) — Supported only for tabular Datasets.

Split based on the timestamp of the input data pieces.

Note: The following fields are mutually exclusive: `timestamp_split`, `fraction_split`, `filter_split`, `predefined_split`, `stratified_split`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
