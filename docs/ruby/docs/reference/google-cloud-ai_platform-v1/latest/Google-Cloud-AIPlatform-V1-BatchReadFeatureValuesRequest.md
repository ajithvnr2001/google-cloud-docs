---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:56.065625+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest.

Request message for [FeaturestoreService.BatchReadFeatureValues](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_batch_read_feature_values_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#batch_read_feature_values \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bigquery_read_instances
    
    
    def bigquery_read_instances() -> ::Google::Cloud::AIPlatform::V1::BigQuerySource

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BigQuerySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BigQuerySource)) — Similar to csv_read_instances, but from BigQuery source.

Note: The following fields are mutually exclusive: `bigquery_read_instances`, `csv_read_instances`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bigquery_read_instances=
    
    
    def bigquery_read_instances=(value) -> ::Google::Cloud::AIPlatform::V1::BigQuerySource

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::BigQuerySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BigQuerySource)) — Similar to csv_read_instances, but from BigQuery source.

Note: The following fields are mutually exclusive: `bigquery_read_instances`, `csv_read_instances`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BigQuerySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BigQuerySource)) — Similar to csv_read_instances, but from BigQuery source.

Note: The following fields are mutually exclusive: `bigquery_read_instances`, `csv_read_instances`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #csv_read_instances
    
    
    def csv_read_instances() -> ::Google::Cloud::AIPlatform::V1::CsvSource

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::CsvSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CsvSource)) — Each read instance consists of exactly one read timestamp and one or more entity IDs identifying entities of the corresponding EntityTypes whose Features are requested.

Each output instance contains Feature values of requested entities concatenated together as of the read time.

An example read instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z`.

An example output instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z, foo_entity_feature1_value, bar_entity_feature2_value`.

Timestamp in each read instance must be millisecond-aligned.

`csv_read_instances` are read instances stored in a plain-text CSV file. The header should be: [ENTITY_TYPE_ID1], [ENTITY_TYPE_ID2], ..., timestamp

The columns can be in any order.

Values in the timestamp column must use the RFC 3339 format, e.g. `2012-07-30T10:43:17.123Z`.

Note: The following fields are mutually exclusive: `csv_read_instances`, `bigquery_read_instances`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #csv_read_instances=
    
    
    def csv_read_instances=(value) -> ::Google::Cloud::AIPlatform::V1::CsvSource

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::CsvSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CsvSource)) — Each read instance consists of exactly one read timestamp and one or more entity IDs identifying entities of the corresponding EntityTypes whose Features are requested.

Each output instance contains Feature values of requested entities concatenated together as of the read time.

An example read instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z`.

An example output instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z, foo_entity_feature1_value, bar_entity_feature2_value`.

Timestamp in each read instance must be millisecond-aligned.

`csv_read_instances` are read instances stored in a plain-text CSV file. The header should be: [ENTITY_TYPE_ID1], [ENTITY_TYPE_ID2], ..., timestamp

The columns can be in any order.

Values in the timestamp column must use the RFC 3339 format, e.g. `2012-07-30T10:43:17.123Z`.

Note: The following fields are mutually exclusive: `csv_read_instances`, `bigquery_read_instances`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::CsvSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CsvSource)) — Each read instance consists of exactly one read timestamp and one or more entity IDs identifying entities of the corresponding EntityTypes whose Features are requested.

Each output instance contains Feature values of requested entities concatenated together as of the read time.

An example read instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z`.

An example output instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z, foo_entity_feature1_value, bar_entity_feature2_value`.

Timestamp in each read instance must be millisecond-aligned.

`csv_read_instances` are read instances stored in a plain-text CSV file. The header should be: [ENTITY_TYPE_ID1], [ENTITY_TYPE_ID2], ..., timestamp

The columns can be in any order.

Values in the timestamp column must use the RFC 3339 format, e.g. `2012-07-30T10:43:17.123Z`.

Note: The following fields are mutually exclusive: `csv_read_instances`, `bigquery_read_instances`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #destination
    
    
    def destination() -> ::Google::Cloud::AIPlatform::V1::FeatureValueDestination

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FeatureValueDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureValueDestination)) — Required. Specifies output location and format. 



### #destination=
    
    
    def destination=(value) -> ::Google::Cloud::AIPlatform::V1::FeatureValueDestination

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::FeatureValueDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureValueDestination)) — Required. Specifies output location and format. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FeatureValueDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureValueDestination)) — Required. Specifies output location and format. 



### #entity_type_specs
    
    
    def entity_type_specs() -> ::Array<::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::EntityTypeSpec>

**Returns**

  * (::Array<[::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::EntityTypeSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest-EntityTypeSpec)>) — Required. Specifies EntityType grouping Features to read values of and settings. 



### #entity_type_specs=
    
    
    def entity_type_specs=(value) -> ::Array<::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::EntityTypeSpec>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::EntityTypeSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest-EntityTypeSpec)>) — Required. Specifies EntityType grouping Features to read values of and settings. 



**Returns**

  * (::Array<[::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::EntityTypeSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest-EntityTypeSpec)>) — Required. Specifies EntityType grouping Features to read values of and settings. 



### #featurestore
    
    
    def featurestore() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Featurestore from which to query Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`



### #featurestore=
    
    
    def featurestore=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Featurestore from which to query Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`



**Returns**

  * (::String) — Required. The resource name of the Featurestore from which to query Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`



### #pass_through_fields
    
    
    def pass_through_fields() -> ::Array<::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::PassThroughField>

**Returns**

  * (::Array<[::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::PassThroughField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest-PassThroughField)>) — When not empty, the specified fields in the *_read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity.

For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes. 




### #pass_through_fields=
    
    
    def pass_through_fields=(value) -> ::Array<::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::PassThroughField>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::PassThroughField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest-PassThroughField)>) — When not empty, the specified fields in the *_read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity.

For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes. 




**Returns**

  * (::Array<[::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::PassThroughField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest-PassThroughField)>) — When not empty, the specified fields in the *_read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity.

For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes. 




### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Optional. Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision. 



### #start_time=
    
    
    def start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Optional. Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Optional. Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
